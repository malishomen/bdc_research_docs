# Runtime vs Aggregate Kill-Criteria Diff Analysis

## Scope
Сравнение логики PASS/FAIL между:
- Runtime: `evolution/edp1_symbolic/run_generations.py`
- Post-hoc aggregate: `scripts/edp1/aggregate_results.py`

## Source Locations
- Runtime параметры: `evolution/edp1_symbolic/run_generations.py:34`..`evolution/edp1_symbolic/run_generations.py:39`
- Runtime kill decisions: `evolution/edp1_symbolic/run_generations.py:170`..`evolution/edp1_symbolic/run_generations.py:203`
- Aggregate kill function: `scripts/edp1/aggregate_results.py:35`..`scripts/edp1/aggregate_results.py:82`

## Post-line Comparison

### 1) diversity_collapse
- Runtime:
  - condition: `div_idx < args.diversity_collapse_threshold`
  - patience: `args.diversity_collapse_patience`
  - fail when streak reaches patience.
- Aggregate:
  - hardcoded condition: `div < 0.15`
  - hardcoded patience: `>= 10`.
- Mismatch:
  - aggregate игнорирует runtime-параметры, использует фиксированные значения.

### 2) trivial_strategy
- Runtime:
  - streak increment on strict `triv_rate > args.trivial_strategy_threshold`
  - kill gate checks `triv_rate >= threshold` and `trivial_streak >= patience`.
- Aggregate:
  - streak increment on strict `triv > 0.80`
  - kill when `trivial_streak >= 5`.
- Mismatch:
  - aggregate hardcoded threshold/patience (`0.80`, `5`), не читает runtime params.
  - runtime использует двухэтапный gate (`>` для streak, `>=` для kill condition).

### 3) plateau
- Runtime:
  - active only in phase 1: `phase == 1`.
  - window length: `args.plateau_window + 1`.
  - improvement threshold: `args.plateau_improvement_pct`.
  - on low improvement:
    - if cooldown passed -> schedule diversity shock and continue;
    - else -> FAIL plateau.
- Aggregate:
  - phase1 starts on `(phase == 1 or gen > phase0_generations)`.
  - history length hardcoded: `>= 11`.
  - improvement threshold hardcoded: `< 0.01`.
  - on low improvement -> increments `plateau_streak`, FAIL at `>=1`.
  - shock reset only clears history if `diversity_shock_applied == 1`.
- Mismatch:
  - aggregate uses implicit phase switch by generation boundary, runtime uses explicit `phase`.
  - aggregate has hardcoded window/improvement constants.
  - runtime can avoid fail via scheduled shock before cooldown failure; aggregate does not model pending shock state.

### 4) PASS/FAIL source
- Runtime:
  - writes canonical `summary.json -> kill_status`.
- Aggregate:
  - recomputes status independently and discards runtime `kill_status` for pass_rate.
- Mismatch:
  - two competing truth sources produce contradictions (observed in TASK-1201).

## Exact Parameter Mismatches
- `plateau_window`: runtime configurable; aggregate fixed at 10 (via `len(max_fit_hist) >= 11`).
- `plateau_improvement_pct`: runtime configurable; aggregate fixed `0.01`.
- `diversity_collapse_threshold`: runtime configurable; aggregate fixed `0.15`.
- `diversity_collapse_patience`: runtime configurable; aggregate fixed `10`.
- `trivial_strategy_threshold`: runtime configurable; aggregate fixed `0.80`.
- `trivial_strategy_patience`: runtime configurable; aggregate fixed `5`.

## Conservativeness
Более консервативна aggregate-логика:
- plateau FAIL срабатывает сразу при первом окне low-improvement (`plateau_streak >= 1`),
- runtime при том же событии сначала может применить shock и продолжить run.

## Conclusion
Логика PASS/FAIL не унифицирована. Текущее пост-фактум пересчитывание в aggregate нарушает принцип единого источника истины.
