# TASK-5200 BRIEF REPORT

## Scope
- Validate reproducibility in an isolated external workspace and report PASS/FAIL criteria.

## Changes
- Added external check report:
  - `reports/external_repro_check.md`

## Verification (L0)
- Command: `ssh -o BatchMode=yes -o ConnectTimeout=8 bdc@192.168.1.100 "hostname"`
- Result: FAIL (connection refused)
- Command: external fallback run in clean clone:
  - `python scripts/applied/run_phase4_repro_reference.py --base_seed 1337 --seeds 30 --out_root results/external_repro_run --baseline_root D:/projects/Bio_Digital_Core/Bio_digital_core/results/exp_0700_applied_v4_gpu_gate/gate/gpu/baseline --profile_path configs/profiles/gpu_profile_v4_reference.yaml --validation_interval 20`
- Result: PASS
- Output summary: `ci95_low=0.9233480782`, `negative_seed_rate=0.1666666667`, `pass=true`.

## Artifacts
- `reports/external_repro_check.md`

## Risks / Limitations
- Independent-machine check was blocked by remote connectivity; executed fallback in isolated clean clone on same hardware host.

## Rollback
- `git revert <commit_hash>`
