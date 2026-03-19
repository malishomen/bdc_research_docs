# R4 Single-Mechanism Generalization Pressure Matrix

## Status
- Date: 2026-03-19
- Task: `TASK-7618`
- Change class: `R1`
- Phase: `R4 - Single-Mechanism Generalization`

## Purpose

This document defines the bounded deterministic pressure surface for `R4`.

It does not measure generalization yet.
It defines the exact slices that `TASK-7619` must implement and that `TASK-7620` must audit.

## Mechanism identity invariants

The following are fixed and may not change across slices:

1. candidate id remains `bounded_working_memory_candidate`
2. mechanism type remains a single bounded FIFO working-memory trace
3. update rule remains append-right / evict-left when width is exceeded
4. prediction rule remains replay-only lookup at depth `recall_gap + 1`
5. no second state channel, adaptive learning, training loop, or multi-buffer design is allowed

## Allowed parameter scaling

`trace_width` may scale only as the minimum replay width required by the slice:

- canonical rule:
  - `trace_width = max_gap + 1`

This preserves the same mechanism identity while preventing hidden widening beyond the pressure being tested.

## Required controls

The same controls remain active on every slice:

1. `majority_symbol_predictor`
   - treated as `no_memory_control`
2. `always_repeat_last_symbol`
   - treated as `trivial_last_symbol_memory`

## Reference measured slices

These are already measured and anchor the R4 matrix:

### 1. `r3_reference_narrow`
- source: `TASK-7610`
- `seq_len = 8`
- `alphabet_size = 4`
- `min_gap = 2`
- `max_gap = 4`
- `trace_width = 5`
- `control_resistant = false`

### 2. `r3_reference_control_resistant`
- source: `TASK-7613`
- `seq_len = 10`
- `alphabet_size = 5`
- `min_gap = 3`
- `max_gap = 6`
- `trace_width = 7`
- `control_resistant = true`
- required constraints:
  - `target_symbol != last_symbol`
  - `target_symbol != majority_symbol`

## Required R4 pressure slices

### 1. `r4_length_extension`
- purpose:
  - test whether the same mechanism survives longer irrelevant context
- pressure axis:
  - longer sequence length
- parameters:
  - `seed = 20260320`
  - `dataset_size = 192`
  - `seq_len = 14`
  - `alphabet_size = 5`
  - `min_gap = 3`
  - `max_gap = 6`
  - `trace_width = 7`
  - `control_resistant = true`

### 2. `r4_gap_extension`
- purpose:
  - test whether the same mechanism survives deeper recall demand
- pressure axis:
  - larger recall gap
- parameters:
  - `seed = 20260321`
  - `dataset_size = 192`
  - `seq_len = 12`
  - `alphabet_size = 5`
  - `min_gap = 4`
  - `max_gap = 8`
  - `trace_width = 9`
  - `control_resistant = true`

### 3. `r4_alphabet_extension`
- purpose:
  - test whether the same mechanism survives broader symbol space without adding a new mechanism
- pressure axis:
  - larger alphabet size
- parameters:
  - `seed = 20260322`
  - `dataset_size = 224`
  - `seq_len = 10`
  - `alphabet_size = 7`
  - `min_gap = 3`
  - `max_gap = 6`
  - `trace_width = 7`
  - `control_resistant = true`

### 4. `r4_combined_bounded`
- purpose:
  - test one bounded combined slice without opening unbounded complexity
- pressure axes:
  - longer sequence length
  - larger recall gap
  - larger alphabet size
- parameters:
  - `seed = 20260323`
  - `dataset_size = 256`
  - `seq_len = 14`
  - `alphabet_size = 7`
  - `min_gap = 4`
  - `max_gap = 8`
  - `trace_width = 9`
  - `control_resistant = true`

## Why this matrix is still bounded

- maximum `seq_len` remains `14`
- maximum `alphabet_size` remains `7`
- maximum `max_gap` remains `8`
- combined pressure is limited to one slice only
- no new control family is introduced
- no second mechanism is introduced

## What `TASK-7619` must emit for each slice

At minimum:
- slice manifest
- deterministic dataset artifact
- `candidate_accuracy`
- `no_memory_control_accuracy`
- `trivial_last_symbol_memory_accuracy`
- `delta_vs_no_memory`
- `delta_vs_trivial_memory`
- gap-wise accuracy summary
- hardest-gap summary
- deterministic replay status

## Current matrix interpretation

- `r4_length_extension` is the cleanest endurance check against longer context
- `r4_gap_extension` is the strongest pure memory-depth check
- `r4_alphabet_extension` is the cleanest symbol-space generalization check
- `r4_combined_bounded` is the strictest bounded slice and must remain single-shot rather than opening a full factorial sweep

## What this matrix does not authorize

It does not authorize:
- multi-mechanism assembly
- a second memory structure
- widening beyond the stated slice bounds
- organism or cell claims
- early `CONFIRM_SINGLE_MECHANISM_GENERALIZATION`

## Next honest step

The correct next step after this matrix is:
1. implement the four required R4 slices deterministically,
2. measure the same FIFO mechanism against the same two controls,
3. then let `TASK-7620` decide:
   - `CONFIRM_SINGLE_MECHANISM_GENERALIZATION`
   - `REMAIN_IN_R4_GENERALIZATION`
