# BDC R1 Canonical Launch Prep

## Status
- Date: `2026-03-19`
- Status: `PRE-RUN READY NOTE`
- Scope: `launch preparation only`

## Formal Pre-Run Document
The formal pre-run document for the canonical `R1` long run is:

- `docs/experiments/BDC_R1_FULL_SWEEP_PREEXPERIMENT_GATE.md`

This note does not replace that document.

It makes the launch interpretation explicit:
- the gate memo defines the scientific question,
- the gate memo defines the only allowed `R1` verdict contract,
- the full canonical long run is now the only valid next execution step,
- and no additional package design is required before launch.

## Canonical Execution Surface
- Manifest:
  - `scripts/edp1/selection_physics_manifest.json`
- Runner:
  - `scripts/edp1/run_selection_physics_reboot_sweep.py`
- Aggregator:
  - `scripts/edp1/aggregate_selection_physics_reboot.py`
- Parallel launch helper:
  - `scripts/edp1/run_selection_physics_reboot_parallel.ps1`
- Host snapshot:
  - `scripts/edp1/capture_selection_physics_host_snapshot.ps1`
- Cleanup preview:
  - `scripts/edp1/cleanup_selection_physics_host.ps1`

## What This Prep Authorizes
- capture a fresh host snapshot,
- preview a cleanup plan for non-essential interference processes,
- and launch the full canonical `R1` sweep when the host is sufficiently clean.

## What This Prep Does Not Authorize
- changing the manifest,
- changing regime families,
- changing seeds,
- changing the gate contract,
- or interpreting smoke evidence as the full `R1` result.

## Launch Readiness Criteria
- host snapshot captured fresh,
- cleanup preview available,
- `Codex IDE` explicitly excluded from termination targets,
- runner / aggregator paths unchanged,
- output root chosen in advance,
- decision contract remains `PASS_TO_R2` vs `REMAIN_IN_R1`.

## Integrity Rule
If cleanup is required, it must be operational only.

It may reduce:
- duplicate Python jobs,
- dev servers,
- extra AI desktop clients,
- Docker / WSL interference when not needed,
- auxiliary editor instances.

It may not:
- terminate Codex,
- terminate critical system services,
- alter the scientific protocol.
