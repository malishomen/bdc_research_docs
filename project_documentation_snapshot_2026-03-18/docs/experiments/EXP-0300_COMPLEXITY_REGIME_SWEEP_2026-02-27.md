# EXP-0300: Complexity Regime Sweep (2026-02-27)

## Background

`TASK-1400B` showed that the legacy complexity regime `A` (`fitness = accuracy - 0.01 * sum(|w|)`) makes `v2` mathematically blocked (`required_accuracy_to_beat_v1 > 1.0`).

Phase 1 in `docs/project/project_roadmap.md` required a controlled sweep of complexity regimes to test whether selection physics can be fixed without changing the hidden_rule lab role.

## Hypotheses & Relation to CANON/ADR

- Primary hypothesis (Phase 1): at least one complexity regime makes `v2` mathematically feasible.
- Competitiveness check: feasibility alone is insufficient; empirical `v2` trajectory must approach/beat `v1`.
- Governance links:
  - `decisions/ADR-0004-hidden-rule-closure.md` - hidden_rule remains lab-only.
  - `decisions/ADR-0005-complexity-regime.md` - canonical regime decision after this experiment.

## Protocol

- Matrix: 5 regimes (`A,B,C,D,E`) x 3 genomes (`v1,v1_5,v2`) = 15 configs.
- Full-scale run:
  - Seeds `N=30`
  - Generations `G=100`
  - Population `P=100`
- Runtime tooling:
  - `scripts/edp1/run_complexity_sweep_1501.py`
  - `scripts/edp1/aggregate_results.py`
- Artifact roots (runtime, not committed):
  - `results/edp1_exp0300_complexity/<regime>_<genome>/...`
  - `results/edp1_exp0300_complexity_sweep/complexity_sweep_summary.json`

## Results

Key sweep summary (means over `N=30`, from TASK-1502/ADR-0005):

| Regime | Definition (short) | v2 feasible? | v1 final max fitness | v2 final max fitness | required_accuracy_to_beat_v1 | Conclusion |
|---|---|---:|---:|---:|---:|---|
| A | `sum(|w|)` + linear penalty | false | 0.788166 | 0.553166 | 1.130104 | Structural impossibility remains |
| B | `mean(|w|)` + linear penalty | true | 0.819032 | 0.784223 | 0.826803 | Feasible; best non-zero-penalty tradeoff |
| C | `sum(|w|)/sqrt(K)` + linear penalty | true | 0.811915 | 0.751174 | 0.863464 | Feasible but weaker than B |
| D | `sum(|w|)` + class lambda | false | 0.788166 | 0.553166 | 1.130104 | Equivalent blockage to A at default lambdas |
| E | penalty off (`fitness=accuracy`) | true | 0.823047 | 0.790234 | 0.823047 | Feasible but zero complexity pressure |

Additional stable observation:
- `v2 final_max_accuracy_mean = 0.790234375` across regimes; the sweep changes physics of selection, not raw representational ceiling.

## Interpretation

- Feasibility was restored in `B/C/E`.
- Empirical competitiveness was **not** achieved in Phase 1: `v2` did not beat `v1` on final max fitness or final max accuracy in any regime.
- Regime `B` is the best compromise:
  - removes structural impossibility,
  - keeps non-zero complexity pressure,
  - outperforms regime `C` on `v2` fitness trajectory,
  - avoids no-penalty degeneracy of `E`.

This interpretation is formalized in `decisions/ADR-0005-complexity-regime.md`.

## Impact on roadmap

- Phase 1 outcome for `docs/project/project_roadmap.md`:
  - PASS on feasibility sub-goal (at least one feasible regime exists).
  - PARTIAL on competitiveness sub-goal (no regime gave `v2 >= v1`).
- Canonical regime for next phases is `B` (ADR-0005), while default CLI behavior was intentionally not changed in TASK-1502.

## Links to TASK reports + ADR

- `reports/analysis/TASK-1501-COMPLEXITY-SWEEP/TASK-1501_BRIEF_REPORT.md`
- `reports/analysis/TASK-1502-COMPLEXITY-SWEEP-FULL/TASK-1502_BRIEF_REPORT.md`
- `decisions/ADR-0005-complexity-regime.md`
