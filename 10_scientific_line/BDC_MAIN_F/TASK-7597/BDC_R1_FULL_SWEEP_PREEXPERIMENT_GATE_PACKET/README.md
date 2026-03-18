# BDC R1 Full Sweep Pre-Experiment Gate Packet

This folder is a synthetic BDC-facing packet for the scientific `R1` pre-experiment gate.

It exists for one narrow purpose:
- verify that a bounded scientific gate packet can be normalized and accepted by the current `BDC Designer` generic folder-intake contract.

It does **not** represent a client packet.
It does **not** convert the scientific reboot line into a client workflow.
It does **not** claim that `R1` has already passed.

## Packet intent
- bind `Phase R1` to a narrow `PASS_TO_R2` vs `REMAIN_IN_R1` decision gate,
- capture the current measured vs missing evidence state,
- attach a fresh smoke-run artifact set as a preservation and intake-validation check,
- test whether `BDC Designer` can ingest the packet cleanly.

## Attached evidence
- `BDC_INPUT_PACKET_R1_FULL_SWEEP_PREEXPERIMENT_GATE.json`
- `unified_variant_comparison.csv`
- `current_runtime_role_mapping.csv`
- `current_slice_metrics.csv`
- `failure_case_registry.csv`
- `prompt_stage_matrix.csv`
- `lead_architect_design_priorities.md`

## Fresh smoke-run root
- `results/selection_physics_reboot_r1_gate_smoke_2026-03-19`

## Rules
- The smoke run is tooling-only evidence.
- The full canonical long run remains required for the actual `R1` scientific gate.
