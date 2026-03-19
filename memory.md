# Project Memory

## Repository
- Path: `D:\projects\Bio_Digital_Core\Bio_digital_core`
- Main working branch: `test`
- Research mirror repo: `D:\projects\Bio_Digital_Core\bdc_research_docs`

## Current Scientific State
- `R1` selection-physics reboot is complete.
- Canonical scientific verdict:
  - `PASS_TO_R2`
- Canonical gate artifact:
  - `results/selection_physics_reboot_r1_full/aggregates/r1_gate_decision.json`
- Full-run summary:
  - `180 / 180` runs passed across 6 required regimes.
- `R2` environment selection is complete.
- Canonical `R2` verdict:
  - `APPROVE_R2_ENVIRONMENT`
- Approved environment:
  - `controlled_sequence_memory`
- Canonical gate artifact:
  - `docs/experiments/BDC_R2_CONTROLLED_TASK_ENVIRONMENT_REFRESH_PACKET/r2_refresh_gate_decision.json`

## Current Analytical State
- Full `R1` packet was run through `BDC Designer`.
- Packet was accepted as `supported`.
- `BDC Designer` winner prior for the full packet:
  - `no_penalty_diagnostic`
- This is a secondary analytical result, not a replacement for the canonical scientific gate.

## Interpretation Rule
- Canonical scientific truth:
  - `R1 = PASS_TO_R2`
- `BDC Designer` truth:
  - secondary narrowing layer only
- Do not let `BDC Designer` replace the scientific gate.

## Current Next Phase
- Active scientific target:
  - `R3 - Sequence-Memory Mechanism Validation`
- Canonical R3 docs:
  - `docs/experiments/EXP-0804_R3_SEQUENCE_MEMORY_MECHANISM_VALIDATION.md`
  - `docs/experiments/BDC_R3_SEQUENCE_MEMORY_MECHANISM_PREEXPERIMENT_GATE.md`
  - `docs/experiments/EXP-0805_R3_SEQUENCE_MEMORY_MECHANISM_IMPLEMENTATION_PACKAGE.md`

## Current Task Chain
- `TASK-7608` - R3 mechanism package
- `TASK-7609` - memory mechanism spec
- `TASK-7610` - bounded memory mechanism implementation
- `TASK-7611` - measured mechanism gate audit

## BDC Designer Rule
- For scientific reboot work, `BDC Designer` must be used first as pre-experiment narrowing/evidence discipline.
- Direct experiment execution comes after that gate, not before.

## Research Mirrors
- Temp mirror:
  - `D:\projects\Bio_Digital_Core\Temp\research\BDC_MAIN_F`
- Designer mirror:
  - `D:\projects\Bio_Digital_Core\Temp\research\BDC_Designer_F`
- Research docs repo:
  - `D:\projects\Bio_Digital_Core\bdc_research_docs`

## Current Stop Point
If a new session starts, the correct next action is:
1. treat `controlled_sequence_memory` as the approved canonical bounded `R2` environment,
2. stay inside the first bounded `R3` mechanism-level cycle,
3. execute `TASK-7609` next,
4. compare only `no_memory_control`, `trivial_last_symbol_memory`, and `bounded_working_memory_candidate`,
5. do not widen to organism/cell claims.
