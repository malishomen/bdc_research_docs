# ADR_0003: KC1_EARLY_COLLAPSE semantics — instantaneous threshold vs time-to-diversity (slow-start)

## Status
Proposed

## Context
Evidence from exp_0007 and exp_0009 shows a tension between **instantaneous early thresholds** and **slow-start** diversity dynamics.

- exp_0007: 11 dead configs (pass_rate=0.0), dominated by **clonal_init + low mutation**; KC1_EARLY_COLLAPSE is the dominant failure mode.
- exp_0009: KC1 triggers at **gen=1** for all dead configs, yet those same configs reach **D>=0.10 by ~gen=3 (median)** and **E>=1.0 by gen=1**; controls do not trigger KC1. Negative controls fail as expected.

References:
- `reports/analysis/EXP_0007_PHASE0_FULLSWEEP_ANALYSIS.md`
- `reports/analysis/EXP_0009_KC1_DIAGNOSTICS_REPORT.md`

## Decision Drivers
- **Reproducibility:** KC1 must be deterministic and reproducible under PiStream seeding.
- **False negatives vs early pruning:** Avoid discarding viable “slow-start” configs too aggressively.
- **Scientific claim boundaries:** What counts as “alive” must remain evidence-backed.
- **Compute budget (HIVE):** Early pruning can reduce CPU/GPU cost but risks invalid pruning.
- **Routing implications:** KC1 influences CPU/GPU routing gates for exploration vs evidence.

## Options
A) **Keep KC1 as-is (instantaneous/early threshold)**
- Rule: KC1 triggers if `E<1.0` or `D<0.10` at any generation `g<=G_MIN`.
- Pros: strict early collapse filter, minimal compute.
- Cons: may label slow-start configs as dead (false negatives).

B) **Introduce KC1' (time-to-threshold)**
- Rule: FAIL only if **D does not reach 0.10 by gen<=3** (fixed early window).
- Pros: allows brief slow-start while still catching collapse.
- Cons: more compute; changes “alive” definition.

C) **Introduce KC1'' (slope/window-based)**
- Rule: FAIL only if **slope_D_0_10 < 0.01** over gens 0..10.
- Pros: captures persistent collapse vs delayed ramp.
- Cons: requires enough generations to estimate slope; may pass borderline cases.

## Consequences
- **Compute budget:** B/C increase early-run compute, may impact HIVE scheduling and CPU queues.
- **Routing policy:** A tighter KC1 increases early CPU pruning; B/C may allow GPU acceleration for more configs (if gates satisfied).
- **Scientific claims:** B/C broaden the “alive” definition; must be clearly labeled as a **new Phase-0 vNext policy**, not retroactively applied to exp_0007.

## Decision
No change to exp_0007/exp_0009. Evaluate KC1 variants via **exp_0010** (pre-registered) and decide whether to adopt KC1' for **Phase-0 vNext** only.

## Notes
- This ADR does **not** change any existing experiments.
- Any KC1 revision must be introduced in a **new experiment/version** with explicit labeling and evidence.
