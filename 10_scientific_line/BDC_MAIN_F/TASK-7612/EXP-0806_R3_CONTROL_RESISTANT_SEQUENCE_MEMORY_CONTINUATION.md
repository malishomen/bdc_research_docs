# EXP-0806: R3 Control-Resistant Sequence-Memory Continuation

## Status
- Date: 2026-03-19
- Status: ACTIVE SCIENTIFIC PACKAGE
- Depends on:
  - `docs/experiments/R3_SEQUENCE_MEMORY_MECHANISM_GATE_DECISION.md`
  - `docs/project/BDC_SCIENTIFIC_PREEXPERIMENT_GATE_PROTOCOL.md`

## Purpose

This package opens the next bounded continuation cycle after the first approved `R3` mechanism win.

It stays inside the same approved environment family:
- `controlled_sequence_memory`

It does not add a second mechanism.
It does not reopen environment choice.
It does not widen to organism claims.

## Scientific question

Can the same bounded FIFO working-memory mechanism retain superiority when the dataset is made explicitly resistant to shortcut controls?

## Why this continuation is stricter

The first `R3` win was honest, but relatively easy:
- the replayable memory candidate had full recall coverage,
- `last_symbol` and `majority` controls were allowed to remain naturally present,
- and the signal may still be dismissed as a favorable first slice.

This continuation removes that weakness.

## Required stricter environment conditions

The continuation artifact must remain in the same sequence-memory family, but add at minimum:
1. `target_symbol != last_symbol`
2. `target_symbol != majority_symbol`
3. deterministic generation remains preserved
4. replay contract remains unchanged

## Allowed mechanism surface

Still only:
1. `majority_symbol_predictor` as no-memory control
2. `trivial_last_symbol_memory`
3. `bounded_working_memory_candidate`

No second mechanism may be added in this cycle.

## Decision gate

This continuation cycle must end with one of two outcomes:
- `CONFIRM_SECOND_BOUNDED_SIGNAL`
- `REMAIN_IN_R3_CONTINUATION`

## What this cycle must prove

It must prove that the approved bounded memory mechanism is not only better on a permissive first slice, but still superior when easy shortcut alignments are explicitly removed.

## What this cycle must not claim

It must not claim:
- general memory solved,
- multi-mechanism readiness,
- organism assembly readiness,
- or cell-level validity.

## Immediate next step

The correct next step after this package is:
1. implement the deterministic control-resistant environment artifact,
2. measure the existing memory mechanism inside it,
3. run a bounded second-signal gate.
