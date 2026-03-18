# TASK-1102B BRIEF REPORT

## Scope
- Added a speciation layer for Phase-1 selection: selection now happens within species instead of global population ranking.
- Preserved fitness function, mutation operator, and diversity-shock mechanism.
- Executed smoke verification and full validation run (`N=30`, `G=100`, `P=100`) for `shock+speciation`.

## Changes
- Added: `evolution/edp1_symbolic/speciation.py`
  - deterministic `genome_distance(genome_a, genome_b)`
  - deterministic greedy clustering with `distance_threshold`
  - species-size cap via split (`max_species_fraction`)
  - per-species selection function `phase1_speciated_selection(...)`
- Updated: `evolution/edp1_symbolic/run_generations.py`
  - global phase1 selection replaced by per-species selection
  - new CLI params:
    - `--speciation_distance_threshold` (default `3`)
    - `--max_species_fraction` (default `0.5`)
  - metrics extended with:
    - `species_count`
    - `largest_species_fraction`
  - diversity shock logic retained
- Updated: `scripts/edp1/run_edp1_sweep.sh`
  - added passthrough params for speciation

## Verification (L0)
- Smoke:
  - `bash scripts/edp1/run_edp1_local.sh --out_dir results/edp1_exp0200_speciation_smoke --generations 30 --population 50 --seed 1337 --diversity_shock_pct 0.2 --speciation_distance_threshold 3 --max_species_fraction 0.5`
  - Result: `PASS`
  - `species_count_min_max=8..15` (`>1` true), `largest_species_fraction_max=0.28` (`<=0.5` true)
- Full validation:
  - `N=30`, seeds `1337..1366`, `G=100`, `P=100`, `phase0_min_generations=10`, `mutation_rate=0.2`, `selection_top_pct_phase1=0.2`, `diversity_shock_pct=0.2`, `speciation_distance_threshold=3`, `max_species_fraction=0.5`
  - Aggregation:
    - `python scripts/edp1/aggregate_results.py --in results/edp1_exp0200_speciation --out results/edp1_exp0200_speciation/aggregates --phase0_generations 10`
  - Result: aggregate files produced (`PASS`).

## Required Comparison
- pass_rate:
  - baseline (`TASK-1101B`): `0.0`
  - shock (`TASK-1102A`): `0.0`
  - shock+speciation (`TASK-1102B`): `0.0`
- kill breakdown:
  - baseline: `plateau=28`, `trivial_strategy=2`
  - shock: `plateau=28`, `trivial_strategy=2`
  - shock+speciation: `plateau=30`, `trivial_strategy=0`
- plateau generation mean:
  - baseline: `30.892857`
  - shock: `100.0`
  - shock+speciation: `100.0`

## Species Metrics
- species_count trajectory mean:
  - g1 `17.30`
  - g10 `19.27`
  - g25 `10.37`
  - g50 `11.13`
  - g75 `11.73`
  - g100 `11.27`
- largest_species_fraction trajectory mean:
  - g1 `0.2043`
  - g10 `0.1780`
  - g25 `0.1687`
  - g50 `0.1743`
  - g75 `0.1733`
  - g100 `0.1803`
- constraints check:
  - `largest_species_fraction` overall max: `0.5` (respects `max_species_fraction=0.5`)

## Artifacts
- `results/edp1_exp0200_speciation/aggregates/metrics_agg.csv`
- `results/edp1_exp0200_speciation/aggregates/fitness_trajectory_agg.csv`
- `results/edp1_exp0200_speciation/aggregates/diversity_trajectory_agg.csv`
- `reports/analysis/TASK-1102B-SPECIATION/TASK-1102B_BRIEF_REPORT.md`

## Risks / Limitations
- With current kill-criteria evaluator, end-of-run plateau classification still yields global `FAIL` despite stable multi-species dynamics and full 100-generation completion.
- Species-cap is enforced by deterministic cluster splitting; this is an operational cap, not biological niche equilibrium.

## Rollback
- Revert commit for TASK-1102B to remove speciation layer and return to shock-only selection path.
