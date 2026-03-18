# DECISION MEMO — KC1 Variant for Phase-0 vNext

## Evidence Summary
Source: `reports/analysis/EXP_0010_KC1_VARIANTS_EVAL_REPORT.md`

Key counts (dead/control/negative):
- KC1_BASELINE: dead pass=0/110, control pass=110/110, negative pass=0/20
- KC1_TTT: dead pass=60/110, control pass=110/110, negative pass=0/20
- KC1_SLOPE: dead pass=110/110, control pass=0/110, negative pass=0/20

## Decision Rule Applied (verbatim)
- If variant meets sanity (negatives fail, controls pass) and improves false negatives for dead set, recommend as KC1' for Phase-0 vNext.
- If variants break sanity, keep KC1 baseline.

## Recommendation
**Adopt KC1_TTT as KC1' for Phase-0 vNext** (new experiment only).
- KC1_TTT preserves negative-control FAIL and control PASS, while reducing false negatives in dead configs.
- KC1_SLOPE fails sanity (controls all FAIL) and is rejected.

## Constraints / Non-Changes
- No changes are made to exp_0007 or exp_0009.
- Adoption of KC1_TTT requires creating a new Phase-0 vNext experiment.

## Rollback Plan
If KC1_TTT proves too permissive/strict in vNext, revert to KC1_BASELINE in the next version with explicit documentation.
