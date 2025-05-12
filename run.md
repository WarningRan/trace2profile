```
conda create -n trace2profile python=3.10 cmake
python3.9 -m pip install --upgrade pip
conda activate trace2profile
protoc --python_out=. profile.proto
python3 -m pip install --upgrade protobuf
pip install -r requirements.txt
```

to download profile.proto 

`curl -O https://raw.githubusercontent.com/google/pprof/master/proto/profile.proto`

to generate profile_pb2

`protoc --python_out=. profile.proto`

To convert trace 2 pprof

`python3 trace2profile.py css-host-183_3244036.1745803131531804330.pt.trace.json css-host-183_3244036.1745803131531804330.pt.trace.pb
`

```
which pprof
brew install pprof
brew install --cask approf

brew install go
go install github.com/google/pprof@latest
~/go/bin/pprof -top css-host-183_3244036.1745803131531804330.pt.trace.pb
```

```
Main binary filename not available.
Type: cpu
Showing nodes accounting for 12.44s, 92.25% of 13.48s total
Dropped 1389 nodes (cum <= 0.07s)
      flat  flat%   sum%        cum   cum%
     0.89s  6.57%  6.57%      0.89s  6.57%  threading.py(1002): _bootstrap
     0.89s  6.57% 13.13%      0.89s  6.57%  threading.py(1045): _bootstrap_inner
     0.59s  4.38% 17.51%      0.59s  4.38%  tqdm/_monitor.py(60): run
     0.59s  4.38% 21.89%      0.59s  4.38%  threading.py(629): wait
     0.59s  4.38% 26.26%      0.59s  4.38%  threading.py(331): wait
     0.40s  2.97% 29.23%      0.40s  2.97%  torch/utils/_contextlib.py(113): decorate_context
     0.30s  2.19% 31.42%      0.30s  2.19%  PyTorch Profiler (0)
     0.30s  2.19% 33.61%      0.30s  2.19%  threading.py(982): run
     0.30s  2.19% 35.80%      0.30s  2.19%  /net/storage149/mnt/md0/zhuoran/fmwork-v22/fmwork-v2.2-0306/vllm/vllm/usage/usage_lib.py(162): _report_usage_worker
     0.30s  2.19% 37.99%      0.30s  2.19%  /net/storage149/mnt/md0/zhuoran/fmwork-v22/fmwork-v2.2-0306/vllm/vllm/usage/usage_lib.py(182): _report_usage_once
     0.30s  2.19% 40.18%      0.30s  2.19%  cpuinfo/cpuinfo.py(2759): get_cpu_info
     0.30s  2.19% 42.37%      0.30s  2.19%  cpuinfo/cpuinfo.py(2742): get_cpu_info_json
     0.30s  2.19% 44.56%      0.30s  2.19%  subprocess.py(1209): communicate
     0.30s  2.19% 46.74%      0.30s  2.19%  subprocess.py(2115): _communicate
     0.30s  2.19% 48.93%      0.30s  2.19%  selectors.py(415): select
     0.30s  2.19% 51.12%      0.30s  2.19%  driver.datasets(260): <module>
     0.30s  2.19% 53.31%      0.30s  2.19%  driver.datasets(26): main
     0.30s  2.19% 55.50%      0.30s  2.19%  driver.datasets(142): runs
     0.30s  2.19% 57.69%      0.30s  2.19%  driver.datasets(242): run
     0.29s  2.18% 59.87%      0.29s  2.18%  /net/storage149/mnt/md0/zhuoran/fmwork-v22/fmwork-v2.2-0306/vllm/vllm/utils.py(1072): inner
     0.29s  2.18% 62.05%      0.29s  2.18%  /net/storage149/mnt/md0/zhuoran/fmwork-v22/fmwork-v2.2-0306/vllm/vllm/entrypoints/llm.py(377): generate
     0.29s  2.17% 64.21%      0.29s  2.17%  /net/storage149/mnt/md0/zhuoran/fmwork-v22/fmwork-v2.2-0306/vllm/vllm/entrypoints/llm.py(1361): _run_engine
     0.29s  2.16% 66.38%      0.29s  2.16%  /net/storage149/mnt/md0/zhuoran/fmwork-v22/fmwork-v2.2-0306/vllm/vllm/engine/llm_engine.py(1268): step
     0.29s  2.16% 68.54%      0.29s  2.16%  torch/nn/modules/module.py(1740): _call_impl
     0.29s  2.15% 70.69%      0.29s  2.15%  /net/storage149/mnt/md0/zhuoran/fmwork-v22/fmwork-v2.2-0306/vllm/vllm/executor/executor_base.py(273): execute_model
     0.29s  2.14% 72.83%      0.29s  2.14%  /net/storage149/mnt/md0/zhuoran/fmwork-v22/fmwork-v2.2-0306/vllm/vllm/executor/mp_distributed_executor.py(136): _driver_execute_model
     0.29s  2.14% 74.98%      0.29s  2.14%  /net/storage149/mnt/md0/zhuoran/fmwork-v22/fmwork-v2.2-0306/vllm/vllm/worker/worker_base.py(386): execute_model
     0.28s  2.10% 77.07%      0.28s  2.10%  /net/storage149/mnt/md0/zhuoran/fmwork-v22/fmwork-v2.2-0306/vllm/vllm/worker/multi_step_model_runner.py(460): execute_model
     0.17s  1.27% 78.34%      0.17s  1.27%  ProfilerStep#1
     0.17s  1.22% 79.57%      0.17s  1.22%  ProfilerStep#3
     0.16s  1.22% 80.79%      0.16s  1.22%  ProfilerStep#2
     0.16s  1.16% 81.95%      0.16s  1.16%  /net/storage149/mnt/md0/zhuoran/fmwork-v22/fmwork-v2.2-0306/vllm/vllm/worker/multi_step_model_runner.py(411): _final_process_outputs
     0.16s  1.15% 83.10%      0.16s  1.15%  /net/storage149/mnt/md0/zhuoran/fmwork-v22/fmwork-v2.2-0306/vllm/vllm/worker/multi_step_model_runner.py(112): _pythonize_sampler_output
     0.15s  1.15% 84.24%      0.15s  1.15%  /net/storage149/mnt/md0/zhuoran/fmwork-v22/fmwork-v2.2-0306/vllm/vllm/worker/multi_step_model_runner.py(94): pythonize
     0.15s  1.13% 85.38%      0.15s  1.13%  torch/cuda/streams.py(216): synchronize
     0.15s  1.13% 86.51%      0.15s  1.13%  <built-in method synchronize of Event object at 0x7fdfc8378960>
     0.15s  1.13% 87.64%      0.15s  1.13%  cudaEventSynchronize
     0.12s  0.86% 88.50%      0.12s  0.86%  /net/storage149/mnt/md0/zhuoran/fmwork-v22/fmwork-v2.2-0306/vllm/vllm/worker/model_runner.py(1654): execute_model
     0.08s  0.62% 89.12%      0.08s  0.62%  sm90_xmma_gemm_bf16bf16_bf16f32_f32_tn_n_tilesize64x128x64_warpgroupsize1x1x1_execute_segment_k_off_kernel__5x_cublas
     0.07s  0.53% 89.65%      0.07s  0.53%  nn.Module: GraniteForCausalLM_0
     0.07s  0.52% 90.17%      0.07s  0.52%  /net/storage149/mnt/md0/zhuoran/fmwork-v22/fmwork-v2.2-0306/vllm/vllm/model_executor/models/granite.py(389): forward
     0.07s  0.52% 90.70%      0.07s  0.52%  /net/storage149/mnt/md0/zhuoran/fmwork-v22/fmwork-v2.2-0306/vllm/vllm/compilation/decorators.py(167): __call__
     0.07s  0.52% 91.22%      0.07s  0.52%  /net/storage149/mnt/md0/zhuoran/fmwork-v22/fmwork-v2.2-0306/vllm/vllm/model_executor/models/granite.py(292): forward
     0.07s  0.51% 91.74%      0.07s  0.51%  sm90_xmma_gemm_bf16bf16_bf16f32_f32_tn_n_tilesize64x64x64_warpgroupsize1x1x1_execute_segment_k_off_kernel__5x_cublas
     0.07s  0.51% 92.25%      0.07s  0.51%  /net/storage149/mnt/md0/zhuoran/fmwork-v22/fmwork-v2.2-0306/vllm/vllm/model_executor/models/granite.py(230): forward
```

```
brew install graphviz
~/go/bin/pprof -http=:8080 css-host-183_3244036.1745803131531804330.pt.trace.pb
```



`go tool pprof css-host-183_3244036.1745803131531804330.pt.trace.pb`

top -cum
```
Showing nodes accounting for 5122.12ms, 37.99% of 13482.98ms total
Dropped 1389 nodes (cum <= 67.41ms)
Showing top 10 nodes out of 45
      flat  flat%   sum%        cum   cum%
  885.31ms  6.57%  6.57%   885.31ms  6.57%  threading.py(1002): _bootstrap
  885.31ms  6.57% 13.13%   885.31ms  6.57%  threading.py(1045): _bootstrap_inner
  590.19ms  4.38% 17.51%   590.19ms  4.38%  tqdm/_monitor.py(60): run
  590.18ms  4.38% 21.89%   590.18ms  4.38%  threading.py(629): wait
  590.18ms  4.38% 26.26%   590.18ms  4.38%  threading.py(331): wait
  400.42ms  2.97% 29.23%   400.42ms  2.97%  torch/utils/_contextlib.py(113): decorate_context
  295.18ms  2.19% 31.42%   295.18ms  2.19%  PyTorch Profiler (0)
  295.12ms  2.19% 33.61%   295.12ms  2.19%  threading.py(982): run
  295.12ms  2.19% 35.80%   295.12ms  2.19%  /net/storage149/mnt/md0/zhuoran/fmwork-v22/fmwork-v2.2-0306/vllm/vllm/usage/usage_lib.py(162): _report_usage_worker
  295.12ms  2.19% 37.99%   295.12ms  2.19%  /net/storage149/mnt/md0/zhuoran/fmwork-v22/fmwork-v2.2-0306/vllm/vllm/usage/usage_lib.py(182): _report_usage_once
```


`go tool pprof -http=:6060 css-host-183_3244036.1745803131531804330.pt.trace.pb`


## try with tensorboard
*Note*: need to add one line to `with torch.profiler.profile`
```
experimental_config=torch._C._profiler._ExperimentalConfig(verbose=True)
```

```
pip install torch_tb_profiler
tensorboard --logdir=./trace
# for server
tensorboard --logdir trace/test --bind_all
tensorboard --logdir trace/test --host=localhost --port=6006
```