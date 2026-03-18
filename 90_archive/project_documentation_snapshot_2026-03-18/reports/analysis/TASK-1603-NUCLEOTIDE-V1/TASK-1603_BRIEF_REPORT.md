# TASK-1603 BRIEF REPORT

## Scope
- Implemented `ClozeGenome v1` nucleotide architecture (`A/T/G + backbone logic`) in `evolution/cloze_symbolic`.
- Added Fibonacci hashing utilities and diagnostic uniformity checks.
- Added phi-scaled mutation + golden-section selection defaults for v1.
- Added v1 sweep runner and oracle checks.
- Preserved v0 compatibility (`--genome_version v0` path unchanged in outputs).

## Changes
- `docs/CLOZE_GENOME_SPEC.md`
  - Added full v1 nucleotide architecture spec, quaternary mapping, scoring, phi/golden params.
- `evolution/cloze_symbolic/fibonacci.py`
  - `fibonacci_hash_pair`, `xor_hash_pair`, chi-square utilities, hash comparison, acid discrimination.
- `evolution/cloze_symbolic/genome.py`
  - Added `ClozeGenomeV1`.
  - Added `acid_contributions`, `conflict_flag`, `bigram_oracle`.
  - Kept v0 `ClozeGenome` intact.
- `evolution/cloze_symbolic/evaluate.py`
  - Auto-dispatch v0/v1.
  - Added v1 candidate scoring via hash tables.
  - Added conflict/discrimination fields to evaluation outputs.
- `evolution/cloze_symbolic/mutate.py`
  - Added v1 init/mutation (`random_genome_v1`, `mutate_genome_v1`) with phi scaling.
  - Added apoptosis mutation path and constants.
- `evolution/cloze_symbolic/select.py`
  - Added golden defaults for v1 and acid-health-aware mutation flow.
- `evolution/cloze_symbolic/run_generations.py`
  - Added CLI: `--genome_version v0|v1`, `--hash_mode`, `--prev_hash_size`, `--next_hash_size`.
  - v1 defaults: `top_k=5`, golden selection, phi mutation.
  - Added metrics: `conflict_flag_rate`, acid discrimination, `apoptosis_events`.
  - v0 defaults preserved (`top_k=16`, `sigma=0.20`, `elite/survivor=0.2/0.5`).
- `scripts/edp1/run_cloze_v1_nucleotide_sweep.py`
  - Runs v1 4-config sweep (`hard|soft` x `top_k=5|8`), oracle checks, hash stats, XOR comparison.
- `docs/experiments/EXP-0400_CLOZE_EVOLUTION_2026-02-27.md`
  - Added section: `Nucleotide Architecture v1 (TASK-1603)`.
- Added runtime diagnostic artifact:
  - `reports/analysis/TASK-1603-NUCLEOTIDE-V1/apoptosis_smoke.json`

## Verification (L0)
- v0 backcompat:
  - `python scripts/edp1/run_cloze_exp_0400.py --smoke --seeds 2 --generations 5 --population 20 --out_root results/.tmp_task1603_v0_backcompat2`
  - Result: PASS (seed_1337 `final_max_accuracy=0.024883359253499222`, unchanged from TASK-1602 baseline).
- Dead params removed in v1:
  - `ClozeGenomeV1` has no `w_position`, `w_prev_match`, `w_next_match`.
  - Result: PASS.
- v1 smoke:
  - `python -m evolution.cloze_symbolic.run_generations --out_dir results/.tmp_task1603_v1_smoke/seed_1337 --genome_version v1 --top_k_tokens 5 --seed 1337 --generations 10 --population 20`
  - Result: PASS (finite metrics, `0 < conflict_flag_rate < 1`).
- Fibonacci hash distribution:
  - from `results/.tmp_task1603_sweep/aggregates/sweep_summary.json` (table_size=8):
    - Fibonacci `p=0.3074 > 0.05`
    - XOR `p=0.0794`
    - Fibonacci better than XOR in this test.
  - Result: PASS (for primary table size used by Acid_T).
- Bigram oracle check:
  - `prev_hash_size=8`: `abs_delta=0.05568`
  - fallback `prev_hash_size=13`: `abs_delta=0.05630`
  - Result: FAIL (`abs_delta` not `<0.02`, and remains `>0.05`).
- Sweep:
  - `python scripts/edp1/run_cloze_v1_nucleotide_sweep.py --seeds 3 --generations 30 --population 50 --subset_size 20 --out_root results/.tmp_task1603_sweep`
  - Result: PASS (all 4 configs completed + XOR control).
- No touch check:
  - `git diff --name-only | rg "evolution/edp1_symbolic"`
  - Result: PASS (no matches).

## Results Summary
- Best v1 config by final binary accuracy:
  - `hard_topk8`: `final_max_accuracy_mean = 0.05267`
- Against baselines:
  - vs frequency: positive in all configs
  - vs bigram: negative in all configs (none beats bigram)
- v1 vs v0:
  - v0 best reference (TASK-1602): `0.04427`
  - v1 best: `0.05267`
  - delta: `+0.00840` (below target `+0.02`)
- conflict flag:
  - high but finite in best config (`0.99916`)
- apoptosis:
  - mechanism unit-smoke PASS (`apoptosis_smoke.json`)
  - sweep activation criterion FAIL (`apoptosis_events_total = 0` in current sweep)

## Success / Kill Criteria Mapping
- `bigram_oracle delta < 0.02`: FAIL
- `any v1 config beats bigram`: FAIL
- `v1 improvement over v0 > +0.02`: FAIL
- `fibonacci better than xor by chi-square test`: PASS (table size 8)
- `conflict_flag_rate` non-degenerate:
  - mixed; one config reaches `1.0` mean exactly (degenerate), best config remains `<1.0`.

Overall TASK-1603 status: **FAIL against stated success criteria**.

## Recommendations
- Move to follow-up `TASK-1603b`:
  - add `Acid_C` (higher-order context / trigram-like channel),
  - add learnable backbone gates to reduce conflict saturation,
  - revisit oracle construction (hash-bucket loss indicates representational compression bottleneck).
- Keep v1 code path as experimental baseline (do not promote to default).

## Artifacts
- `docs/CLOZE_GENOME_SPEC.md`
- `evolution/cloze_symbolic/fibonacci.py`
- `evolution/cloze_symbolic/genome.py`
- `evolution/cloze_symbolic/evaluate.py`
- `evolution/cloze_symbolic/mutate.py`
- `evolution/cloze_symbolic/select.py`
- `evolution/cloze_symbolic/run_generations.py`
- `scripts/edp1/run_cloze_v1_nucleotide_sweep.py`
- `docs/experiments/EXP-0400_CLOZE_EVOLUTION_2026-02-27.md`
- `reports/analysis/TASK-1603-NUCLEOTIDE-V1/TASK-1603_BRIEF_REPORT.md`
- `reports/analysis/TASK-1603-NUCLEOTIDE-V1/apoptosis_smoke.json`

## Rollback
- `git revert <TASK-1603-commit-hash>`
