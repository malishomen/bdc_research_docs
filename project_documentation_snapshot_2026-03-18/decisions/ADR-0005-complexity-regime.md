# ADR-0005: Canonical complexity regime after exp_0300 sweep

Date: 2026-02-27

## Context
- TASK-1400B established that the legacy regime (`A`: `fitness = accuracy - 0.01 * sum(|w|)`) makes `v2` mathematically impossible versus `v1` (`required_accuracy_to_beat_v1 > 1.0`).
- TASK-1501 implemented configurable regimes `A..E` and exp_0300 sweep tooling.
- TASK-1502 executed full exp_0300: 15 configs (`A..E x v1/v1_5/v2`), `N=30`, `G=100`, `P=100`.
- Objective: pick canonical complexity physics for next phases without changing default CLI behavior in this task.

## Alternatives
- **A:** `complexity = sum(|w|)`, `penalty = lambda * complexity` (legacy).
- **B:** `complexity = mean(|w|) = sum(|w|)/K`, `penalty = lambda * complexity`.
- **C:** `complexity = sum(|w|)/sqrt(K)`, `penalty = lambda * complexity`.
- **D:** `complexity = sum(|w|)`, `penalty = lambda_class(genome_version) * complexity`.
- **E:** `complexity` measured, `penalty = 0`, `fitness = accuracy`.

## Evidence
Source:
- `results/edp1_exp0300_complexity_sweep/complexity_sweep_summary.json`
- `results/edp1_exp0300_complexity_sweep/complexity_sweep_summary.csv`

Key table (means over N=30):

| Regime | v2 feasible | v1 max_fit | v2 max_fit | v2 max_acc | v2 max_penalty | required_accuracy_to_beat_v1 |
|---|---:|---:|---:|---:|---:|---:|
| A | false | 0.788166 | 0.553166 | 0.790234 | 0.341938 | 1.130104 |
| B | true  | 0.819032 | 0.784223 | 0.790234 | 0.007771 | 0.826803 |
| C | true  | 0.811915 | 0.751174 | 0.790234 | 0.051549 | 0.863464 |
| D | false | 0.788166 | 0.553166 | 0.790234 | 0.341938 | 1.130104 |
| E | true  | 0.823047 | 0.790234 | 0.790234 | 0.000000 | 0.823047 |

Additional v2 vs v1 deltas:
- `B`: `delta_fit = -0.034809`, `delta_acc = -0.035221` (closest non-zero-penalty regime).
- `C`: `delta_fit = -0.060741`, `delta_acc = -0.036328`.
- `E`: `delta_fit = -0.032813`, `delta_acc = -0.032813` (best raw delta but zero complexity pressure).

Roadmap criterion check:
- "At least one regime makes v2 mathematically feasible and empirically competitive."
- Feasibility is achieved in `B/C/E`; empirical competitiveness (v2 >= v1 on final max fitness/accuracy) is **not** achieved in any regime.

## Decision
1. Select **Regime B** as the canonical complexity regime for next experimental phases.
2. Keep regimes `C` and `E` as reference controls (secondary diagnostics), not canonical.
3. Keep legacy default CLI behavior unchanged in this task (`--complexity_regime` default stays `A`); default switch is a separate follow-up implementation task.

Rationale:
- `B` removes structural impossibility for `v2` (`feasible=true`) while preserving non-zero complexity pressure.
- Compared to `C`, `B` gives better v2 fitness trajectory and smaller v2-v1 gap.
- Compared to `E`, `B` avoids zero-penalty collapse into pure-accuracy optimization and preserves biology-motivated complexity tradeoff.

## Consequences
- Phase 2+ experiment specs should use regime `B` as canonical baseline for selection physics unless explicitly justified otherwise.
- Reported comparisons should continue to include `A` (legacy) and optionally `E` (no-penalty control) for interpretability.
- Since v2 is feasible but not yet empirically competitive, physics issue is partially resolved; further method/genome work remains required before claiming competitiveness.

## Rollback
- Governance rollback: revert this ADR (`git revert <commit-hash-with-ADR-0005>`).
- Operational rollback: run experiments with explicit `--complexity_regime A` until a superseding ADR is approved.
