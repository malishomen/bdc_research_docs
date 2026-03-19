# BDC R4 Single-Mechanism Generalization Pre-Experiment Gate

## Cycle Identity
- Cycle ID: `BDC_R4_SINGLE_MECHANISM_GENERALIZATION`
- Scientific phase: `R4 - Single-Mechanism Generalization`
- Active environment family: `controlled_sequence_memory`
- Active mechanism: `bounded_working_memory_candidate`
- Date: `2026-03-19`

## Hypothesis
- Primary hypothesis:
  - the approved FIFO working-memory mechanism should retain superiority under broader bounded pressure without changing mechanism identity.
- Out-of-scope hypotheses:
  - multi-mechanism interaction,
  - assembly,
  - organism or cell claims,
  - environment-family replacement.

## Decision Gate
- What decision must this cycle support?
  - whether the same mechanism family truly generalizes under bounded pressure.
- Allowed outcomes:
  - `CONFIRM_SINGLE_MECHANISM_GENERALIZATION`
  - `REMAIN_IN_R4_GENERALIZATION`

## Evidence State
- Measured evidence:
  - two bounded positive signals exist,
  - one of them is control-resistant,
  - the same mechanism identity has been preserved so far.
- Missing evidence:
  - no broader generalization matrix has been measured,
  - no combined bounded pressure slice has been measured.

## False Directions To Exclude
- Do not add a second mechanism.
- Do not widen memory architecture silently.
- Do not use adaptive learning or training.
- Do not treat two bounded signals as equivalent to generalization.

## Minimal Execution Scope
- define a bounded pressure matrix,
- keep the same FIFO mechanism identity,
- measure performance against the same controls,
- and decide whether generalization is real or not.
