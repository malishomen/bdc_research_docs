# TASK-7598 BRIEF REPORT

## Scope
- Declare the current R1 gate memo as the formal pre-run document for the canonical long run.
- Capture a fresh host snapshot.
- Add a cleanup script that targets non-essential interference processes while preserving Codex.

## Changes
- Created docs/experiments/BDC_R1_CANONICAL_LAUNCH_PREP.md.
- Created scripts/edp1/cleanup_selection_physics_host.ps1.
- Captured eports/analysis/TASK-7598-BDC-R1-CANONICAL-LAUNCH-PREP-AND-CLEANUP/host_snapshot_2026-03-19.json.
- Captured eports/analysis/TASK-7598-BDC-R1-CANONICAL-LAUNCH-PREP-AND-CLEANUP/cleanup_preview_2026-03-19.json.
- Created eports/analysis/TASK-7598-BDC-R1-CANONICAL-LAUNCH-PREP-AND-CLEANUP/PROCESS_SNAPSHOT_2026-03-19.md.

## Verification (L0)
- Command: powershell -ExecutionPolicy Bypass -File scripts/edp1/capture_selection_physics_host_snapshot.ps1 -OutJson reports/analysis/TASK-7598-BDC-R1-CANONICAL-LAUNCH-PREP-AND-CLEANUP/host_snapshot_2026-03-19.json
- Result: PASS
- Output summary: logical_cpu=8, ree_memory_mb=7509, python_process_count=8.

- Command: powershell -ExecutionPolicy Bypass -File scripts/edp1/cleanup_selection_physics_host.ps1
- Result: PASS
- Output summary: preview-only run completed and wrote the default preview file.

- Command: powershell -ExecutionPolicy Bypass -File scripts/edp1/cleanup_selection_physics_host.ps1 -Execute:$false -OutJson reports/analysis/TASK-7598-BDC-R1-CANONICAL-LAUNCH-PREP-AND-CLEANUP/cleanup_preview_2026-03-19.json
- Result: PASS
- Output summary: codex_protected=true, 	arget_count=32, 	erminated_count=0.

## Artifacts
- docs/experiments/BDC_R1_CANONICAL_LAUNCH_PREP.md - launch-prep note that binds the existing gate memo as the formal pre-run document.
- scripts/edp1/cleanup_selection_physics_host.ps1 - safe cleanup tool with preview-by-default behavior.
- eports/analysis/TASK-7598-BDC-R1-CANONICAL-LAUNCH-PREP-AND-CLEANUP/host_snapshot_2026-03-19.json - fresh machine snapshot.
- eports/analysis/TASK-7598-BDC-R1-CANONICAL-LAUNCH-PREP-AND-CLEANUP/cleanup_preview_2026-03-19.json - machine-readable preview of termination targets.
- eports/analysis/TASK-7598-BDC-R1-CANONICAL-LAUNCH-PREP-AND-CLEANUP/PROCESS_SNAPSHOT_2026-03-19.md - readable launch-impact summary.

## Risks / Limitations
- The cleanup script targets only known interference families and is intentionally conservative around Codex, but it still operates at the process level and should be run only immediately before the long run.
- wslservice.exe and mmemWSL are included as optional targets because they materially affect the host, but they may respawn depending on host configuration.
- This task did not terminate any processes.

## Rollback
- Revert with git revert <task-commit-hash> after identifying the final commit for TASK-7598.
