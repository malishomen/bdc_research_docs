# BDC Post-Second-Signal Pre-Experiment Gate

## Cycle Identity
- Cycle ID: `BDC_POST_SECOND_SIGNAL_GATE`
- Scientific phase: `R3 post-second-signal decision`
- Active environment family: `controlled_sequence_memory`
- Confirmed mechanism: `bounded_working_memory_candidate`
- Date: `2026-03-19`

## Hypothesis
- Primary hypothesis:
  - after two bounded single-mechanism signals, the next correct gate is more likely to be single-mechanism generalization than immediate two-mechanism micro-assembly.
- Alternative bounded hypothesis:
  - the evidence may already justify a minimal two-mechanism micro-assembly gate.
- Out-of-scope hypotheses:
  - organism validity,
  - cell validity,
  - broad architecture search.

## Decision Gate
- What decision must this cycle support?
  - whether the next bounded gate should be `single_mechanism_generalization` or `minimal_multi_mechanism_micro_assembly`.
- Allowed outcomes:
  - `OPEN_SINGLE_MECHANISM_GENERALIZATION_GATE`
  - `OPEN_MINIMAL_MICRO_ASSEMBLY_GATE`
  - `REMAIN_IN_POST_SECOND_SIGNAL_GATE`

## Evidence State
- Measured evidence:
  - two positive bounded signals exist for `bounded_working_memory_candidate`,
  - both signals remain inside the same environment family,
  - one of the signals is control-resistant.
- Missing evidence:
  - no second mechanism has ever been measured,
  - no mechanism-interaction evidence exists,
  - no micro-assembly evidence exists.

## False Directions To Exclude
- Do not let second-signal confirmation masquerade as assembly evidence.
- Do not widen to organism or cell rhetoric.
- Do not discard BDC Designer narrowing at this transition point.

## Minimal Execution Scope
- compare exactly two next-step options,
- serialize the evidence asymmetry honestly,
- let the gate choose the next bounded package.
