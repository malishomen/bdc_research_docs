# EXP-0805: R3 Sequence-Memory Mechanism Implementation Package

## Purpose

This package converts the first R3 mechanism cycle into a bounded executable chain.

## Required implementation sequence
1. `TASK-7609` - mechanism candidate spec and state-update contract
2. `TASK-7610` - bounded implementation + controls + tests
3. `TASK-7611` - measured mechanism gate audit

## Required controls
- `no_memory_control`
- `trivial_last_symbol_memory`
- `bounded_working_memory_candidate`

## Definition of Done
- mechanism candidate implemented,
- controls implemented,
- deterministic replay preserved,
- gate packet emits only:
  - `APPROVE_MECHANISM_CONTINUATION`
  - `REMAIN_IN_MECHANISM_PHASE`
