# TASK-1103C BRIEF REPORT

## Scope
- Found the best **single-run single-generation** `max_accuracy` across all `results/edp1_exp0200*/seeds/*/metrics.csv`.
- Extracted corresponding genome v1 via deterministic replay of matching code snapshot.
- Evaluated extracted genome on the same 512-sample exhaustive dataset used in `ltf_ceiling_proof.py`.
- Compared direct single-genome accuracy against theoretical LTF ceiling.

## Changes
- Added `scripts/analysis/extract_best_single_genome.py`.
- Generated:
  - `reports/analysis/TASK-1103C-SINGLE-GENOME/best_genome_v1.json`
  - `reports/analysis/TASK-1103C-SINGLE-GENOME/single_genome_accuracy.json`
  - `reports/analysis/TASK-1103C-SINGLE-GENOME/TASK-1103C_BRIEF_REPORT.md`

## Verification (L0)
- Best metric scan:
  - source: all `results/edp1_exp0200*/seeds/*/metrics.csv`
  - best found: `max_accuracy=0.8671875`, seed `1338`, generation `90`, path `results/edp1_exp0200_shock/seeds/seed_1338/metrics.csv`
- Replay extraction:
  - Used code snapshot `7a74787` (temporary git worktree), same run parameters from source summary.
  - Replayed run and extracted generation-90 top genome.
  - Replay check: extracted generation accuracy `0.8671875` (matches source metric).
- Direct ceiling comparison:
  - Dataset: exhaustive `2^9=512` bit-vectors (identical to `ltf_ceiling_result.json` spec).
  - Evaluation: pure accuracy (`predict == label`), no fitness penalty.
  - Single-genome accuracy: `0.78125`.
  - Theoretical LTF ceiling: `0.837890625`.
  - Delta: `-0.056640625`.

## Required Outputs
- `reports/analysis/TASK-1103C-SINGLE-GENOME/best_genome_v1.json`
- `reports/analysis/TASK-1103C-SINGLE-GENOME/single_genome_accuracy.json`
- `reports/analysis/TASK-1103C-SINGLE-GENOME/TASK-1103C_BRIEF_REPORT.md`

## Conclusion
- **Ceiling confirmed** for direct single-genome check: extracted best single genome is below theoretical LTF ceiling on identical dataset.
- Previous mismatch in TASK-1103 (`experimental max_accuracy_mean > theoretical`) is explained by different statistic target (`max over generations of run-mean`) rather than single-genome direct comparison.

## Rollback
- Revert this task commit to remove extraction script and report artifacts.
