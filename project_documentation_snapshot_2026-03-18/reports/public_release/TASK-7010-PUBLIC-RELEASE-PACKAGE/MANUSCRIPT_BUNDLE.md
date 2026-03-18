# Manuscript Bundle (Public Release)

## Main Manuscript

# Restricted BDC Theory: Submission-Ready Manuscript

## Positioning Statement
This manuscript presents BDC as a restricted theory: validated for equilibrium-guided architecture priors and hybrid engineering utility, while explicitly rejecting portable universal transition-law claims.

## Frozen Core Claims
- Positive: equilibrium/architecture prior validity within bounded scope.
- Negative: no portable low-dimensional transition law under tested transfer regimes.
- Engineering: hybrid prior-guided search retains practical utility.

## Evidence Highlights
- OOD transfer supported: `True`
- OOD equilibrium transfer pass-rate: `0.8333`
- OOD hybrid transfer pass-rate: `1.0000`
- Playbook supported: `True`
- Strategy selection accuracy: `1.0000`
- Real-world pilot supported: `True`
- Hybrid speedup (hours): `16.4900`

## Scope Guardrails
- This paper does not claim universal transition dynamics across all task families.
- This paper does not claim standalone BDC design dominance over all search baselines.
- This paper claims bounded utility under explicit strategy-selection and reproducibility contracts.

## Draft Carry-Forward
# Restricted BDC: Manuscript Draft

## 1. Introduction
This draft consolidates restricted BDC claims into a publication-ready narrative with explicit positive and negative results.

## 2. Theory Scope
- Restricted theory status: `restricted`
- Transition portability supported: `False`

## 3. Positive Results
- Supported claim count: `3`
- OOD core transfer supported: `True`
- OOD equilibrium transfer pass-rate: `0.8333`
- OOD hybrid transfer pass-rate: `1.0000`
- OOD role-count transfer pass-rate: `1.0000`

## 4. Negative Results
- Falsified claim count: `4`
- Portable low-dimensional transition law was not recovered under tested settings.

## 5. Engineering Implications
- Playbook supported: `True`
- Strategy selection accuracy: `1.0000`
- Mean performance delta vs default: `-0.0134`
- Mean cost reduction vs default: `1.2857`

## 6. Limitations
- Findings are validated under the defined synthetic and OOD benchmark envelopes, not all possible real-world distributions.
- Engineering value is strongest in hybrid-guided workflows and weaker as standalone architecture selection.

## 7. Reproducibility
- Core claims matrix, scope statement, and OOD/playbook summaries are linked in the section and figure manifests.
- Independent reproduction package is available from TASK-6920.

## 8. Conclusion
Restricted BDC remains scientifically defensible as a causal-equilibrium and architecture-prior framework with practical value in hybrid search settings.

## Camera-Ready Checklist
- Claims table frozen and linked to evidence artifacts.
- Figure/table list frozen with source mapping.
- Reproducibility note provides one-command verification path and artifact integrity checks.

## Appendix

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

## Reproducibility Note

# Reproducibility Note

## One-command check
python scripts/analysis/run_phase22_independent_reproduction_package.py --out_root results/reproduction_package

## Required artifacts
- results/restricted_bdc_consolidation/core_claims_matrix.csv
- results/restricted_bdc_consolidation/theory_scope_statement.json
- results/negative_transition_result/restricted_bdc_theory.json
- results/hybrid_architecture_search/hybrid_value_summary.json
- results/design_rulebook/design_rules.json
- results/effective_role_count/stopping_rule_summary.json

## Integrity checks
1. Verify expected artifacts exist in `results/reproduction_package/expected_artifacts.csv`.
2. Verify claim statuses in `results/reproduction_package/claim_reproduction_matrix.csv`.
3. Verify manuscript freeze tables in `results/submission_package/`.
