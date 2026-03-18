# TASK-1200 BRIEF REPORT

## Scope
- Implemented Genome v2 (MRTN): `K=4` LTF sub-rules + 16-bit truth table.
- Preserved deterministic behavior and kept Genome v1 available.
- Integrated v2 into existing EDP1 runtime/speciation/metrics flow.

## Changes
- `evolution/edp1_symbolic/genome.py`
  - Added `LTFSubrule`.
  - Added `MultiRuleGenome` (`genome_version="v2"`), with truth-table composition.
- `evolution/edp1_symbolic/mutate.py`
  - `random_genome(..., genome_version={v1,v2})`.
  - `mutate_genome` supports:
    - Gaussian mutation for continuous params,
    - bit-flip for v2 truth table.
- `evolution/edp1_symbolic/evaluate.py`
  - Added `predict_v2`.
  - Existing eval path supports v1/v2 via shared `predict` interface.
- `evolution/edp1_symbolic/speciation.py`
  - `genome_distance` now supports:
    - v1: existing coarse threshold distance,
    - v2: `L2(weights) + Hamming(truth_table)`.
  - `phase1_speciated_selection` passes truth-table flip prob.
- `evolution/edp1_symbolic/run_generations.py`
  - Added CLI: `--genome_version {v1,v2}`.
  - Added `genome_version` to `metrics.csv`.
  - Diversity shock and random immigrants now respect selected genome version.
  - Summary now includes `genome_version`.
- `scripts/edp1/run_edp1_sweep.sh`
  - Added `--genome_version` passthrough.
- `evolution/edp1_symbolic/__init__.py`
  - Exported `LTFSubrule` and `MultiRuleGenome`.

## Verification (L0)
- Tests:
  - `pytest scripts/wiki_pilot/tests/`
  - Result: `PASS` (10 passed).
- Smoke run (v2):
  - `bash scripts/edp1/run_edp1_local.sh --out_dir results/edp1_exp0200_v2_smoke --genome_version v2 --generations 20 --population 50 --seed 1337 --phase0_min_generations 10 --mutation_rate 0.2 --selection_top_pct_phase1 0.2 --diversity_shock_pct 0.2 --speciation_distance_threshold 3 --max_species_fraction 0.5`
  - Result: `PASS`.
- Metric checks on smoke:
  - `functional_diversity <= 1.0`: `PASS` (`max=1.0`)
  - `species_count > 1`: `PASS` (min/max `50/50`)
  - `largest_species_fraction <= 0.5`: `PASS` (`max=0.02`)
  - `metrics.csv` includes `genome_version`: `PASS` (`v2`)
- Deterministic replay check:
  - Two identical v2 runs with same seed (`results/edp1_exp0200_v2_replay_a` and `_b`)
  - `metrics.csv` SHA256 equal: `PASS`
  - `summary.json` equal after normalizing `finished_at_utc` and `out_dir`: `PASS`

## Artifacts
- `reports/analysis/TASK-1200-MRTN/TASK-1200_BRIEF_REPORT.md`

## Risks / Limitations
- No separate EDP1 unit-test suite exists yet; verification relies on runtime smoke + deterministic replay checks.

## Rollback
- Revert this commit to return to v1-only runtime behavior.
