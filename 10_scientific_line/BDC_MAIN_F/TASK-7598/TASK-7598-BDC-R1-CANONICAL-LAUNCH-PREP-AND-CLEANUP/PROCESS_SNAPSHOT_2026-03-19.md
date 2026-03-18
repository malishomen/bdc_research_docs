# PROCESS SNAPSHOT 2026-03-19

## Host State
- Collected at: $(@{collected_at_utc=03/18/2026 23:44:07; logical_cpu=8; total_cpu_percent=4; free_memory_mb=7509; gpu=System.Object[]; python_process_count=8; python_processes=System.Object[]; top_processes=System.Object[]}.collected_at_utc)
- Logical CPU: $(@{collected_at_utc=03/18/2026 23:44:07; logical_cpu=8; total_cpu_percent=4; free_memory_mb=7509; gpu=System.Object[]; python_process_count=8; python_processes=System.Object[]; top_processes=System.Object[]}.logical_cpu)
- Total CPU at snapshot: $(@{collected_at_utc=03/18/2026 23:44:07; logical_cpu=8; total_cpu_percent=4; free_memory_mb=7509; gpu=System.Object[]; python_process_count=8; python_processes=System.Object[]; top_processes=System.Object[]}.total_cpu_percent)%
- Free memory: $(@{collected_at_utc=03/18/2026 23:44:07; logical_cpu=8; total_cpu_percent=4; free_memory_mb=7509; gpu=System.Object[]; python_process_count=8; python_processes=System.Object[]; top_processes=System.Object[]}.free_memory_mb) MB
- GPU: $(@{collected_at_utc=03/18/2026 23:44:07; logical_cpu=8; total_cpu_percent=4; free_memory_mb=7509; gpu=System.Object[]; python_process_count=8; python_processes=System.Object[]; top_processes=System.Object[]}.gpu[0].name)
- GPU utilization: $(@{collected_at_utc=03/18/2026 23:44:07; logical_cpu=8; total_cpu_percent=4; free_memory_mb=7509; gpu=System.Object[]; python_process_count=8; python_processes=System.Object[]; top_processes=System.Object[]}.gpu[0].utilization_gpu)
- Python process count: $(@{collected_at_utc=03/18/2026 23:44:07; logical_cpu=8; total_cpu_percent=4; free_memory_mb=7509; gpu=System.Object[]; python_process_count=8; python_processes=System.Object[]; top_processes=System.Object[]}.python_process_count)

## Launch Impact
- Host condition is better than the earlier snapshot because free memory is now above 7 GB and instantaneous CPU usage is low.
- The machine is still not clean enough for the canonical R1 long run because the cleanup preview identifies $(@{collected_at_utc=03/18/2026 23:44:21; execute=False; codex_protected=True; target_count=32; targets=System.Object[]; terminated=System.Object[]}.target_count) non-essential interference targets.
- Main long-run interference families remain AI desktop clients, dev servers, Docker/WSL, and auxiliary editor/runtime processes.

## Cleanup Preview Groups
- `claude.exe`: 13
- `node.exe`: 7
- `ChatGPT.exe`: 5
- `com.docker.backend.exe`: 2
- `python.exe`: 2
- `Telegram.exe`: 1
- `vmmemWSL`: 1
- `wslservice.exe`: 1

## Highest Python Noise
- PID 33148 :: C:\Users\user\AppData\Roaming\uv\python\cpython-3.13.12-windows-x86_64-none\python.exe :: CPU=214.40625 :: WS_MB=63.8
- PID 135296 :: C:\Users\user\AppData\Roaming\uv\python\cpython-3.13.12-windows-x86_64-none\python.exe :: CPU=54.296875 :: WS_MB=63.6
- PID 212424 :: C:\Users\user\AppData\Local\Programs\Python\Python311\python.exe :: CPU=54.234375 :: WS_MB=151.8

## Operational Interpretation
- Codex is excluded from termination targets by script rule.
- The cleanup script is suitable for pre-run host reduction, but should still be treated as operational tooling, not as part of the scientific protocol.
- The canonical next step remains: run cleanup in execute mode only when the operator is ready to launch the full R1 sweep immediately after.
