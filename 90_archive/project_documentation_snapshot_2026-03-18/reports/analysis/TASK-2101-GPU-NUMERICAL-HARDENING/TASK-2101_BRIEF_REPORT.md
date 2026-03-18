# TASK-2101 BRIEF REPORT

## Scope
- Harden GPU numeric path in `scripts/wiki_pilot/run_once.py` to prevent AMP false-positive crashes.
- Keep strict legacy behavior available via explicit CLI flag.
- Add tests for numeric guardrails and deterministic replay behavior.

## Changes
- Updated `scripts/wiki_pilot/run_once.py`:
  - Replaced fragile hard assert in softmax sum check with dtype-aware numeric audit (`numeric_sum_tolerance`).
  - Added explicit finite-value guards for logits/probabilities/sums.
  - Added `--strict_numeric_asserts` flag (legacy strict behavior with `1e-5` tolerance).
  - Added `softmax_max_deviation` metric output and audit fields in diagnostic payload.
- Added tests:
  - `tests/test_exp0700_numeric_guardrails.py`

## Verification (L0)
- Command: `python -m py_compile scripts/wiki_pilot/run_once.py tests/test_exp0700_numeric_guardrails.py`
- Result: PASS

- Command: `pytest -q tests/test_exp0700_numeric_guardrails.py`
- Result: PASS
- Output summary: `4 passed`.

- Command: `python scripts/wiki_pilot/run_once.py --dataset_root D:/datasets/bdc/simplified_wiki_v0/20260201/full_build --out_dir results/.tmp_task2101_seed1337_amp --seed 1337 --steps 80 --batch_size 12 --seq_len 128 --d_model 128 --nhead 4 --num_layers 2 --dim_ff 256 --device cuda --gpu_mem_soft_limit_gb 9.0 --use_amp`
- Result: PASS
- Output summary: run completes without softmax assertion crash.

- Command: `python scripts/wiki_pilot/run_once.py --dataset_root D:/datasets/bdc/simplified_wiki_v0/20260201/full_build --out_dir results/.tmp_task2101_seed1337_amp_strict --seed 1337 --steps 80 --batch_size 12 --seq_len 128 --d_model 128 --nhead 4 --num_layers 2 --dim_ff 256 --device cuda --gpu_mem_soft_limit_gb 9.0 --use_amp --strict_numeric_asserts`
- Result: PASS (expected strict failure)
- Output summary: deterministic strict assertion reproduced with max deviation diagnostics.

## Artifacts
- `scripts/wiki_pilot/run_once.py` - numeric guardrail hardening + strict flag.
- `tests/test_exp0700_numeric_guardrails.py` - guardrail and determinism tests.
- `reports/analysis/TASK-2101-GPU-NUMERICAL-HARDENING/TASK-2101_BRIEF_REPORT.md` - task report.

## Risks / Limitations
- Strict mode remains intentionally incompatible with FP16 drift and is expected to fail under AMP; this is debug-only behavior.
- Guardrails stop on non-finite tensors, but root numerical quality still depends on model/training hyperparameters.

## Rollback
- Revert with: `git revert <TASK-2101_commit_hash>`
