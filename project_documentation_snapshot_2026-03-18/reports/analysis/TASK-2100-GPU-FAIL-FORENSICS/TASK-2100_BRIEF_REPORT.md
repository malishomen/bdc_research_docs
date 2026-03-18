# TASK-2100 BRIEF REPORT

## Scope
- Investigate GPU optimized diagnostic failures from `EXP-0700` (`N=10`, seeds `1337..1346`).
- Produce seed-level machine-readable evidence and ranked root-cause hypotheses.

## Changes
- Created forensic artifacts:
  - `reports/analysis/TASK-2100-GPU-FAIL-FORENSICS/gpu_failure_forensics_summary.json`
  - `reports/analysis/TASK-2100-GPU-FAIL-FORENSICS/gpu_failure_forensics_summary.csv`
- Added this report.

## Verification (L0)
- Command: `python -c "import json, pathlib; d=json.loads(pathlib.Path('results/exp_0700_applied/diagnostic/aggregates/run_index_v2.json').read_text(encoding='utf-8')); print(d['failure_count'], len(d['failures']))"`
- Result: PASS
- Output summary: `6 6` (all recorded failures are GPU optimized runs).

- Command: `python scripts/wiki_pilot/run_once.py --dataset_root D:/datasets/bdc/simplified_wiki_v0/20260201/full_build --out_dir results/.tmp_task2100_repro_seed1337 --seed 1337 --steps 80 --batch_size 12 --seq_len 128 --d_model 128 --nhead 4 --num_layers 2 --dim_ff 256 --device cuda --gpu_mem_soft_limit_gb 9.0 --use_amp`
- Result: PASS (for forensic reproduction)
- Output summary: deterministic crash reproduced with `AssertionError: softmax probabilities must sum to ~1`.

- Command: `python -c "import json, pathlib; d=json.loads(pathlib.Path('reports/analysis/TASK-2100-GPU-FAIL-FORENSICS/gpu_failure_forensics_summary.json').read_text(encoding='utf-8')); print(d['n_failures'], d['n_success'], d['root_cause_ranking'][0]['status'])"`
- Result: PASS
- Output summary: `6 4 confirmed`.

## Artifacts
- `reports/analysis/TASK-2100-GPU-FAIL-FORENSICS/gpu_failure_forensics_summary.json` - seed-level forensic rows and ranked hypotheses.
- `reports/analysis/TASK-2100-GPU-FAIL-FORENSICS/gpu_failure_forensics_summary.csv` - compact tabular seed-level forensic evidence.
- `reports/analysis/TASK-2100-GPU-FAIL-FORENSICS/TASK-2100_BRIEF_REPORT.md` - formal task summary.

## Risks / Limitations
- Reproduction confirms one dominant failure signature (`softmax_assert`) but does not by itself guarantee full numeric stability after fix.
- Temporary reproduction artifacts under `results/.tmp_task2100_*` are runtime-only and intentionally not versioned.

## Rollback
- Revert with: `git revert <TASK-2100_commit_hash>`
