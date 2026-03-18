# TASK-1002-STABILITY-PATCH BRIEF REPORT

## Scope
- Stabilize Wiki Pilot training while preserving determinism constraints.
- Keep seeds/deterministic flags/fp32/dropout/batch/seq unchanged.

## Changes
- `scripts/wiki_pilot/run_once.py`
  - default LR reduced `3e-4 -> 3e-5`.
  - added gradient clipping: `torch.nn.utils.clip_grad_norm_(model.parameters(), 1.0)`.
  - added linear warmup scheduler (`LinearWarmupScheduler`, 200 steps).
  - added per-step LR logging (`learning_rate` in `metrics.csv`).
  - added early `val_loss` NaN detection (`val_loss_nan_detected`) before entropy checks.
  - added per-step logits diagnostics (`logits_max`, `logits_min` in `metrics.csv`).
- `scripts/wiki_pilot/run_once.sh`
  - default LR updated to `3e-5`.

## Verification (L0)
- `rg -n "clip_grad_norm" scripts/wiki_pilot/` -> PASS
- `rg -n "warmup|LinearWarmupScheduler" scripts/wiki_pilot/` -> PASS
- `rg -n "3e-5" scripts/wiki_pilot/` -> PASS
- `python scripts/wiki_pilot/run_once.py --dry_run` -> PASS
- `python scripts/wiki_pilot/run_once.py --dry_run --out_dir results/wiki_pilot/run_2` -> PASS
- `python scripts/wiki_pilot/run_once.py --dry_run --out_dir results/wiki_pilot/run_3` -> PASS
- `python scripts/wiki_pilot/compare_runs.py --verify --root results/wiki_pilot` -> PASS

## Artifacts
- `scripts/wiki_pilot/run_once.py`
- `scripts/wiki_pilot/run_once.sh`
- `reports/analysis/TASK-1002-STABILITY-PATCH/TASK-1002-STABILITY-PATCH_BRIEF_REPORT.md`

## Risks / Limitations
- Full 2000-step stability is not proven by dry-run; requires separate 3x full run evidence.

## Rollback
- Revert commit for TASK-1002 and rerun dry-run verification.
