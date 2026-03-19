# R4 Single-Mechanism Generalization Measurement Note

## Status
- Date: 2026-03-19
- Task: `TASK-7619`
- Result type: measured deterministic artifact set

## Result root
- `results/r4_single_mechanism_generalization`

## What was measured

The same approved FIFO mechanism `bounded_working_memory_candidate` was measured on all four required `R4` slices from the canonical pressure matrix:

1. `r4_length_extension`
2. `r4_gap_extension`
3. `r4_alphabet_extension`
4. `r4_combined_bounded`

The same controls remained active on every slice:
- `majority_symbol_predictor`
- `always_repeat_last_symbol`

## Measured summary

From `results/r4_single_mechanism_generalization/generalization_summary.json`:

- `slice_count = 4`
- all slices:
  - `candidate_accuracy = 1.0`
  - `no_memory_control_accuracy = 0.0`
  - `trivial_last_symbol_memory_accuracy = 0.0`
  - `deterministic_replay_status = true`
  - `candidate_gt_no_memory = true`
  - `candidate_gt_trivial = true`
  - `hardest_gap_gt_no_memory = true`
  - `hardest_gap_gt_trivial = true`

### Hardest measured recall gaps
- `r4_length_extension`:
  - `hardest_recall_gap = 6`
- `r4_gap_extension`:
  - `hardest_recall_gap = 8`
- `r4_alphabet_extension`:
  - `hardest_recall_gap = 6`
- `r4_combined_bounded`:
  - `hardest_recall_gap = 8`

## Interpretation

- the same FIFO mechanism remained intact across all required bounded `R4` slices,
- no widening to a second mechanism or second state channel was needed,
- the measured superiority is present on every slice and on each slice's hardest recall gap,
- therefore `TASK-7619` successfully converts the `R4` matrix into a measured surface suitable for `TASK-7620`.

## Constraint

This note does not emit the `R4` verdict.

The only honest next step is:
- run `TASK-7620`
- and decide:
  - `CONFIRM_SINGLE_MECHANISM_GENERALIZATION`
  - `REMAIN_IN_R4_GENERALIZATION`
