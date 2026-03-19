# BDC R3 Control-Resistant Sequence-Memory Pre-Experiment Gate

## Cycle Identity
- Cycle ID: `BDC_R3_CONTROL_RESISTANT_SEQUENCE_MEMORY`
- Scientific phase: `R3 - Mechanism Continuation`
- Active environment family: `controlled_sequence_memory`
- Date: `2026-03-19`

## Hypothesis
- Primary hypothesis:
  - the bounded FIFO working-memory mechanism should retain measurable superiority when shortcut-friendly alignment is removed from the dataset.
- Out-of-scope hypotheses:
  - second mechanism addition,
  - uncertainty handling,
  - multi-buffer architecture,
  - organism-level claims.

## Decision Gate
- What decision must this cycle support?
  - whether a second independent bounded signal exists for the same mechanism family.
- Allowed gate outcomes:
  - `CONFIRM_SECOND_BOUNDED_SIGNAL`
  - `REMAIN_IN_R3_CONTINUATION`

## Evidence State
- Measured evidence:
  - first bounded mechanism win already exists,
  - deterministic replay surface already exists,
  - controls already exist.
- Missing evidence:
  - no measured control-resistant slice yet,
  - no second bounded signal yet.

## False Directions To Exclude
- Do not add a second mechanism.
- Do not reopen environment choice.
- Do not relax baseline pressure.
- Do not treat the first easy win as sufficient on its own.

## Minimal Execution Scope
- Build one deterministic control-resistant dataset variant.
- Reuse the same bounded FIFO memory mechanism.
- Re-measure only against existing controls.
