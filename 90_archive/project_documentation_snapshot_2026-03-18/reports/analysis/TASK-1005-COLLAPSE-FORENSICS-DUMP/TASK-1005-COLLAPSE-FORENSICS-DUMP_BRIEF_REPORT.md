# TASK-1005-COLLAPSE-FORENSICS-DUMP BRIEF REPORT

## Scope
- Collect L0 forensics around deterministic `entropy_collapse` without changing training behavior.
- Two identical forensic runs to validate rerun consistency.

## Commands Executed
- `python scripts/wiki_pilot/run_once.py --seed 1337 --steps 220 --out_dir results/wiki_pilot/run_forensics_220 --log_jsonl results/wiki_pilot/run_forensics_220/diag.jsonl --dump_batch 1 --dump_every 25`
- `python scripts/wiki_pilot/run_once.py --seed 1337 --steps 220 --out_dir results/wiki_pilot/run_forensics_220_rerun --log_jsonl results/wiki_pilot/run_forensics_220_rerun/diag.jsonl --dump_batch 1 --dump_every 25`
- `python scripts/wiki_pilot/compare_runs.py --verify --root results/wiki_pilot --include_runs run_forensics_220 run_forensics_220_rerun`
- `python scripts/wiki_pilot/generate_report.py`

## L0 Findings
- Collapse step/reason (both runs):
  - `step=200`, `reason=entropy_collapse`

- Top token in forensic dump batch (`step=25`, `dump_batch=1`):
  - `top1_token_id=612`
  - `top1_token_freq=0.04638671875`
  - `special_status=non_special`

- Special token shares in dump batch (`step=25`):
  - `pad=0.0`
  - `bos=0.000244140625`
  - `eos=0.000244140625`
  - `unk=0.0`

- Token-id bounds:
  - `max_token_id_in_batch=32760`
  - `vocab_size=32768`

- `mean_prob_max` and `mean_logits_std` trajectory (steps 25..200):
  - `25:  mean_prob_max=1.0,              mean_logits_std=51.462257385253906`
  - `50:  mean_prob_max=0.9999982118606567, mean_logits_std=51.048072814941406`
  - `75:  mean_prob_max=0.999778151512146,  mean_logits_std=50.086761474609375`
  - `100: mean_prob_max=0.9965909719467163, mean_logits_std=48.14091491699219`
  - `125: mean_prob_max=0.9924477934837341, mean_logits_std=48.368682861328125`
  - `150: mean_prob_max=0.9890545606613159, mean_logits_std=49.501033782958984`
  - `175: mean_prob_max=0.996746838092804,  mean_logits_std=49.54145431518555`
  - `200: mean_prob_max=0.9745372533798218, mean_logits_std=48.05051040649414`

- First 16 tokens (from dump batch, identical in both runs):
  - `input_ids_first16 = [25207, 612, 22265, 9739, 24896, 25137, 991, 30759, 7552, 14700, 5186, 17883, 22115, 7552, 29701, 14186]`
  - `labels_first16   = [612, 22265, 9739, 24896, 25137, 991, 30759, 7552, 14700, 5186, 17883, 22115, 7552, 29701, 14186, 10279]`
  - `pred_first16     = [25207, 612, 22265, 9739, 24896, 25137, 991, 30759, 7552, 14700, 5186, 17883, 22115, 7552, 29701, 14186]`

## Rerun Consistency
- `compare_runs.py --include_runs run_forensics_220 run_forensics_220_rerun` -> `PASS`
- Deterministic equality confirmed for key fields:
  - `train_loss`, `val_loss`, `perplexity`, `gradient_norm`, `token_entropy`, `repetition_rate` all deltas `0.0`
  - step counts identical: `200` and `200`

## Verification
- `results/wiki_pilot/run_forensics_220/diag.jsonl` exists: PASS
- `results/wiki_pilot/run_forensics_220_rerun/diag.jsonl` exists: PASS
- line count in `run_forensics_220/diag.jsonl`: `11`
- include-runs verification command: PASS

## Artifacts
- `results/wiki_pilot/run_forensics_220/metrics.csv`
- `results/wiki_pilot/run_forensics_220/kill_status.json`
- `results/wiki_pilot/run_forensics_220/diag.jsonl`
- `results/wiki_pilot/run_forensics_220_rerun/metrics.csv`
- `results/wiki_pilot/run_forensics_220_rerun/kill_status.json`
- `results/wiki_pilot/run_forensics_220_rerun/diag.jsonl`
- `reports/analysis/TASK-1005-COLLAPSE-FORENSICS-DUMP/TASK-1005-COLLAPSE-FORENSICS-DUMP_BRIEF_REPORT.md`

## Conclusion
- Entropy collapse is reproducible and deterministic at step 200 under unchanged training settings.
- Forensics dump is complete for pre-fail/at-fail trajectory and batch-level token/probability diagnostics.
