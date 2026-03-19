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
- `R3` first mechanism gate is complete.
- Canonical `R3` verdict:
  - `APPROVE_MECHANISM_CONTINUATION`
- Approved bounded mechanism:
  - `bounded_working_memory_candidate`
- Canonical gate artifact:
  - `results/r3_sequence_memory_mechanism/mechanism_gate_decision.json`
- `R3` second bounded signal is now confirmed.
- Canonical continuation verdict:
  - `CONFIRM_SECOND_BOUNDED_SIGNAL`
- Continuation gate artifact:
  - `results/r3_control_resistant_sequence_memory/second_bounded_signal_decision.json`
- Post-second-signal decision gate is complete.
- Canonical decision verdict:
  - `OPEN_SINGLE_MECHANISM_GENERALIZATION_GATE`
- Decision artifact:
  - `docs/experiments/POST_SECOND_SIGNAL_GATE_DECISION.md`

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
  - `R4 - Single-Mechanism Generalization Gate`
- Canonical R3 docs:
  - `docs/experiments/EXP-0804_R3_SEQUENCE_MEMORY_MECHANISM_VALIDATION.md`
  - `docs/experiments/BDC_R3_SEQUENCE_MEMORY_MECHANISM_PREEXPERIMENT_GATE.md`
  - `docs/experiments/EXP-0805_R3_SEQUENCE_MEMORY_MECHANISM_IMPLEMENTATION_PACKAGE.md`
  - `docs/experiments/R3_SEQUENCE_MEMORY_MECHANISM_GATE_DECISION.md`
  - `docs/experiments/R3_SECOND_BOUNDED_SIGNAL_GATE_DECISION.md`
  - `docs/experiments/POST_SECOND_SIGNAL_GATE_DECISION.md`
- Canonical R4 docs:
  - `docs/experiments/EXP-0810_R4_SINGLE_MECHANISM_GENERALIZATION.md`
  - `docs/experiments/BDC_R4_SINGLE_MECHANISM_GENERALIZATION_PREEXPERIMENT_GATE.md`
  - `docs/experiments/EXP-0811_R4_SINGLE_MECHANISM_GENERALIZATION_IMPLEMENTATION_PACKAGE.md`

## Current Task Chain
- `TASK-7608` - R3 mechanism package
- `TASK-7609` - memory mechanism spec
- `TASK-7610` - bounded memory mechanism implementation
- `TASK-7611` - measured mechanism gate audit
- `TASK-7612` - control-resistant continuation package
- `TASK-7613` - control-resistant artifact
- `TASK-7614` - second bounded signal gate
- `TASK-7615` - post-second-signal decision package
- `TASK-7616` - post-second-signal decision gate
- `TASK-7617` - single-mechanism generalization package
- `TASK-7618` - generalization pressure matrix
- `TASK-7619` - generalization implementation and measurement
- `TASK-7620` - generalization gate audit

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
2. treat `bounded_working_memory_candidate` as a mechanism with two bounded positive signals inside the same environment family,
3. treat `single_mechanism_generalization` as the selected and already opened next bounded gate,
4. treat `docs/experiments/R4_SINGLE_MECHANISM_GENERALIZATION_PRESSURE_MATRIX.md` as the canonical bounded `R4` pressure surface,
5. treat `docs/experiments/R4_SINGLE_MECHANISM_GENERALIZATION_MEASUREMENT_NOTE.md` as the measured `R4` implementation result,
6. execute `TASK-7620` next,
7. do not open micro-assembly until it gets its own explicit bounded evidence gate.
