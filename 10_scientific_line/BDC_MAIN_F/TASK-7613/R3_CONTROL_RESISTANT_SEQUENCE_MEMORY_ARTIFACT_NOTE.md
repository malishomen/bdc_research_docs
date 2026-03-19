# R3 Control-Resistant Sequence-Memory Artifact Note

## Status
- Date: 2026-03-19
- Task: `TASK-7613`
- Environment family: `controlled_sequence_memory`

## Artifact conditions
- `target_symbol != last_symbol`
- `target_symbol != majority_symbol`
- deterministic generation preserved
- replay rule unchanged

## Measured result
From `results/r3_control_resistant_sequence_memory/mechanism_scorecard.json`:
- `candidate_accuracy = 1.0`
- `no_memory_control_accuracy = 0.0`
- `trivial_last_symbol_memory_accuracy = 0.0`
- `delta_vs_no_memory = 1.0`
- `delta_vs_trivial_memory = 1.0`
- `hardest_recall_gap = 6`
- `hardest_gap candidate_accuracy = 1.0`
- `hardest_gap no_memory_control_accuracy = 0.0`
- `hardest_gap trivial_last_symbol_memory_accuracy = 0.0`
- `deterministic_replay_status = true`

## Interpretation
- the same bounded FIFO memory mechanism survives a stricter control-resistant slice,
- shortcut-friendly alignment has been removed successfully,
- measured superiority remains present on the hardest gap slice.

## Constraint
- This is still one bounded continuation artifact, not a multi-mechanism claim.
