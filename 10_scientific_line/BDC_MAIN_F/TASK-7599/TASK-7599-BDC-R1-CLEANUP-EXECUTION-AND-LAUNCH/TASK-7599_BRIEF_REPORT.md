# TASK-7599 BRIEF REPORT

## Scope
- Execute the prepared host cleanup in real mode.
- Capture a post-cleanup host snapshot.
- Launch the canonical R1 long run.
- Add progress monitoring that exposes percent completion and approximate ETA once completed runs appear.

## Changes
- Updated scripts/edp1/cleanup_selection_physics_host.ps1 to use a switch-based execute flag.
- Updated scripts/edp1/run_selection_physics_reboot_parallel.ps1 to write JSON without BOM so worker manifests are readable by the runner.
- Added scripts/edp1/monitor_selection_physics_reboot_progress.ps1.
- Captured execution artifacts for cleanup and post-cleanup state.
- Started the canonical R1 long run and wrote esults/selection_physics_reboot_r1_full/parallel_launch/started_processes.json.

## Verification (L0)
- Command: powershell -ExecutionPolicy Bypass -File scripts/edp1/cleanup_selection_physics_host.ps1 -Execute -OutJson reports/analysis/TASK-7599-BDC-R1-CLEANUP-EXECUTION-AND-LAUNCH/cleanup_execute_2026-03-19.json
- Result: PASS
- Output summary: 	arget_count=7, 	erminated_successfully=6, 	ermination_failures=1.

- Command: powershell -ExecutionPolicy Bypass -File scripts/edp1/capture_selection_physics_host_snapshot.ps1 -OutJson reports/analysis/TASK-7599-BDC-R1-CLEANUP-EXECUTION-AND-LAUNCH/host_snapshot_post_cleanup_2026-03-19.json
- Result: PASS
- Output summary: ree_memory_mb=15563, python_process_count=0 immediately after cleanup snapshot.

- Command: powershell -ExecutionPolicy Bypass -File scripts/edp1/run_selection_physics_reboot_parallel.ps1 -Execute
- Result: PASS
- Output summary: started 4 worker launcher processes and wrote started_processes.json.

- Command: powershell -ExecutionPolicy Bypass -File scripts/edp1/monitor_selection_physics_reboot_progress.ps1
- Result: PASS
- Output summary: 	otal_runs=180, completed_runs=0, ctive_run_slots=4, percent_complete=0, ta_hint=waiting_for_first_completed_run; expected_total_runtime_hours_on_this_host_approx=4-6.

## Artifacts
- scripts/edp1/cleanup_selection_physics_host.ps1 - execute-capable cleanup script with Codex protection.
- scripts/edp1/run_selection_physics_reboot_parallel.ps1 - corrected BOM-safe parallel launcher.
- scripts/edp1/monitor_selection_physics_reboot_progress.ps1 - progress and ETA monitor.
- eports/analysis/TASK-7599-BDC-R1-CLEANUP-EXECUTION-AND-LAUNCH/cleanup_execute_2026-03-19.json - cleanup execution record.
- eports/analysis/TASK-7599-BDC-R1-CLEANUP-EXECUTION-AND-LAUNCH/host_snapshot_post_cleanup_2026-03-19.json - post-cleanup host snapshot.
- eports/analysis/TASK-7599-BDC-R1-CLEANUP-EXECUTION-AND-LAUNCH/PROCESS_STATE_POST_CLEANUP_2026-03-19.md - readable launch-state summary.
- esults/selection_physics_reboot_r1_full/parallel_launch/started_processes.json - active long-run worker registry.
- esults/selection_physics_reboot_r1_full/parallel_launch/progress_status.json - progress snapshot with percent completion / ETA fields.

## Risks / Limitations
- mmemWSL survived cleanup because the process could not be terminated under current permissions.
- The progress monitor cannot produce a numeric ETA until at least one run completes and emits a summary.json.
- The long run is started, not finished. No scientific verdict should be inferred from launch state.

## Rollback
- Revert repository changes with git revert <task-commit-hash> after identifying the final commit for TASK-7599.
- Long-run worker processes can be stopped manually by PID using started_processes.json if needed.
