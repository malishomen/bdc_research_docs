# BDC R5 Single-Mechanism Transfer Pre-Experiment Gate

## Cycle Identity
- Cycle ID: `BDC_R5_SINGLE_MECHANISM_TRANSFER`
- Scientific phase: `R5 - Single-Mechanism Transfer`
- Confirmed source environment family: `controlled_sequence_memory`
- Active mechanism: `bounded_working_memory_candidate`
- Date: `2026-03-19`

## Hypothesis
- Primary hypothesis:
  - after confirmed single-mechanism generalization, the same mechanism should first transfer into one adjacent bounded environment family before any mechanism interaction is introduced.
- Alternative bounded hypothesis:
  - the transfer target may still be too weak or too noisy, so the project may need to remain in `R5` transfer planning.
- Out-of-scope hypotheses:
  - multi-mechanism assembly,
  - organism or cell claims,
  - broad architecture search.

## Decision Gate
- What decision must this cycle support?
  - whether there is an honest adjacent bounded transfer target ready for launch preparation.
- Allowed outcomes:
  - `APPROVE_R5_TRANSFER_TARGET`
  - `REMAIN_IN_R5_TRANSFER`

## Evidence State
- Measured evidence:
  - two bounded positive signals exist for the same mechanism,
  - one of them is control-resistant,
  - single-mechanism generalization is confirmed,
  - the post-`R4` gate selects transfer rather than micro-assembly.
- Missing evidence:
  - no out-of-family transfer evidence exists yet,
  - no adjacent transfer target has been approved yet,
  - no transfer launch surface exists yet.

## False Directions To Exclude
- Do not let transfer planning widen into a second mechanism.
- Do not let cloze or uncertainty rhetoric outrun deterministic bounded framing.
- Do not jump directly into a run before the target surface is explicitly approved.

## Minimal Execution Scope
- compare the adjacent bounded transfer targets honestly,
- choose the narrowest honest target,
- prepare a reproducible launch-ready transfer surface without running the long-run yet.
