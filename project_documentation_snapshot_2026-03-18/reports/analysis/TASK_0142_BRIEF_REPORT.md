# TASK-0142 BRIEF REPORT — 6-hour governed exp_0017 run on simplified_wiki_v0 (integrity gate + monitoring; logs gitignored)

Branch/HEAD: `test` @ `ebf32b3bc3a64d29711a47c5f4a9ec38f80c5113`

## Integrity Gate (Required)

Dataset root (external-only):
- `D:\datasets\bdc\simplified_wiki_v0\20260201\full_build`

Integrity check:
- `KC_DATA_INTEGRITY: PASS` (docs.jsonl sha256 matches `datasets/simplified_wiki_v0/DERIVED_MANIFEST.json`)

## Run Launched (6h Budget)

Monitoring runbook:
- `reports/analysis/TASK_0142_MONITORING_COMMANDS.md`

Run tag:
- `task0142_6h`

Run dir (gitignored):
- `logs/exp_0017_comprehension_v0_cloze/run_20260208T215517Z_ebf32b3_task0142_6h`

CUDA evidence (from `RUN_METADATA.json`):
- `torch_cuda_available=true`
- `torch_cuda_device_name="NVIDIA GeForce GTX 1080 Ti"`
- `device="cuda"`

Command:
```powershell
python experiments/exp_0017_comprehension_v0_cloze/src/train.py `
  --dataset_root D:\datasets\bdc\simplified_wiki_v0\20260201\full_build `
  --max_steps 999999 `
  --time_budget_minutes 360 `
  --seed 12345 `
  --run_tag task0142_6h `
  --log_every 200 `
  --eval_every 1000
```

## Status

- **RUNNING** (launched in background; results will be written under the run dir above).
- After completion: inspect `metrics.json` and run policy evaluation (optional single-run mode) per `reports/analysis/TASK_0142_MONITORING_COMMANDS.md`.

