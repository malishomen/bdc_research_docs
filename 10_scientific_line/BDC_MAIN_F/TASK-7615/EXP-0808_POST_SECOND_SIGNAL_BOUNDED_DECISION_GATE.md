# EXP-0808: Post-Second-Signal Bounded Decision Gate

## Status
- Date: 2026-03-19
- Status: ACTIVE DECISION PACKAGE
- Depends on:
  - `docs/experiments/R3_SECOND_BOUNDED_SIGNAL_GATE_DECISION.md`
  - `docs/project/BDC_SCIENTIFIC_PREEXPERIMENT_GATE_PROTOCOL.md`

## Purpose

This package opens the first bounded decision gate after confirmation of a second bounded signal for the same replayable memory mechanism family.

The project now has enough evidence to discuss a broader next gate.
It still does not have authority to widen automatically.

## Decision question

What is the next honest bounded move after two positive signals for `bounded_working_memory_candidate` inside `controlled_sequence_memory`?

## Candidate next-step options

1. `single_mechanism_generalization`
- keep one mechanism only,
- vary the sequence-memory environment within the same family,
- test whether the same mechanism survives broader but still bounded pressure.

2. `minimal_multi_mechanism_micro_assembly`
- keep the approved memory mechanism,
- add one additional minimal mechanism,
- test whether a two-mechanism micro-assembly remains interpretable and bounded.

## Decision gate outcomes

This package must end with one of:
- `OPEN_SINGLE_MECHANISM_GENERALIZATION_GATE`
- `OPEN_MINIMAL_MICRO_ASSEMBLY_GATE`
- `REMAIN_IN_POST_SECOND_SIGNAL_GATE`

## Why this gate exists

Without an explicit gate, the project could easily overread the second bounded signal and jump directly into premature assembly rhetoric.

That would be a process defect.

## Current evidence asymmetry

What is already measured:
- two bounded positive signals for the same FIFO memory mechanism,
- one permissive slice,
- one control-resistant slice.

What is not yet measured:
- any second mechanism,
- any interaction between two mechanisms,
- any bounded assembly behavior,
- any evidence that interpretability survives beyond single-mechanism scope.

## Immediate interpretation rule

The existence of a second bounded signal strengthens the case for a broader next gate.

It does not settle which broader gate is correct.

## What this package must not do

- It must not silently approve micro-assembly.
- It must not silently widen to organism or cell language.
- It must not re-open environment choice.
- It must not pretend that two single-mechanism signals equal assembly evidence.

## Immediate next step

The next correct action is:
1. serialize a bounded comparison surface for the two next-step options,
2. run that surface through `BDC Designer`,
3. only then emit the post-second-signal gate verdict.
