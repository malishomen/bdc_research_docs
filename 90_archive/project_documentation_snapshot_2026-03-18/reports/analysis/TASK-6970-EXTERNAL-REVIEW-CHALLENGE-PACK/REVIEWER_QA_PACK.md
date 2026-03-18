# Reviewer QA Pack

## 1. Likely Reviewer Attacks
- **novelty attack** (likelihood=medium, severity=medium): Use falsification-aware positioning and evidence traceability.
- **scope attack** (likelihood=high, severity=high): Point to explicit non-claims and restricted scope statement.
- **negative-result attack** (likelihood=medium, severity=medium): Use falsification-aware positioning and evidence traceability.
- **external-validity attack** (likelihood=high, severity=medium): Bound claims to tested OOD and pilot domains; avoid universal language.
- **engineering-value attack** (likelihood=high, severity=medium): Bound claims to tested OOD and pilot domains; avoid universal language.
- **reproducibility attack** (likelihood=medium, severity=high): Provide claim-evidence links and one-command repro path.
- **causality-overclaim attack** (likelihood=medium, severity=high): Provide claim-evidence links and one-command repro path.

## 2. Claim Defense Map
- `P1` [SUPPORTED]: Cite frozen evidence and keep inference bounded to declared scope. (evidence: restricted_bdc_theory.json)
- `P2` [SUPPORTED]: Cite frozen evidence and keep inference bounded to declared scope. (evidence: restricted_bdc_theory.json, design_rules.json)
- `N1` [FALSIFIED]: Present as explicit negative result and explain engineering implication. (evidence: restricted_bdc_theory.json)
- `N2` [FALSIFIED]: Present as explicit negative result and explain engineering implication. (evidence: restricted_bdc_theory.json, design_limits_summary.json)
- `N3` [FALSIFIED]: Present as explicit negative result and explain engineering implication. (evidence: restricted_bdc_theory.json)
- `E1` [FALSIFIED]: Present as explicit negative result and explain engineering implication. (evidence: design_limits_summary.json)
- `E2` [SUPPORTED]: Cite frozen evidence and keep inference bounded to declared scope. (evidence: hybrid_value_summary.json)

## 3. Overclaim Risk Flags
- pattern=`universal` count=2 risk=high -> Replace with bounded wording tied to scope statement.
- pattern=`always` count=0 risk=low -> No action.
- pattern=`prove` count=0 risk=low -> No action.
- pattern=`guarantee` count=0 risk=low -> No action.
- pattern=`scope_non_claims_declared` count=3 risk=low -> No action.

## 4. What Is Claimed / Not Claimed
- Claimed: restricted equilibrium/architecture/hybrid utility under bounded scope.
- Not claimed: universal transition law, unbounded external validity, standalone universal dominance.
