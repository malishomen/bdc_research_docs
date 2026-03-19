# R3 Sequence-Memory Mechanism Spec

## Status
- Date: 2026-03-19
- Task: `TASK-7609`
- Change class: `R1`
- Environment: `controlled_sequence_memory`

## Purpose

This document defines the first bounded mechanism candidate inside the approved `R2` environment.

The goal is not to prove general memory.
The goal is to define one explicit replayable mechanism that can be measured against non-mechanistic and trivial-memory controls.

## Mechanism candidate

### Candidate ID
- `bounded_working_memory_candidate`

### Mechanism type
- bounded FIFO working-memory trace

### Rationale
- it isolates memory as the active mechanism,
- it is deterministic,
- it is replayable step by step,
- and it does not require a second mechanism layer.

## State contract

### State fields
1. `trace_width`
- fixed positive integer
- canonical default for this cycle: `5`

2. `trace`
- ordered tuple of the most recent observed symbols
- maximum length equals `trace_width`

3. `steps_seen`
- integer count of processed symbols

### Initialization
- `trace = ()`
- `steps_seen = 0`
- `trace_width = 5`

## Update rule

For each observed symbol `s` in sequence order:
1. increment `steps_seen`
2. append `s` to the right side of `trace`
3. if `len(trace)` exceeds `trace_width`, drop the oldest symbol from the left

This produces a deterministic FIFO replay surface.

## Prediction rule

At query time, given `recall_gap`:
1. compute `required_depth = recall_gap + 1`
2. if `required_depth > len(trace)`, prediction is invalid and the mechanism fails replay coverage
3. otherwise predict the symbol at index `-required_depth` from the trace

Interpretation:
- the mechanism predicts the symbol that occurred `recall_gap` positions before the final sequence position
- the mechanism does so only through the bounded replayable trace

## Control definitions

### `no_memory_control`
- operationalized as `majority_symbol_predictor`
- justification:
  - it uses no replayable internal state,
  - it is a strong non-mechanistic heuristic,
  - it remains the most demanding baseline from the approved `R2` environment

### `trivial_last_symbol_memory`
- operationalized as `always_repeat_last_symbol`
- justification:
  - it uses only the most recent symbol,
  - it is replayable,
  - but it does not solve the bounded recall requirement honestly

### `bounded_working_memory_candidate`
- the explicit FIFO trace defined above

## Required measured outputs

The implementation step must emit at minimum:
- `candidate_accuracy`
- `no_memory_control_accuracy`
- `trivial_last_symbol_memory_accuracy`
- `delta_vs_no_memory`
- `delta_vs_trivial_memory`
- `gap_accuracy_by_recall_gap`
- `deterministic_replay_status`
- `replay_examples`

## Mechanism gate rule

The measured gate may emit only:
- `APPROVE_MECHANISM_CONTINUATION`
- `REMAIN_IN_MECHANISM_PHASE`

### Approval conditions
1. deterministic replay passes
2. candidate accuracy is strictly greater than `no_memory_control_accuracy`
3. candidate accuracy is strictly greater than `trivial_last_symbol_memory_accuracy`
4. candidate remains above both controls on the hardest observed recall gap slice
5. no hidden second mechanism is introduced

### Remain-in-phase conditions
- any approval condition fails
- replay is not deterministic
- performance gain exists only on easy gaps
- or implementation drifts beyond the single bounded trace mechanism

## Explicit exclusions
- no uncertainty gating
- no multi-buffer design
- no communication channel
- no learned weights or adaptive training loop
- no organism or cell rhetoric

## Expected next step
- `TASK-7610` must implement this exact contract, not a broader mechanism family.
