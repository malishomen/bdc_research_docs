# Process Snapshot - 2026-03-18

## Snapshot source
- JSON source: `reports/analysis/TASK-7594-BDC-SELECTION-PHYSICS-R1-LAUNCH-PREP/host_snapshot.json`
- Collection time (UTC): `2026-03-18T18:38:11Z`

## Host summary
- Logical CPU: `8`
- Total CPU at capture: `14%`
- Free memory: `4144.6 MB`
- GPU present: `NVIDIA GeForce GTX 1080 Ti`
- GPU utilization at capture: `6%`
- GPU memory used: `1762 MiB / 11264 MiB`
- Python process count at capture: `12`

## High-impact competing load

### Continuous/background system pressure
- `vmmemWSL` - very high resident memory (`~1078.7 MB WS`, `~7841.1 MB PM`)
- `com.docker.backend` - active Docker backend with long-lived CPU history
- `MsMpEng` - Windows Defender, non-trivial background CPU and memory usage
- `Memory Compression` - high memory pressure indicator

### Interactive/user-space pressure
- `Codex`
- `claude`
- `ChatGPT` (multiple processes)
- `Telegram`
- `msedge`

These are not catastrophic by themselves, but they reduce headroom for a multi-hour CPU long-run.

### Python-specific contention
Notable long-lived or warm Python processes at capture:
- PID `33148` - `uv` Python, cumulative CPU `197.09`
- PID `135296` - `uv` Python, cumulative CPU `37.75`
- PID `96432` - Python 3.11, cumulative CPU `35.14`

There are also multiple low-activity helper/interpreter processes which increase scheduler noise and memory fragmentation.

## Impact on canonical Phase R1 run

### What this means
The workstation is not idle.

The captured state is consistent with a machine that can run the `R1` sweep, but not at maximum safe parallelism.

### Why GPU is not the main accelerator
The GPU is visible and mostly idle, but the current `edp1_symbolic` path is CPU-oriented.

The long-run is driven by:
- `evolution/edp1_symbolic/run_generations.py`
- pure Python subprocess execution
- no CUDA / Torch / CuPy backend

Therefore the GPU does not materially reduce the canonical sweep time in the current implementation.

## Operational recommendation

### Recommended worker count
- Use `4` workers

### Not recommended
- `8` workers on this machine under the current background load
- launching while additional Python-heavy jobs are active
- assuming GPU availability changes the runtime in the current code path

## Pre-launch cleanup recommendation
Before starting the canonical `R1` long-run:
1. stop non-essential Python jobs
2. stop or reduce Docker/WSL pressure if not needed
3. avoid concurrent notebook/CLI experiments
4. keep the launch at `4` workers unless the machine is measurably cleaner

## Bottom line
The machine is capable of running the full canonical `Phase R1` sweep.

But in the captured state it is a **contended CPU host**, not a clean dedicated worker.

The safe choice remains:
- `4` parallel workers
- previewed launch plan only until the machine is cleaned
