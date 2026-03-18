# TASK-0144 BRIEF REPORT — governed 2-hour exp_0017 run (io-tuned) + monitoring + integrity + policy

Branch/HEAD: `test` @ `9708fecb84eccc9b2418a1e26820945bbc2a0cc5`

## Run

- run_tag: `task0144_quality_2h_io`
- dataset_root (external-only): `D:\datasets\bdc\simplified_wiki_v0\20260201\full_build`
- seed: `12345`
- device: `cuda`

Command (stdout/stderr tee’d):
```powershell
$root = "D:\datasets\bdc\simplified_wiki_v0\20260201\full_build"
python experiments/exp_0017_comprehension_v0_cloze/src/train.py `
  --dataset_root $root `
  --device cuda `
  --seed 12345 `
  --time_budget_minutes 120 `
  --max_steps 100000000 `
  --eval_every 1000 `
  --eval_max_docs 2000 `
  --log_every 200 `
  --batch_size 32 `
  --num_workers 4 `
  --pin_memory `
  --prefetch_factor 2 `
  --persistent_workers `
  --run_tag task0144_quality_2h_io
```

Monitoring/runbook:
- `reports/analysis/TASK_0144_MONITORING_COMMANDS.md`

Launcher + GPU util logs (gitignored):
- launcher log: `logs/exp_0017_comprehension_v0_cloze/_launchers/launcher_20260209T075956Z_task0144_quality_2h_io.log`
- nvidia-smi csv (5s): `logs/exp_0017_comprehension_v0_cloze/_launchers/nvidia_smi_20260209T075956Z_task0144_quality_2h_io.csv`

Run outputs (gitignored):
- run_dir: `logs/exp_0017_comprehension_v0_cloze/run_20260209T075959Z_9708fec_task0144_quality_2h_io`

## Gates

Dataset integrity (pre-run):
- `KC_DATA_INTEGRITY: PASS`

Artifact integrity:
```powershell
python tools/analysis/exp0017_artifact_integrity_check.py `
  --run_dir logs/exp_0017_comprehension_v0_cloze/run_20260209T075959Z_9708fec_task0144_quality_2h_io `
  --hash
```
Result: PASS (`INTEGRITY_EXIT_CODE=0`).

Policy eval:
```powershell
python tools/analysis/exp0017_progress_policy_eval.py `
  --runs_root logs/exp_0017_comprehension_v0_cloze `
  --run_tags task0144_quality_2h_io `
  --require_integrity `
  --dataset_root D:\datasets\bdc\simplified_wiki_v0\20260201\full_build `
  --require_sanity
```
Result: `exit_code=0` / `VERDICT: PASS`.

## Outcome (metrics.json excerpt)

- completion: `TIME_BUDGET_REACHED step=91000 budget_minutes=120`
- final_step: `91001`
- val: acc=`0.5346070504` (k=`63406`, n=`118603`), loss=`3.0943933426`
- test: acc=`0.5134025949` (k=`63550`, n=`123782`), loss=`3.2469025292`
- baselines (val):
  - shuffled acc=`0.0276468555`
  - random acc=`0.0000927464`
- verdict_kc_sanity: `PASS`

## Artifact Hashes (sha256)

- `RUN_METADATA.json`: `050c14d81259d5457bb5cdff36cab247bda7b3ff4d805751873beb605884e053`
- `RUN_STATUS.json`: `5d62ce6228cde6b1a02c3edce6fe88d3ed92d50905c91db5a5ac482c0218d484`
- `metrics_by_step.jsonl`: `12f39ef40212021bb83a6d6d1b9b26093cf203744105d536083df1cc98e86567`
- `metrics.json`: `0354495bd2099596cb1009c3c4cc06e8e080e7a781eaa2cd6762cad77353fc3c`

## GPU Utilization Summary (nvidia-smi csv)

From `nvidia_smi_...csv` (samples=1423, 5s cadence):
- gpu_util min: `0`
- gpu_util p50: `57`
- gpu_util mean: `53.58`
- gpu_util max: `76`

## Explicitly Not Committed

- No raw run artifacts under `logs/exp_0017_comprehension_v0_cloze/**` committed (gitignored).
- No external dataset files committed.

