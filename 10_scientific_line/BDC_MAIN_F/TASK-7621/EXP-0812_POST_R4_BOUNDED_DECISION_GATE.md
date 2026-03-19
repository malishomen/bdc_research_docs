# EXP-0812: Post-R4 Bounded Decision Gate

## Status
- Date: 2026-03-19
- Status: ACTIVE DECISION PACKAGE
- Depends on:
  - `docs/experiments/R4_SINGLE_MECHANISM_GENERALIZATION_GATE_DECISION.md`
  - `docs/project/BDC_SCIENTIFIC_PREEXPERIMENT_GATE_PROTOCOL.md`

## Purpose

This package opens the next bounded decision gate after confirmation of single-mechanism generalization.

The project now has enough evidence to discuss a broader next gate.
It still does not have authority to widen automatically.

## Decision question

What is the next honest bounded move after confirmed single-mechanism generalization for `bounded_working_memory_candidate`?

## Candidate next-step options

### 1. `single_mechanism_transfer_gate`
- keep the same single mechanism only,
- choose one adjacent deterministic bounded environment family,
- test whether the same mechanism survives environment transfer before any mechanism interaction is introduced.

### 2. `minimal_multi_mechanism_micro_assembly`
- keep the approved memory mechanism,
- add one second minimal mechanism,
- test whether a two-mechanism micro-assembly remains bounded and interpretable.

## Decision gate outcomes

This package must end with one of:
- `OPEN_SINGLE_MECHANISM_TRANSFER_GATE`
- `OPEN_MINIMAL_MICRO_ASSEMBLY_GATE`
- `REMAIN_IN_POST_R4_GATE`

## Why this gate exists

Without an explicit gate, the project could overread `R4` confirmation and jump directly into premature assembly rhetoric.

That would be a process defect.

## Current evidence asymmetry

What is already measured:
- two bounded positive signals for the same FIFO memory mechanism,
- one control-resistant continuation signal,
- one bounded generalization confirmation across the required `R4` pressure matrix.

What is not yet measured:
- any second mechanism,
- any interaction between two mechanisms,
- any micro-assembly behavior,
- any out-of-family transfer for the same mechanism.

## Immediate interpretation rule

The existence of bounded generalization strengthens the case for a broader next gate.

It does not settle which broader gate is correct.

## What this package must not do

- It must not silently approve micro-assembly.
- It must not silently widen to organism or cell language.
- It must not pretend that single-mechanism generalization already equals assembly evidence.
- It must not let `BDC Designer` replace the scientific gate.

## Immediate next step

The next correct action is:
1. serialize a bounded comparison surface for the two next-step options,
2. run that surface through `BDC Designer`,
3. only then emit the post-`R4` gate verdict.
