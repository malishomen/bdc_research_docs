# PROCESS STATE POST CLEANUP 2026-03-19

## Cleanup Result
- Target count: $(@{collected_at_utc=03/19/2026 00:09:55; execute=True; codex_protected=True; target_count=7; targets=System.Object[]; terminated=System.Object[]}.target_count)
- Terminated successfully: $terminatedOk
- Termination failures: $terminatedFail
- Main failure: mmemWSL remained due to access denial.

## Post-Cleanup Host
- Collected at: $(@{collected_at_utc=03/19/2026 00:10:03; logical_cpu=8; total_cpu_percent=17; free_memory_mb=15563; gpu=System.Object[]; python_process_count=0; python_processes=; top_processes=System.Object[]}.collected_at_utc)
- Logical CPU: $(@{collected_at_utc=03/19/2026 00:10:03; logical_cpu=8; total_cpu_percent=17; free_memory_mb=15563; gpu=System.Object[]; python_process_count=0; python_processes=; top_processes=System.Object[]}.logical_cpu)
- Total CPU at snapshot: $(@{collected_at_utc=03/19/2026 00:10:03; logical_cpu=8; total_cpu_percent=17; free_memory_mb=15563; gpu=System.Object[]; python_process_count=0; python_processes=; top_processes=System.Object[]}.total_cpu_percent)%
- Free memory: $(@{collected_at_utc=03/19/2026 00:10:03; logical_cpu=8; total_cpu_percent=17; free_memory_mb=15563; gpu=System.Object[]; python_process_count=0; python_processes=; top_processes=System.Object[]}.free_memory_mb) MB
- Python process count: $(@{collected_at_utc=03/19/2026 00:10:03; logical_cpu=8; total_cpu_percent=17; free_memory_mb=15563; gpu=System.Object[]; python_process_count=0; python_processes=; top_processes=System.Object[]}.python_process_count)
- GPU utilization: $(@{collected_at_utc=03/19/2026 00:10:03; logical_cpu=8; total_cpu_percent=17; free_memory_mb=15563; gpu=System.Object[]; python_process_count=0; python_processes=; top_processes=System.Object[]}.gpu[0].utilization_gpu)

## Launch State
- Started workers: $(@(   ).Count)
- Total runs planned: $(@{collected_at_utc=03/19/2026 00:12:48; out_root=D:\projects\Bio_Digital_Core\Bio_digital_core\results\selection_physics_reboot_r1_full; total_runs=180; completed_runs=0; active_run_slots=4; percent_complete=0; eta_hours=; eta_hint=waiting_for_first_completed_run; expected_total_runtime_hours_on_this_host_approx=4-6; workers=System.Object[]}.total_runs)
- Completed runs currently visible: $(@{collected_at_utc=03/19/2026 00:12:48; out_root=D:\projects\Bio_Digital_Core\Bio_digital_core\results\selection_physics_reboot_r1_full; total_runs=180; completed_runs=0; active_run_slots=4; percent_complete=0; eta_hours=; eta_hint=waiting_for_first_completed_run; expected_total_runtime_hours_on_this_host_approx=4-6; workers=System.Object[]}.completed_runs)
- Percent complete: $(@{collected_at_utc=03/19/2026 00:12:48; out_root=D:\projects\Bio_Digital_Core\Bio_digital_core\results\selection_physics_reboot_r1_full; total_runs=180; completed_runs=0; active_run_slots=4; percent_complete=0; eta_hours=; eta_hint=waiting_for_first_completed_run; expected_total_runtime_hours_on_this_host_approx=4-6; workers=System.Object[]}.percent_complete)%
- ETA hours: $(@{collected_at_utc=03/19/2026 00:12:48; out_root=D:\projects\Bio_Digital_Core\Bio_digital_core\results\selection_physics_reboot_r1_full; total_runs=180; completed_runs=0; active_run_slots=4; percent_complete=0; eta_hours=; eta_hint=waiting_for_first_completed_run; expected_total_runtime_hours_on_this_host_approx=4-6; workers=System.Object[]}.eta_hours)
- ETA hint: $(@{collected_at_utc=03/19/2026 00:12:48; out_root=D:\projects\Bio_Digital_Core\Bio_digital_core\results\selection_physics_reboot_r1_full; total_runs=180; completed_runs=0; active_run_slots=4; percent_complete=0; eta_hours=; eta_hint=waiting_for_first_completed_run; expected_total_runtime_hours_on_this_host_approx=4-6; workers=System.Object[]}.eta_hint)

## Worker State
- worker 01: pid=71032, running=True, expected_runs=60, completed_runs=0, active_run_slots=1
- worker 02: pid=85452, running=True, expected_runs=60, completed_runs=0, active_run_slots=1
- worker 03: pid=166584, running=True, expected_runs=30, completed_runs=0, active_run_slots=1
- worker 04: pid=139100, running=True, expected_runs=30, completed_runs=0, active_run_slots=1

## Monitoring Command
- powershell -ExecutionPolicy Bypass -File scripts/edp1/monitor_selection_physics_reboot_progress.ps1

## Interpretation
- Cleanup materially improved launch conditions by removing Python noise, Node dev servers, Docker backend, and WSL service noise.
- The canonical R1 long run is now started and should be monitored through progress_status.json.
- A scientific verdict is still not available until the full sweep completes and the aggregate gate audit is rerun on the complete output root.
