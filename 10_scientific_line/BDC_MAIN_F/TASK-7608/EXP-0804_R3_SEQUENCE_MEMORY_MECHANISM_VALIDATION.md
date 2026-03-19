# EXP-0804: R3 Sequence-Memory Mechanism Validation

## Status
- Date: 2026-03-19
- Status: ACTIVE SCIENTIFIC PACKAGE
- Depends on:
  - `docs/experiments/R2_MEASURED_REFRESH_GATE_DECISION.md`
  - `docs/experiments/R2_CONTROLLED_SEQUENCE_MEMORY_ARTIFACT.md`
  - `docs/project/BDC_SCIENTIFIC_PREEXPERIMENT_GATE_PROTOCOL.md`

## Purpose

This package opens the first bounded downstream mechanism-level cycle after `R2` environment approval.

Approved environment:
- `controlled_sequence_memory`

Allowed scientific question:
- can one explicit bounded memory mechanism outperform no-memory or trivial-memory behavior inside the approved environment?

This package does not authorize:
- organism assembly,
- cell rhetoric,
- multi-mechanism builds,
- or broad architecture search.

## Mechanism focus

The first mechanism-level cycle should isolate:
- `bounded working-memory trace`

Meaning:
- a small explicit internal state that carries limited information across sequence steps,
- with deterministic update rules,
- and measurable contribution beyond trivial heuristics.

## Decision gate

This mechanism cycle must end with one of two outcomes:
- `APPROVE_MECHANISM_CONTINUATION`
- `REMAIN_IN_MECHANISM_PHASE`

## Required comparison surface

At minimum compare:
1. `no_memory_control`
2. `trivial_last_symbol_memory`
3. `bounded_working_memory_candidate`

## Required measurements
- sequence recall accuracy,
- delta over active baselines,
- contribution beyond `majority_symbol_predictor`,
- failure under longer recall gaps,
- deterministic replay of mechanism state updates.

## What must not happen
- no mixing with uncertainty mechanism in the same cycle,
- no language expansion,
- no role inflation,
- no new organism vocabulary.

## Immediate next step

The correct next step after this package is:
1. define the mechanism pre-experiment gate,
2. define the bounded implementation package,
3. only then start coding the first mechanism candidate.
