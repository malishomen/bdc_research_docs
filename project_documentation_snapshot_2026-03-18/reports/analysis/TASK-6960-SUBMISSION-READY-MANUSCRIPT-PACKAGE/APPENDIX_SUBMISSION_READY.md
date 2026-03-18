# Appendix (Submission-Ready)

## A1. Claim Inventory
- `P1` | `SUPPORTED` | Equilibrium role weights follow causal contribution structure
- `P2` | `SUPPORTED` | Causal architecture emergence is predictable from task structure
- `N1` | `FALSIFIED` | Portable universal transition law across families/role counts
- `N2` | `FALSIFIED` | Regime meta-law alone is sufficient for robust transfer
- `N3` | `FALSIFIED` | Hidden-state augmentation alone rescues transition portability
- `E1` | `FALSIFIED` | Standalone BDC design dominates engineering baselines
- `E2` | `SUPPORTED` | Hybrid BDC-prior search provides practical utility

## A2. Reproduction Matrix
- `C_POS_1` | status=`reproducible` | check=`scope_statement_contains_restricted_theory`
- `C_NEG_1` | status=`reproducible` | check=`falsified_claims_contains_transition_portability`
- `C_ENG_1` | status=`reproducible` | check=`hybrid_value_supported_true`

## A3. Scope Boundaries
- Positive core is bounded to restricted BDC setup with documented OOD envelopes.
- Transition-law non-portability is treated as a first-class negative result.
- Engineering value is framed as hybrid utility, not universal optimality.
