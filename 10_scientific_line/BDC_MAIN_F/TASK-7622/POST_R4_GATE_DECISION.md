# Post-R4 Gate Decision

## Canonical Verdict
- `OPEN_SINGLE_MECHANISM_TRANSFER_GATE`

## BDC Designer result
From `docs/experiments/BDC_POST_R4_DECISION_PACKET/BDC_CLIENT_BUNDLE_OUTPUT/bundle_result.json`:
- `supported = true`
- `recommended_variant_id = single_mechanism_transfer_gate`
- `strategy_mode = direct_architecture_selection`
- `confidence_band = high`
- `selective_outcome_class = recommend_ready`
- `evidence_state_class = inferred_only`

## Why this is the honest choice

Current evidence asymmetry is clear:
- the same mechanism now has bounded generalization confirmation,
- no measured second mechanism exists,
- no measured mechanism interaction evidence exists,
- no measured micro-assembly behavior exists.

Because of that asymmetry, the narrowest honest next gate is:
- `single_mechanism_transfer_gate`

and not:
- `minimal_multi_mechanism_micro_assembly`

## What this verdict does mean

It means:
- the next bounded package should still preserve the same single mechanism,
- the project should test transfer of that mechanism into one adjacent bounded environment family before opening assembly.

## What this verdict does not mean

It does not mean:
- micro-assembly is falsified forever,
- interaction is impossible,
- organism or cell claims are closer than before.

It only means that immediate micro-assembly would still be premature relative to current evidence.
