# R2 Controlled Sequence Memory Artifact

## Status
- Date: 2026-03-19
- Status: EXECUTABLE DETERMINISTIC ARTIFACT
- Role in R2: conservative implementation prior

## Purpose

This artifact converts `controlled_sequence_memory` from an analytical prior into an executable deterministic environment surface.

It is intentionally narrow.
It does not approve the entire R2 phase.
It creates the first measured implementation foothold inside R2.

## What is implemented
- deterministic dataset constructor,
- recall-gap task structure,
- baseline scorecard,
- smoke-run artifact writer,
- regression tests.

## Current smoke evidence
- dataset size: `64`
- sequence length: `8`
- alphabet size: `4`
- recall gap range: `2..4`
- baseline scorecard:
  - `random_symbol_predictor = 0.203125`
  - `always_repeat_last_symbol = 0.234375`
  - `majority_symbol_predictor = 0.484375`

## Current interpretation
- the task is executable and deterministic,
- last-symbol triviality is not perfect,
- baseline discipline now exists in measured form,
- but the full R2 environment gate still remains open.

## Next honest step
- promote this artifact into candidate-specific gate evidence,
- then rerun the bounded R2 gate on measured rather than inferred support.
