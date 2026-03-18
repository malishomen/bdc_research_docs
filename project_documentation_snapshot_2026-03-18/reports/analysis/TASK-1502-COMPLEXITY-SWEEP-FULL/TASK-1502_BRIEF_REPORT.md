# TASK-1502 BRIEF REPORT

## Scope
- Completed full Phase 1 exp_0300 sweep for hidden_rule laboratory line:
  - 5 complexity regimes (`A,B,C,D,E`) x 3 genomes (`v1,v1_5,v2`) = 15 configs.
  - Full scale target: `N=30`, `G=100`, `P=100`.
- Performed sweep analytics and produced governance decision `ADR-0005`.
- No changes to EDP1 runtime code, no changes to `KILL_CRITERIA.yaml`.
- Context references: `docs/project/project_main_doc.md`, `docs/project/project_roadmap.md`.

## Changes
- Created:
  - `decisions/ADR-0005-complexity-regime.md`
  - `reports/analysis/TASK-1502-COMPLEXITY-SWEEP-FULL/TASK-1502_BRIEF_REPORT.md`
- Produced runtime artifacts (not committed):
  - `results/edp1_exp0300_complexity/<regime>_<genome>/seeds/seed_<id>/...`
  - `results/edp1_exp0300_complexity/*/aggregates/*`
  - `results/edp1_exp0300_complexity_sweep/complexity_sweep_summary.json`
  - `results/edp1_exp0300_complexity_sweep/complexity_sweep_summary.csv`

## Verification (L0)
- Full sweep execution (first attempt):
  - `python scripts/edp1/run_complexity_sweep_1501.py --seeds 30 --generations 100 --population 100 --out_root results/edp1_exp0300_complexity --summary_out results/edp1_exp0300_complexity_sweep/complexity_sweep_summary.json`
  - Result: PARTIAL (environment timeout after ~4h; completed A/B and part of C).
- Resume execution for missing configs/seeds (batch loop):
  - `python -m evolution.edp1_symbolic.run_generations ... --complexity_regime <regime> --genome_version <genome> --seed <seed> --generations 100 --population 100`
  - Followed by per-config aggregation:
    - `python scripts/edp1/aggregate_results.py --in results/edp1_exp0300_complexity/<regime>_<genome> --out results/edp1_exp0300_complexity/<regime>_<genome>/aggregates --phase0_generations 10`
  - Result: PASS (all missing seeds recovered).
- Rebuild global sweep summary:
  - `python scripts/edp1/aggregate_results.py --sweep_root results/edp1_exp0300_complexity --sweep_summary_out results/edp1_exp0300_complexity_sweep/complexity_sweep_summary.json`
  - Result: PASS.
- Completeness check (15 configs x 30 seeds + required files):
  - `python -c "... check metrics.csv and summary.json for seed_1337..1366 in all 15 configs ..."`
  - Result: PASS (`FULL_15x30_OK`).
- Summary schema check:
  - `python -c "... parse complexity_sweep_summary.json and verify required fields for all 15 records ..."`
  - Result: PASS (`SUMMARY_SCHEMA_OK`).
- v2 sanity-check (manual recompute `required_accuracy_to_beat_v1`):
  - `python -c "... for regimes B and E compute v1.final_max_fitness_mean + v2.final_max_penalty_mean and compare to summary ..."`
  - Result: PASS (exact match, diff `0.0` for both).
- Smoke subset rerun (`1 regime x 1 genome x N=2, G=10`):
  - Two runs:
    - `python -m evolution.edp1_symbolic.run_generations --out_dir results/.tmp_task1502_subset/B_v2/seeds/seed_1337 --genome_version v2 --seed 1337 --generations 10 --population 100 --complexity_regime B`
    - `python -m evolution.edp1_symbolic.run_generations --out_dir results/.tmp_task1502_subset/B_v2/seeds/seed_1338 --genome_version v2 --seed 1338 --generations 10 --population 100 --complexity_regime B`
  - Aggregate + sweep:
    - `python scripts/edp1/aggregate_results.py --in results/.tmp_task1502_subset/B_v2 --out results/.tmp_task1502_subset/B_v2/aggregates --phase0_generations 10`
    - `python scripts/edp1/aggregate_results.py --sweep_root results/.tmp_task1502_subset --sweep_summary_out results/.tmp_task1502_subset/complexity_sweep_summary.json`
  - Result: PASS (`subset_records=1`, schema intact).

## Coverage Table (15 configs)
- `A_v1: N=30`
- `A_v1_5: N=30`
- `A_v2: N=30`
- `B_v1: N=30`
- `B_v1_5: N=30`
- `B_v2: N=30`
- `C_v1: N=30`
- `C_v1_5: N=30`
- `C_v2: N=30`
- `D_v1: N=30`
- `D_v1_5: N=30`
- `D_v2: N=30`
- `E_v1: N=30`
- `E_v1_5: N=30`
- `E_v2: N=30`

## Key Results
From `results/edp1_exp0300_complexity_sweep/complexity_sweep_summary.json`:
- `v2 feasibility_flag`:
  - `A=false`, `B=true`, `C=true`, `D=false`, `E=true`.
- `required_accuracy_to_beat_v1` for `v2`:
  - `A=1.130103976076135` (not feasible)
  - `B=0.8268034167037162`
  - `C=0.8634642169608048`
  - `D=1.130103976076135` (not feasible)
  - `E=0.823046875`
- `v2 final_max_accuracy_mean = 0.790234375` (constant across regimes).
- `v2 final_max_fitness_mean`:
  - `A=0.5531664379938884`
  - `B=0.7842233238562164`
  - `C=0.7511739270082675`
  - `D=0.5531664379938884`
  - `E=0.790234375`.

## Scientific Conclusion
- Phase-1 feasibility objective is **partially met**: at least one regime (`B/C/E`) makes `v2` mathematically feasible.
- Roadmap strict criterion ("feasible and empirically competitive") is **NOT fully met**:
  - `v2` does not outperform `v1` on final max fitness or final max accuracy in any regime.
- Recommended canonical regime: **B** (see `ADR-0005`):
  - Feasible for `v2`.
  - Preserves non-zero complexity pressure.
  - Better v2-v1 fitness gap than `C`, avoids zero-penalty degeneracy of `E`.

## Artifacts
- `decisions/ADR-0005-complexity-regime.md`
- `reports/analysis/TASK-1502-COMPLEXITY-SWEEP-FULL/TASK-1502_BRIEF_REPORT.md`
- `results/edp1_exp0300_complexity_sweep/complexity_sweep_summary.json` (runtime artifact, not in git)
- `results/edp1_exp0300_complexity_sweep/complexity_sweep_summary.csv` (runtime artifact, not in git)

## Risks / Limitations
- Very high runtime cost: full sweep required long batch execution and retry after timeout.
- Despite feasibility recovery under `B/C/E`, empirical competitiveness of `v2` vs `v1` remains unresolved.
- Decision in ADR-0005 does not flip CLI default; adoption of canonical regime in default runtime should be handled by dedicated follow-up task.

## Rollback
- Revert governance/report changes:
  - `git revert <TASK-1502-commit-hash>`
- Runtime rollback remains explicit CLI usage:
  - `--complexity_regime A`
