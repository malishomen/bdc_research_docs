# R5 Transfer Longrun Execution Runbook

## Scope
- Prepare the operational layer for the canonical `R5` transfer run.
- Do not reopen scientific scope.
- Do not start the canonical run inside this document.

## Current Canonical State
- Scientific status:
  - `READY_FOR_R5_TRANSFER_LONGRUN`
- Approved target:
  - `symbolic_micro_corpus_cloze_transfer`
- Approved mechanism family:
  - `bounded_working_memory_candidate`

## Runtime Posture
- execution mode:
  - `deterministic_cpu`
- preferred device:
  - `cpu`
- reason:
  - the run evaluates a fixed FIFO mechanism across deterministic transfer slices;
  - there is no GPU-native training loop here.

## Longrun Surface
- seeds:
  - `30`
- slices:
  - `4`
- total runs:
  - `120`

Slice set:
1. `base_cloze_transfer`
2. `gap_extension_cloze_transfer`
3. `lexicon_extension_cloze_transfer`
4. `combined_bounded_cloze_transfer`

## Measured Runtime Expectation
Measured reduced benchmark:
- `2` runs completed in `0.453s`
- projected full runtime at the same rate:
  - `27.18s`

Operational interpretation:
- this is not an `R1`-class multi-hour run;
- no aggressive host cleanup or parallel worker split is required;
- practical operator budget should still allow `1-2` minutes end-to-end for process startup, IO, and verification.

## Canonical Launch Command
```powershell
python scripts/analysis/run_phase68_r5_transfer_launch_prep.py --stage longrun --manifest_path scripts/analysis/r5_cloze_transfer_longrun_manifest.json --longrun_out results/r5_cloze_transfer_longrun --progress_path results/r5_cloze_transfer_longrun/progress_status.json
```

## Launcher Preview Command
```powershell
powershell -ExecutionPolicy Bypass -File scripts/analysis/launch_r5_transfer_longrun.ps1 -ManifestPath scripts/analysis/r5_cloze_transfer_longrun_manifest.json -OutRoot results/r5_cloze_transfer_longrun -LaunchInfoJson results/r5_cloze_transfer_longrun/launch_info.json
```

## Launcher Execute Command
```powershell
powershell -ExecutionPolicy Bypass -File scripts/analysis/launch_r5_transfer_longrun.ps1 -Execute -ManifestPath scripts/analysis/r5_cloze_transfer_longrun_manifest.json -OutRoot results/r5_cloze_transfer_longrun -LaunchInfoJson results/r5_cloze_transfer_longrun/launch_info.json
```

## Live Status Command
```powershell
powershell -ExecutionPolicy Bypass -File scripts/analysis/monitor_r5_transfer_longrun_progress.ps1 -OutRoot results/r5_cloze_transfer_longrun -LaunchInfoJson results/r5_cloze_transfer_longrun/launch_info.json -OutJson results/r5_cloze_transfer_longrun/progress_status_view.json
```

## Expected Output Surface
Required root:
- `results/r5_cloze_transfer_longrun`

Required files after completion:
- `progress_status.json`
- `longrun_summary.json`
- `longrun_summary.csv`
- per-run `manifest.json`
- per-run `scorecard.json`
- per-run `dataset_preview.json`

## Host Snapshot
Current measured host snapshot reference:
- `reports/analysis/TASK-7627-BDC-R5-TRANSFER-LONGRUN-EXECUTION-SUPPORT/r5_host_snapshot.json`

Operational reading:
- current host has enough free RAM for this run;
- CPU load is low enough that the run can be executed without dedicated cleanup;
- GPU presence is irrelevant for this specific phase.

## Mandatory Preflight
- before launch, run:
  - `python scripts/analysis/verify_bdc_state_hierarchy.py`
- required result:
  - `status = PASS`
- if this check fails:
  - do not launch the long-run,
  - resolve hierarchy drift first.

## Preflight Meaning
- confirms that `CANON.md`, `bdc_real_statemant.md`, `memory.md`, and the `R5` execution packet still agree on:
  - the current active phase,
  - the current authorized next action,
  - the current scope limits.

## Constraint Carried Forward
The run must:
- keep the same FIFO mechanism family unchanged;
- keep the approved deterministic cloze transfer surface unchanged;
- not reuse the historical cloze evolutionary stack as proof of transfer;
- not widen scope to multi-mechanism, organism, or cell claims.
