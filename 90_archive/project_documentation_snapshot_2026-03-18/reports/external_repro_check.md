# External Reproducibility Check

## Objective
Validate Phase-4 reference profile reproducibility in an isolated external workspace.

## Constraints observed
- Direct external host execution was attempted via `ssh bdc@192.168.1.100` and failed (`Connection refused`).
- Fallback path used: clean independent clone on the same hardware host.

## External workspace
- Path: `D:/projects/Bio_Digital_Core/Bio_digital_core_external_repro_check_20260305_184524`
- Branch: `test`

## Command
```bash
python scripts/applied/run_phase4_repro_reference.py   --base_seed 1337 --seeds 30   --out_root results/external_repro_run   --baseline_root D:/projects/Bio_Digital_Core/Bio_digital_core/results/exp_0700_applied_v4_gpu_gate/gate/gpu/baseline   --profile_path configs/profiles/gpu_profile_v4_reference.yaml   --validation_interval 20
```

## Results
- `mean_delta = 1.3595809936523433`
- `ci95_low = 0.9233480782112988`
- `ci95_high = 1.7958139090933878`
- `negative_seed_rate = 0.16666666666666666`
- `pass = True`

## Criteria check
- `CI95_low > 0` -> PASS
- `negative_seed_rate < 0.25` -> PASS

## Comparison with local repro_run
- External and local aggregate values matched exactly at reported precision.
