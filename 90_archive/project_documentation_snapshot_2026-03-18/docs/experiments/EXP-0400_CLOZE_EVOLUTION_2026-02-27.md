# EXP-0400: Cloze Evolution on simplified_wiki_v0 (2026-02-27)

## Background

Phase 2 in `docs/project/project_roadmap.md` requires bridging evolution with a real wiki-derived task instead of toy `hidden_rule`.

This experiment introduces `evolution/cloze_symbolic/` as a separate module and uses deterministic cloze evaluation on a subset of `simplified_wiki_v0`.

Complexity physics is fixed to canonical regime **B** from `decisions/ADR-0005-complexity-regime.md`.

## Hypotheses & Relation to CANON/ADR

- H-0400-1: symbolic evolution can improve cloze fitness over generations on deterministic wiki subset.
- H-0400-2: evolved strategies can outperform baseline predictors.
- Governance relation:
  - ADR-0004: hidden_rule stays lab-only and untouched.
  - ADR-0005: regime B (`mean(|w|)`) is canonical for Phase 2+.

## Protocol

- Engine: `python -m evolution.cloze_symbolic.run_generations`
- Sweep wrapper: `python scripts/edp1/run_cloze_exp_0400.py`
- Data:
  - source: `D:/datasets/bdc/simplified_wiki_v0/20260201/full_build/docs.jsonl`
  - deterministic subset via stream-derived seed (`ENV_PISTREAM`)
  - cloze masking with `mask_rate=0.15`, `mask_salt=comprehension_v0_cloze_mask_v1`
- Genome:
  - `ClozeGenome v0` from `docs/CLOZE_GENOME_SPEC.md`
  - interpretable scalar weights + top-K token biases
- Fitness decomposition:
  - `accuracy`
  - `complexity = mean(|w|)` (regime B)
  - `penalty = lambda * complexity` (`lambda=0.01`)
  - `fitness = accuracy - penalty`

Run status in TASK-1600:
- Smoke executed: `N=2, G=5, P=20`
- Full canonical run target: `N=30, G=50, P=100` (follow-up required)

## Results

Smoke summary (`results/.tmp_task1600_cloze_smoke/aggregates/summary.json`):

| Metric | Value |
|---|---:|
| complexity_regime | B |
| seed_count | 2 |
| final_max_accuracy_mean | 0.026509 |
| final_max_fitness_mean | 0.021698 |
| final_max_complexity_mean | 0.626641 |
| final_max_penalty_mean | 0.006266 |
| best_baseline_accuracy_mean | 0.161516 |
| meets_5pct_gain_flag | false |

Per-seed baseline snapshot:

| Seed | random | frequency | constant | bigram | best baseline | evolved max acc |
|---:|---:|---:|---:|---:|---:|---:|
| 1337 | 0.011198 | 0.023017 | 0.000311 | 0.151166 | 0.151166 | 0.024883 |
| 1338 | 0.013293 | 0.027217 | 0.000306 | 0.171865 | 0.171865 | 0.028135 |

## Interpretation

- Positive signal:
  - fitness slope in smoke is positive for both seeds.
  - module is operational and deterministic with full metric decomposition.
- Negative signal:
  - evolved max accuracy is well below best baseline (bigram) in smoke.
  - 5% absolute gain criterion is not met.

Current conclusion:
- Phase 2 implementation is functional, but scientific success criteria are not yet met on smoke evidence.
- Full `N=30, G=50, P=100` execution is required before final PASS/FAIL declaration for Phase 2.

## Diagnostic Addendum (TASK-1601)

Source artifact:
- `reports/analysis/TASK-1601-CLOZE-DIAGNOSTIC/diagnostic_results.json`

### 1) Smoke trajectory diagnostics (L0)

Generation-level `max_accuracy_mean` across smoke seeds:

| Generation | max_accuracy_mean |
|---:|---:|
| 1 | 0.025436 |
| 2 | 0.025436 |
| 3 | 0.025436 |
| 4 | 0.025592 |
| 5 | 0.026509 |

Key ratios (means):
- `final_max_accuracy_mean = 0.026509`
- `best_baseline_accuracy_mean = 0.161516`
- `ratio_evo_to_best_baseline_mean = 0.164155` (about 16.4% of best baseline)
- `random_observed_accuracy_mean = 0.014161`
- `random_expected_uniform_topk = 0.0625` (`1/16`)
- `ratio_evo_to_random_mean = 1.93254`

Interpretation:
- Evo signal is above observed random baseline, but far below strongest baseline (bigram).
- Trajectory is nearly flat in early generations and remains in low-accuracy regime.

### 2) Representational capacity check (frequency oracle)

`ClozeGenome.frequency_oracle(top_k_tokens, strength=10.0)` was evaluated directly (no GA):

| Seed | oracle_accuracy | frequency_baseline_accuracy | abs_delta |
|---:|---:|---:|---:|
| 1337 | 0.023017 | 0.023017 | 0.0 |
| 1338 | 0.024465 | 0.024465 | 0.0 |

Result:
- `representational_defect_flag = false` for frequency baseline.
- ClozeGenome v0 can exactly realize frequency strategy; failure is not due to inability to encode that baseline.

### 3) Mini search-dynamics (simplified scenario)

Simplified diagnostic scenario:
- `subset_size=20`, `vocab_size=128`, `top_k_tokens=8`
- `N=1`, `G=50`, `P=20`
- `complexity_lambda=0.001`
- two starts: `random_init` and `oracle_init` (near frequency oracle).

Results:

| Series | start max_acc | end max_acc | start max_fit | end max_fit | slope(acc) | slope(fit) |
|---|---:|---:|---:|---:|---|---|
| random_init | 0.046425 | 0.051068 | 0.045893 | 0.050839 | + | + |
| oracle_init | 0.045032 | 0.051068 | 0.044176 | 0.050587 | + | + |

Reference baseline in same mini-task:
- `best_baseline_accuracy = 0.116992` (bigram), still well above evolved maxima.

### Addendum conclusion

- Limiter profile for current Phase 2 is **not** a hard representational defect for frequency baseline.
- Main bottleneck is combined:
  - search dynamics provide only modest gains,
  - task setup/baseline strength (especially bigram) leaves a large accuracy gap.
- Before full expensive run, recommended next step is targeted R1:
  - improve genome expressivity toward contextual heuristics beyond frequency,
  - or redesign mutation/selection for better exploration around context-sensitive solutions,
  - and evaluate sensitivity to task setup (`top_k`, vocab size, subset complexity).

## Search Signal Fix (TASK-1602)

Controlled sweep (`N=3, G=30, P=50`) over:
- `fitness_mode in {hard, soft}`
- `top_k_tokens in {4, 16}`

Sweep artifact:
- `results/.tmp_task1602_sweep/aggregates/sweep_summary.json`

| config | final_max_accuracy_mean | vs frequency_baseline | vs bigram_baseline | trajectory_slope_mean |
|---|---:|---:|---:|---:|
| hard_topk4 | 0.044267 | +0.016806 | -0.040392 | +0.004877 |
| hard_topk16 | 0.042739 | +0.015279 | -0.130085 | +0.013369 |
| soft_topk4 | 0.041810 | +0.014349 | -0.042849 | +0.006853 |
| soft_topk16 | 0.039975 | +0.012514 | -0.132849 | +0.011665 |

Observed decision from sweep:
- `at_least_one_meets_frequency = true` (all four configs meet it in mean).
- Best by `final_max_accuracy_mean`: **hard_topk4**.
- All configs keep positive trajectory slope.

Interpretation:
- Dimensionality reduction (`top_k=4`) is a stronger lever than switching to soft fitness in this sweep.
- Soft fitness improves `soft_accuracy` signal, but did not yield best binary accuracy under current operators.
- Bigram baseline remains unbeaten in all tested configs.

Recommended Phase 2 gate configuration:
- Use `top_k=4` as minimum viable configuration for next gate-scale run.
- Keep `fitness_mode` configurable; prefer `hard` for binary-accuracy target unless future sweeps show soft advantage.

## Nucleotide Architecture v1 (TASK-1603)

v1 introduced:
- 3-acid decomposition (`A/T/G`) + backbone-style additive integration.
- Fibonacci-hashed context tables (`prev:8`, `next:5`) and optional XOR control.
- Golden selection defaults (`elite=0.382`, `survivor=0.618`) for v1.
- phi-scaled mutation (`Acid_A < Acid_T < Acid_G`).
- conflict flag and acid-discrimination telemetry.

Diagnostic sweep (`N=3, G=30, P=50`, subset_size=20):

| config | final_max_accuracy_mean | vs frequency | vs bigram | trajectory_slope_mean | conflict_flag_rate_mean |
|---|---:|---:|---:|---:|---:|
| hard_topk5 | 0.046166 | +0.018706 | -0.049472 | +0.003395 | 0.996796 |
| hard_topk8 | 0.052668 | +0.023393 | -0.075580 | +0.006032 | 0.999158 |
| soft_topk5 | 0.052432 | +0.023174 | -0.049039 | +0.000763 | 0.999479 |
| soft_topk8 | 0.046675 | +0.017417 | -0.087485 | +0.001221 | 1.000000 |

Oracle/representation checks:
- Bigram oracle (`prev_hash=8`): `abs_delta = 0.05568` vs bigram baseline (FAIL).
- Escalation (`prev_hash=13`): `abs_delta = 0.05630` (FAIL, no recovery).

Hash distribution check:
- table_size=8:
  - Fibonacci `p=0.3074`
  - XOR `p=0.0794`
  - Fibonacci distribution quality is better in this test.

Acid contribution proxy (means, best config `hard_topk8`):
- `A_mean ~ 1.566`
- `T_mean ~ 1.934`
- `G_mean ~ 1.123`

Outcome classification:
- v1 does not beat bigram in any tested config.
- v1 improvement over v0 best (`0.04427`) is only `+0.00840` (below +0.02 target).
- Phase-2 v1 attempt is **FAIL** against TASK-1603 success criteria; next step is v1.5/v2 design or R2 pivot.

## Sensor Architecture v2 (TASK-1604)

Core change:
- switched from hashed context tables to pre-computed sensor features:
  - forward bigram sensor `P(candidate | prev)` proxy
  - reverse-bigram sensor `P(next | candidate)` proxy
  - frequency sensor retained.

Oracle checks (must be exact):
- bigram oracle delta: `0.0`
- frequency oracle delta: `0.0`

Diagnostic sweep (`N=3, G=30, P=50`, subset_size=20):

| config | final_max_accuracy_mean | vs frequency | vs bigram | trajectory_slope_mean | mean w_bigram |
|---|---:|---:|---:|---:|---:|
| hard_topk5 | 0.110306 | +0.081047 | +0.008835 | +0.014969 | 0.593803 |
| hard_topk8 | 0.153567 | +0.124308 | +0.019407 | +0.039193 | 1.630987 |
| soft_topk5 | 0.108296 | +0.079037 | +0.006825 | +0.048541 | 2.456531 |
| soft_topk8 | 0.151505 | +0.122246 | +0.017345 | +0.081445 | 3.082169 |

v2 outcome:
- at least one config beats bigram baseline: **YES** (all 4 configs in this sweep).
- best config: `hard_topk8`.
- improvement over v1 best (`0.052668`): `+0.100899`.

Interpretation:
- sensor integration removes the v1 hash compression failure mode.
- evolution learns positive bigram usage (`w_bigram > 0`) while combining reverse-bigram and frequency channels.

## Phase 2 Gate Run (TASK-1605)

Canonical gate configuration:
- `genome_version=v2`
- `fitness_mode=hard`
- `top_k_tokens=8`
- `N=30 seeds`, `G=50`, `P=100`, `subset_size=100`

Methodological correction applied:
- Criterion 1 is evaluated on per-seed deltas:
  - `delta_i = final_max_accuracy_i - baseline_i`
  - PASS requires `lower_CI95(delta) >= 0.05`.

Gate summary (`results/edp1_exp0400_cloze_v2_gate/aggregates/phase2_gate_summary.json`):
- `final_max_accuracy_mean = 0.116008` (95% CI `[0.113367, 0.118648]`)
- `best_baseline_mean = 0.092264` (95% CI `[0.089753, 0.094774]`)
- `delta_mean = 0.023744` (95% CI `[0.022390, 0.025098]`)
- `functional_diversity_final_mean = 0.998333`
- `trajectory_slope_mean (acc g50-g1) = 0.033716`

Criteria verdict:
- Criterion 1 (`lower_CI95(delta) >= 0.05`): **FAIL** (`0.022390 < 0.05`)
- Criterion 2 (positive slope in >=27/30): **PASS** (`30/30`)
- Criterion 3 (diversity >0.3 in >=27/30): **PASS** (`30/30`)

Kill checks:
- none triggered (`0/4`).

Phase decision:
- **Phase 2 Gate = FAIL** due to criterion 1 not met, despite stable positive dynamics and high diversity.

## Sensor Enrichment Diagnostic (TASK-1606)

Goal:
- test whether adding 2nd-order skip sensors raises `delta = max_accuracy - bigram_baseline`,
- and whether `G=50` was under-converged.

Protocol:
- 4-arm sweep: `{3-sensor, 5-sensor} x {G=50, G=100}`
- fixed params: `v2`, `hard`, `top_k=8`, `P=100`, `subset_size=100`
- diagnostic sample for this run: `N=10` seeds (`1337..1346`).

Backcompat check (critical):
- `3-sensor G50 seed=1337` reproduces TASK-1605 exactly:
  - `final.max_accuracy = 0.11932108218478815`
  - `final.mean_accuracy = 0.11631955079122001`
  - `final.max_fitness = 0.11584000282565296`

Key diagnostics:
- bigram oracle with skip-capable code path still exact: `delta=0.0`
- skip sensor wiring test (`w_bigram=5`, `w_skip=5`) changes predictions vs pure bigram oracle (`315/1000` sample predictions differ).

Results (`results/edp1_exp0400_cloze_v2_enrichment/aggregates/enrichment_summary_t_ci.json`):

| arm | sensors | G | delta_mean | 95% CI(delta, t) | note |
|---|---|---:|---:|---:|---|
| arm_3s_G50 | 3-sensor | 50 | 0.025330 | [0.022968, 0.027692] | control |
| arm_5s_G50 | 5-sensor | 50 | 0.035708 | [0.032088, 0.039328] | +skip helps |
| arm_3s_G100 | 3-sensor | 100 | 0.025678 | [0.023292, 0.028064] | marginal G effect |
| arm_5s_G100 | 5-sensor | 100 | 0.035823 | [0.032309, 0.039337] | best mean delta |

Interpretation (diagnostic):
- strongest effect is sensor enrichment (`+~0.012 delta` vs 3-sensor).
- increasing generations 50 -> 100 gives marginal change at this setting.
- no arm reaches CI lower bound `>= 0.05`.

Current decision signal:
- decision matrix branch `D` at `N=10`: threshold not reached.
- implies current architecture/config still below formal gate margin; next decision is gate re-run variant vs ADR/R2 review.

## Impact on roadmap

- Enables Phase 2 execution path with explicit cloze genome spec and reproducible run tooling.
- Provides baseline-comparison instrumentation needed for gate decision.
- Does not modify hidden_rule engine or wiki LM training stack.

## Links to TASK reports + ADR

- `reports/analysis/TASK-1600-CLOZE-EVOLUTION/TASK-1600_BRIEF_REPORT.md`
- `reports/analysis/TASK-1601-CLOZE-DIAGNOSTIC/TASK-1601_BRIEF_REPORT.md`
- `reports/analysis/TASK-1602-CLOZE-SEARCH-FIX/TASK-1602_BRIEF_REPORT.md`
- `docs/CLOZE_GENOME_SPEC.md`
- `decisions/ADR-0005-complexity-regime.md`
- `docs/experiments/EXP-0300_COMPLEXITY_REGIME_SWEEP_2026-02-27.md`
