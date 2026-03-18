# TASK-0140 BRIEF REPORT — comprehension v0 progress policy + governed replicate runs + PASS/FAIL decision

Branch/HEAD (start): `test` @ `f94f1437473a29e980f3041ed82d86204874bfd7`

## What Changed (In Git)

- Policy: `docs/spec/COMPREHENSION_V0_PROGRESS_POLICY.md`
- Policy eval tool: `tools/analysis/exp0017_progress_policy_eval.py`
- Monitoring: `reports/analysis/TASK_0140_MONITORING_COMMANDS.md`

## Dataset Gate (KC_DATA_INTEGRITY)

dataset_root (external-only):
- `D:\datasets\bdc\simplified_wiki_v0\20260201\full_build`

docs.jsonl sha256:
- expected (derived manifest): `dbb3b1bce7864db98beef169ff81181daeaaf5382d7e85ed82fba025597ff687`
- actual:                    `dbb3b1bce7864db98beef169ff81181daeaaf5382d7e85ed82fba025597ff687`

Result: **PASS**.

## Governed Replicates (Same Config/Seed)

Runs (gitignored under `logs/`):
- `task0140_main1`: `logs/exp_0017_comprehension_v0_cloze/run_20260208T205032Z_f94f143_task0140_main1`
- `task0140_main2`: `logs/exp_0017_comprehension_v0_cloze/run_20260208T205851Z_f94f143_task0140_main2`

Command used (fixed-step replicate; deterministic):
```powershell
$root = "D:\datasets\bdc\simplified_wiki_v0\20260201\full_build"
python experiments/exp_0017_comprehension_v0_cloze/src/train.py --dataset_root $root --max_steps 3500 --seed 12345 --run_tag task0140_main1 --log_every 100 --eval_every 500
python experiments/exp_0017_comprehension_v0_cloze/src/train.py --dataset_root $root --max_steps 3500 --seed 12345 --run_tag task0140_main2 --log_every 100 --eval_every 500
```

Note: a 4-hour time-budget mode (`--time_budget_minutes 240`) is supported but was not used here because time-budgeted runs can stop at different step counts and break replicate comparability. See `reports/analysis/TASK_0140_MONITORING_COMMANDS.md`.

## Metrics (Final)

Both runs produced identical metrics:
- val_acc: `0.1491193309` (masked_total=118603, masked_correct=17686)
- test_acc: `0.1456512255` (masked_total=123782, masked_correct=18029)
- shuffled baseline val_acc: `0.0276468555`

## Policy Evaluation (PASS/FAIL)

Policy tool command:
```powershell
python tools/analysis/exp0017_progress_policy_eval.py `
  --runs_root logs/exp_0017_comprehension_v0_cloze `
  --run_tags task0140_main1 task0140_main2 `
  --require_integrity `
  --dataset_root D:\datasets\bdc\simplified_wiki_v0\20260201\full_build `
  --require_sanity
```

Result:
- **VERDICT: PASS** (exit code 0)

Key gates:
- KC_SANITY: PASS (model exceeds shuffled baseline by margin)
- KC_REPRO: PASS (val drift abs = 0.0 <= 0.01)
- KC_IMPROVEMENT vs TASK-0139 main: PASS (Δval_acc ≈ +0.0315 abs >= 0.02)

## Explicitly Not Committed

- No checkpoints, logits, or large logs committed (all run artifacts are under `logs/` and gitignored).

