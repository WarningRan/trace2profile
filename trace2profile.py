#!/usr/bin/env python3

import json
import sys
from typing import Dict, List, Any
import google.protobuf.text_format as text_format
from google.protobuf import message
import profile_pb2

def read_trace_file(file_path: str) -> Dict:
    """Read and parse the PyTorch trace JSON file."""
    with open(file_path, 'r') as f:
        return json.load(f)

def convert_trace_to_pprof(trace_data: Dict) -> profile_pb2.Profile:
    """Convert PyTorch trace data to pprof format."""
    profile = profile_pb2.Profile()
    
    # Add string table entries
    string_table = profile.string_table
    string_table.append("")  # First string is always empty
    
    # Create a mapping for string indices
    string_indices = {}
    
    def get_string_index(s: str) -> int:
        if s not in string_indices:
            string_indices[s] = len(string_table)
            string_table.append(s)
        return string_indices[s]
    
    # Add sample types
    sample_type = profile.sample_type.add()
    sample_type.type = get_string_index("cpu")
    sample_type.unit = get_string_index("nanoseconds")
    
    # Create a mapping for functions
    function_map = {}
    
    def get_function(name: str, filename: str) -> int:
        key = (name, filename)
        if key not in function_map:
            function = profile.function.add()
            function.id = len(profile.function)
            function.name = get_string_index(name)
            function.filename = get_string_index(filename)
            function_map[key] = function.id
        return function_map[key]
    
    # Process trace events
    for event in trace_data.get("traceEvents", []):
        if "dur" not in event:  # Skip events without duration
            continue
            
        # Create a new sample
        sample = profile.sample.add()
        # Convert microseconds to nanoseconds and ensure it's an integer
        duration_ns = int(event["dur"] * 1000)
        sample.value.append(duration_ns)
        
        # Get stack trace from the event
        stack = []
        if "args" in event and "stack" in event["args"]:
            stack = event["args"]["stack"]
        elif "stack" in event:
            stack = event["stack"]
        
        if not stack:
            # If no stack trace, use the event name and category
            stack = [{"name": event.get("name", "unknown"), "cat": event.get("cat", "unknown")}]
        
        # Create locations for each frame in the stack
        for frame in reversed(stack):  # Reverse to get caller -> callee order
            location = profile.location.add()
            location.id = len(profile.location)
            
            # Get function name and filename from the frame
            name = frame.get("name", "unknown")
            filename = frame.get("cat", "unknown")
            
            # Add function information
            function_id = get_function(name, filename)
            
            # Link location to function
            line = location.line.add()
            line.function_id = function_id
            
            # Add location to sample
            sample.location_id.append(location.id)
    
    return profile

def save_pprof(profile: profile_pb2.Profile, output_path: str):
    """Save the pprof profile to a file."""
    with open(output_path, 'wb') as f:
        f.write(profile.SerializeToString())

def main():
    if len(sys.argv) != 3:
        print("Usage: python trace2profile.py <input_trace.json> <output_profile.pb>")
        sys.exit(1)
        
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    
    # Read and convert
    trace_data = read_trace_file(input_file)
    profile = convert_trace_to_pprof(trace_data)
    
    # Save the result
    save_pprof(profile, output_file)
    print(f"Successfully converted {input_file} to {output_file}")

if __name__ == "__main__":
    main()