# EXP-0800: Selection Physics Reboot (2026-03-17)

## Background

`TASK-1400B` and `ADR-0004` established that the old `hidden_rule` line cannot remain the active product path and that the legacy selection physics structurally blocks architectural growth.

`docs/project/BDC_RESEARCH_REBOOT_PLAN.md` therefore sets Phase `R1` as the first real scientific gate of the reboot:

- validate new resource/energy/complexity selection physics,
- before any new organism-level buildout is attempted.

This experiment package is the first scientific package of the rebooted BDC research line.

## Hypotheses & Relation to CANON/ADR

### Primary hypothesis
At least one new selection regime can:
- preserve mathematical feasibility of architectural growth,
- avoid immediate empirical collapse,
- and remain more biology-like than the old linear complexity penalty.

### Secondary hypothesis
A regime can be acceptable for reboot progression even if it does not yet produce final superiority over historical baselines, provided it:
- removes structural impossibility,
- and produces bounded, non-collapsing search dynamics.

### Governance anchors
- `CANON.md`
- `decisions/ADR-0004-hidden-rule-closure.md`
- `decisions/ADR-0005-complexity-regime.md`
- `docs/project/BDC_PROJECT_HISTORY_MAP.md`
- `docs/project/BDC_RESEARCH_REBOOT_PLAN.md`
- `docs/project/BDC_RESEARCH_REBOOT_CHARTER.md`

## Protocol

### Objective
Test a new family of selection/resource regimes without reopening the old `hidden_rule` line as a product claim.

### Experimental role of the environment
The environment in this phase is still a **controlled laboratory stand**.
It is not yet the final reboot task environment.

Its purpose is only:
- to compare regime behavior cleanly,
- to test feasibility and collapse properties,
- to isolate the effect of selection physics.

### Candidate regime families

The reboot package must test at least these regime families:

1. **Legacy control**
   - historical linear complexity penalty
   - included only as control

2. **Energy-budget regime**
   - complexity consumes energy budget rather than directly subtracting fitness

3. **Maintenance-cost regime**
   - architectural complexity imposes recurring maintenance cost
   - but not hard direct linear impossibility

4. **Resource-allocation regime**
   - agents allocate finite resources across capacity, action, and persistence

5. **Hybrid bounded regime**
   - combines energy and maintenance signals
   - explicitly constrained to avoid zero-cost complexity fantasy

### Minimum protocol contract
- `N >= 30` seeds unless an explicit diagnostic substage is justified
- deterministic seeds and environment manifests
- explicit baseline/control regime included
- explicit feasibility calculation
- explicit collapse metrics
- no post-hoc regime deletion from final report

### Minimum metrics

For each regime:
- feasibility flag for architectural growth
- required_accuracy_to_beat_legacy_baseline
- final max fitness
- final max accuracy
- complexity or capacity load
- collapse rate
- entropy / diversity retention
- non-trivial strategy rate
- runtime pass rate

### Mandatory comparisons
- regime vs legacy control
- regime vs no-penalty diagnostic floor/ceiling control
- regime vs at least one bounded non-linear alternative

## Results

This experiment package is not executed yet.

Expected result structure:
- regime comparison table
- feasibility summary
- collapse summary
- pass/fail gate verdict

## Interpretation

Pass does **not** mean:
- the reboot has recovered digital organisms,
- the old biological ambitions are validated,
- or the project is ready for SuperCell assembly.

Pass means only:
- selection physics is no longer structurally broken enough to block further reboot phases.

Failure means:
- do not proceed to organism/component assembly,
- redesign the regime family first.

## Impact on Roadmap

If this package passes:
- authorize `Phase R2 — New Controlled Task Environment`

If this package fails:
- remain inside `Phase R1`
- iterate on regime design only

## Links to TASK reports + ADR

Required upstream:
- `reports/analysis/TASK-1400B-COMPLEXITY-AUDIT-ADDENDUM/TASK-1400B_BRIEF_REPORT.md`
- `decisions/ADR-0004-hidden-rule-closure.md`
- `decisions/ADR-0005-complexity-regime.md`
- `docs/project/BDC_PROJECT_HISTORY_MAP.md`
- `docs/project/BDC_RESEARCH_REBOOT_PLAN.md`
- `docs/project/BDC_RESEARCH_REBOOT_CHARTER.md`

