# EXP-0813: Post-R4 Decision Implementation Package

## Purpose

This package turns the post-`R4` decision into a bounded executable gate.

## Required implementation sequence
1. `TASK-7621` - decision package and gate framing
2. `TASK-7622` - BDC-assisted option comparison and verdict

## Required options
1. `single_mechanism_transfer_gate`
2. `minimal_multi_mechanism_micro_assembly`

## Definition of Done
- the decision surface is explicitly serialized,
- `BDC Designer` processes the packet,
- the gate emits one of:
  - `OPEN_SINGLE_MECHANISM_TRANSFER_GATE`
  - `OPEN_MINIMAL_MICRO_ASSEMBLY_GATE`
  - `REMAIN_IN_POST_R4_GATE`

## Scope rule
- This package chooses the next bounded gate only.
- It does not implement the next gate yet.
