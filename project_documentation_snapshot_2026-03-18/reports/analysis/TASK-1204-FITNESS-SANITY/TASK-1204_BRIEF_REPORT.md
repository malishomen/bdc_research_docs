# TASK-1204 BRIEF REPORT

## Scope
- Проверена корректность `fitness/accuracy` на hidden_rule baselines без изменения эволюционной логики.
- Все расчеты выполнены через canonical функцию `evaluate_genome` из `evolution/edp1_symbolic/evaluate.py`.

## Changes
- Добавлен скрипт:
  - `scripts/analysis/fitness_sanity_1204.py`
- Сформирован результат:
  - `reports/analysis/TASK-1204-FITNESS-SANITY/fitness_sanity_results.json`

## Verification (L0)
- Command:
  - `python scripts/analysis/fitness_sanity_1204.py --out reports/analysis/TASK-1204-FITNESS-SANITY/fitness_sanity_results.json`
- Result: PASS

## Baseline Acc/Fitness (hidden_rule, exhaustive 512, bit_len=9)
- `always_1`:
  - accuracy `0.677734375`
  - fitness `0.677734375`
- `always_0`:
  - accuracy `0.322265625`
  - fitness `0.322265625`
- `random_coinflip(seed=1337)`:
  - accuracy `0.521484375`
  - fitness `0.521484375`

## v1 always_1 imitation
- Genome: `threshold_count=0`, all weights `0`, `bias=1`
- accuracy `0.677734375`
- fitness `0.667734375`
- complexity penalty `0.01`

## v2 random genomes (n=100, seed fixed)
- Accuracy distribution:
  - mean `0.48541015625`
  - median `0.49609375`
  - CI95 `0.021258157885349963`
- Fitness distribution:
  - mean `0.2169342248735789`
  - median `0.22759967930037833`
  - CI95 `0.021233312470578917`

## Floor comparison (~0.53)
- Observed floor source:
  - `results/edp1_exp0200_v2/aggregates/metrics_agg.csv: final_max_fitness_mean`
  - value `0.5356865515715755`
- Delta vs random v2 fitness mean:
  - `+0.3187523266979966`

## Conclusion
- Observed v2 floor (`~0.53`) **does not match** random-v2 baseline fitness (`~0.217`).
- `evaluate/fitness` implementation appears **sane** for tested baselines:
  - trivial predictors behave as expected,
  - fitness penalty impact is consistent with complexity term,
  - no immediate evidence of formula bug from baseline checks.

## Artifacts
- `scripts/analysis/fitness_sanity_1204.py`
- `reports/analysis/TASK-1204-FITNESS-SANITY/fitness_sanity_results.json`
- `reports/analysis/TASK-1204-FITNESS-SANITY/TASK-1204_BRIEF_REPORT.md`

## Risks / Limitations
- This is a sanity pass, not a formal proof of global correctness for all regimes.
- Baseline random predictor is deterministic pseudo-random adapter over exhaustive data; it is suitable for reproducible reference but not for stochastic confidence across RNG seeds.

## Rollback
- Not required (analysis-only + additive artifacts).
