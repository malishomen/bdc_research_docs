# Project Memory

## Repository
- Path: `D:\projects\Bio_Digital_Core\Bio_digital_core`
- Main working branch: `test`
- Research mirror repo: `D:\projects\Bio_Digital_Core\bdc_research_docs`
- Primary live-state reference: `bdc_real_statemant.md`
- Hierarchy/governance reference: `docs/project/BDC_SOURCE_OF_TRUTH_AND_EXECUTION_HIERARCHY.md`

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
- `R4` single-mechanism generalization gate is now complete.
- Canonical `R4` verdict:
  - `CONFIRM_SINGLE_MECHANISM_GENERALIZATION`
- Canonical gate artifact:
  - `results/r4_single_mechanism_generalization/generalization_gate_decision.json`
- Secondary analytical `BDC Designer` packet verdict:
  - `supported = true`
  - `recommended_variant_id = bounded_working_memory_candidate`
- Post-`R4` decision gate is now complete.
- Canonical decision verdict:
  - `OPEN_SINGLE_MECHANISM_TRANSFER_GATE`
- Decision artifact:
  - `docs/experiments/BDC_POST_R4_DECISION_PACKET/post_r4_gate_decision.json`
- Secondary analytical `BDC Designer` packet verdict:
  - `supported = true`
  - `recommended_variant_id = single_mechanism_transfer_gate`
- `R5` transfer target decision gate is now complete.
- Canonical `R5` verdict:
  - `APPROVE_R5_TRANSFER_TARGET`
- Approved transfer target:
  - `symbolic_micro_corpus_cloze_transfer`
- Canonical gate artifact:
  - `docs/experiments/BDC_R5_TRANSFER_TARGET_PACKET/r5_transfer_target_decision.json`
- `R5` launch prep is now complete.
- Canonical launch-prep verdict:
  - `READY_FOR_R5_TRANSFER_LONGRUN`
- Launch-prep artifact:
  - `docs/experiments/BDC_R5_TRANSFER_LAUNCH_PREP_PACKET/r5_transfer_launch_prep_decision.json`
- `R5` measured transfer gate is now complete.
- Canonical `R5` verdict:
  - `CONFIRM_SINGLE_MECHANISM_TRANSFER_SIGNAL`
- Canonical gate artifact:
  - `results/r5_cloze_transfer_longrun/r5_transfer_measured_gate_decision.json`

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
  - `Post-R5 Bounded Decision Gate`
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
  - `docs/experiments/R4_SINGLE_MECHANISM_GENERALIZATION_GATE_DECISION.md`
  - `docs/experiments/POST_R4_GATE_DECISION.md`

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
- `TASK-7621` - post-R4 decision package
- `TASK-7622` - post-R4 decision gate
- `TASK-7623` - R5 single-mechanism transfer package
- `TASK-7624` - R5 transfer target matrix
- `TASK-7625` - R5 transfer target decision gate
- `TASK-7626` - R5 transfer long-run launch prep
- `TASK-7627` - R5 transfer long-run execution support
- `TASK-7628` - R5 transfer execution readiness gate

## Current R5 Transfer State
- `R5` transfer target is now approved.
- Approved target:
  - `symbolic_micro_corpus_cloze_transfer`
- Deferred target:
  - `controlled_uncertainty_abstention_transfer`
- Reason:
  - still documentation-only, so it is not honest for immediate long-run preparation.
- Launch-ready status:
  - `READY_FOR_R5_TRANSFER_LONGRUN`
- Operational execution support:
  - launcher preview exists,
  - incremental progress + ETA monitor exists,
  - host snapshot is captured,
  - projected full runtime is about `27.18s` on the current host.
- Execution-ready status:
  - `READY_TO_EXECUTE_R5_LONGRUN`
- Measured long-run status:
  - `120 / 120` completed runs
- Measured transfer verdict:
  - `CONFIRM_SINGLE_MECHANISM_TRANSFER_SIGNAL`
- Measured transfer reading:
  - candidate mean accuracy remained `1.0` on the full bounded transfer surface,
  - deterministic replay remained true,
  - the same FIFO mechanism remained above all three controls.

## BDC Designer Rule
- For scientific reboot work, `BDC Designer` must be used first as pre-experiment narrowing/evidence discipline.
- Direct experiment execution comes after that gate, not before.

## Current Product Hardening State
- Active product execution focus:
  - post-Cockpit `BDC Designer` hardening
- Canonical product hardening reference:
  - `docs/project/BDC_DESIGNER_POST_COCKPIT_HARDENING_PLAN.md`
- Active task chain:
  - `TASK-7640`
  - `TASK-7641`
  - `TASK-7642`
  - `TASK-7643`
  - `TASK-7644`
  - `TASK-7645`
- Hardening target:
  - keep native intake working on external packets
  - eliminate non-deployable winners
  - eliminate cross-domain fallback contamination
  - separate intake success from recommendation trust
- Hardening outcome:
  - `PASS_EXTERNAL_RERUN_GATE`
- Product next honest step:
  - open a bounded Cockpit session-continuity hardening cycle

## Research Mirrors
- Temp mirror:
  - `D:\projects\Bio_Digital_Core\Temp\research\BDC_MAIN_F`
- Designer mirror:
  - `D:\projects\Bio_Digital_Core\Temp\research\BDC_Designer_F`
- Research docs repo:
  - `D:\projects\Bio_Digital_Core\bdc_research_docs`

## Current Stop Point
If a new session starts, the correct next action is:
1. read `bdc_real_statemant.md` first as the canonical live-state summary,
2. read `docs/project/BDC_SOURCE_OF_TRUTH_AND_EXECUTION_HIERARCHY.md` as the conflict-resolution and execution-discipline rule,
3. run `python scripts/analysis/verify_bdc_state_hierarchy.py` before major execution,
4. treat `controlled_sequence_memory` as the approved canonical bounded `R2` environment,
5. treat `bounded_working_memory_candidate` as a mechanism with two bounded positive signals inside the same environment family,
6. treat `CONFIRM_SINGLE_MECHANISM_TRANSFER_SIGNAL` as the current canonical scientific truth,
7. treat `BDC Designer` as a secondary confirming layer, not a replacement for the scientific gate,
8. treat `docs/experiments/EXP-0814_R5_SINGLE_MECHANISM_TRANSFER.md` as the active bounded `R5` package that produced the measured result,
9. treat `symbolic_micro_corpus_cloze_transfer` as the approved `R5` transfer target,
10. treat `docs/experiments/R5_TRANSFER_LONGRUN_EXECUTION_RUNBOOK.md` as the canonical operator reference that governed launch and monitoring,
11. treat `docs/experiments/R5_TRANSFER_EXECUTION_GATE_DECISION.md` as the canonical pre-run execution gate outcome,
12. treat `docs/experiments/R5_TRANSFER_MEASURED_GATE_DECISION.md` as the canonical measured-transfer reference,
13. the next honest step is now a bounded post-`R5` decision gate,
14. in parallel, the active product execution focus is now the bounded post-Cockpit `BDC Designer` hardening chain,
15. treat `PASS_EXTERNAL_RERUN_GATE` as the current product truth for `BDC Designer`,
16. the next honest product step is a bounded Cockpit session-continuity hardening cycle,
17. do not let product hardening overwrite canonical scientific truth,
18. do not open organism or cell claims,
19. do not open micro-assembly until it gets its own explicit bounded evidence gate.
