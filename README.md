# trace2profile

A Python tool for converting PyTorch trace JSON data into the pprof format.

## Project Overview

**Tracing** and **Profiling** are two essential techniques for performance analysis. While tracing records discrete events with timestamps and call stacks, generating massive amounts of data that are difficult to analyze, profiling uses periodic sampling to create aggregated performance data, making it easier to pinpoint performance bottlenecks.

This project bridges the gap between these two methods. It parses PyTorch trace JSON data and converts it into the standard [pprof](https://github.com/google/pprof) (protocol buffer) format. This allows developers to use pprof's powerful visualization tools to effectively analyze and debug performance issues.

By performing this conversion, we can transform raw **trace** data into a meaningful **profile** of the system, enabling more efficient performance optimization.

## Key Technical Aspects and Multi-Core Profiler (MCP) Application

This project specifically addresses performance analysis in multi-core environments, incorporating core concepts of **MCP (Multi-Core Profiler)**.

  * **Trace Data Parsing**: The tool parses the PyTorch trace JSON file, extracting events, durations, and call stack information.
  * **Multi-Core Aggregation**: By aggregating event durations from different threads and cores as sample values, we can get a holistic view of performance. This aligns with the aggregation function of **MCP**, helping to identify "hot" functions that are frequently executed in a multi-core setting.
  * **Call Stack Reconstruction**: The code converts the trace's call stack information into the **location** and **function** structures required by pprof. This enables pprof to generate intuitive flame graphs or call graphs that clearly show function relationships.
  * **Unified Performance View**: By converting trace data from multiple cores into a single pprof file, we leverage pprof's capabilities to analyze the performance of different threads simultaneously. This allows us to identify issues like lock contention and context switching—key concerns for **MCP**—for a more comprehensive performance evaluation of the multi-core system.

## How to Use

1.  **Prepare the Environment**:
    ```bash
    conda create -n trace2profile python=3.10 cmake
    conda activate trace2profile
    ```
2.  **Install Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```
3.  **Generate Protobuf File**:
    ```bash
    curl -O https://raw.githubusercontent.com/google/pprof/master/proto/profile.proto
    protoc --python_out=. profile.proto
    ```
4.  **Perform the Conversion**:
    ```bash
    python3 trace2profile.py css-host-183_3244036.1745803131531804330.pt.trace.json css-host-183_3244036.1745803131531804330.pt.trace.pb
    ```

## Example

Using `pprof` to analyze the generated `.pb` file, you can clearly see function calls and performance hotspots in a multi-threaded environment.

```bash
~/go/bin/pprof -top css-host-183_3244036.1745803131531804330.pt.trace.pb
```

Output:

```
Showing nodes accounting for 12.44s, 92.25% of 13.48s total
Dropped 1389 nodes (cum <= 0.07s)
      flat  flat%   sum%        cum   cum%
     0.89s  6.57%  6.57%      0.89s  6.57%  threading.py(1002): _bootstrap
     0.89s  6.57% 13.13%      0.89s  6.57%  threading.py(1045): _bootstrap_inner
     ...
```

The `pprof` output reveals that thread-related functions from `threading.py` consume a significant amount of time, which aligns with the multi-core performance bottlenecks that the **MCP** approach focuses on.

You can also use `pprof`'s visualization feature:

```bash
brew install graphviz
~/go/bin/pprof -http=:8080 css-host-183_3244036.1745803131531804330.pt.trace.pb
```

## Future Plans

  * Support more trace file formats, such as Linux `perf trace`.
  * Add dedicated handling for events like lock contention and context switches to apply **MCP** techniques more precisely.
  * Develop a simple web interface for a more user-friendly visualization experience.
