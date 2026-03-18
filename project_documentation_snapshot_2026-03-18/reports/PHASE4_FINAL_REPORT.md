# PHASE4_FINAL_REPORT

## 1 Introduction
Phase 4 is closed with strict separation of verdict layers:
- **Scientific Track:** `RUN COMPLETE / GATE FAIL` (unchanged, ADR-0010/ADR-0012).
- **Applied Track:** practical GPU optimization stabilized and validated in a parallel governance lane (ADR-0013/ADR-0015).

## 2 Experimental Protocol
Reference profile lock:
- `profile_id = gpu_profile_v4_reference`
- `batch_size=8, steps=120, lr=3e-5, AMP=on, fp32_critical=on, clip=1`
- Locked in: `configs/profiles/gpu_profile_v4_reference.yaml`
- SHA256(parameters): `6aa623965a8937b82366258f64172333e350ceca774e2d582132b45390714e0b`

Paired metric:
- `delta_i = val_loss_baseline_i - val_loss_reference_i`
- CI calculated over seed-level deltas.

## 3 Reference Profile
The reference profile is frozen and registered in:
- `configs/profiles/gpu_profile_v4_reference.yaml`
- `configs/applied/gpu_profile_registry_v4.json`
Status is `reference_locked`; profile is immutable for this closure cycle.

## 4 Statistical Results
Gate-level paired aggregate (GPU v4 gate baseline vs optimized):
- `mean_delta = 1.3836773343`
- `CI95 = [0.9475860640, 1.8197686045]`
- `stability_fail_rate = 0.0`

Repro run (`results/repro_run`, N=30):
- `mean_delta = 1.3595809937`
- `CI95 = [0.9233480782, 1.7958139091]`
- `negative_seed_rate = 0.1666666667`

## 5 Robustness Metrics
Robustness metric introduced:
- `negative_seed_rate = N_negative / N`
- Current value: `5/30 = 0.1667`
- Negative seeds: `[1339, 1342, 1352, 1356, 1359]`

Standardized report payload is exported to:
- `reports/metrics.json`

## 6 Seed Failure Analysis
Forensic package is available:
- `analysis/seed_forensics/seed_1339.json`
- `analysis/seed_forensics/seed_1342.json`
- `analysis/seed_forensics/seed_1352.json`
- `analysis/seed_forensics/seed_1356.json`
- `analysis/seed_forensics/seed_1359.json`
- Summary: `reports/seed_failure_analysis.md`

Observed pattern:
- No runtime nondeterminism signature.
- Negative seeds show seed/protocol sensitivity with confidence-collapse behavior (high logits magnitude, low entropy windows).

## 7 Reproducibility Test
Repro run artifacts:
- `results/repro_run/per_seed_metrics.csv`
- `results/repro_run/aggregate_metrics.json`
- `results/repro_run/CI_report.md`

Criteria check:
- `CI95_low > 0` -> **PASS**
- `negative_seed_rate < 0.25` -> **PASS**

## 8 Conclusions
Scientific Track:
- Cooperative hypothesis remains **not confirmed** under scientific Phase-4 governance.

Applied Track:
- Locked GPU reference profile provides stable, reproducible uplift vs baseline in paired seed analysis.
- Practical profile closure is complete without changing scientific thresholds or scientific verdict.

## 9 Hardening Block (TASK-4700..5200)
- `TASK-4700`: immutable lock added for reference profile (`.lock` + guard script).
- `TASK-4800`: deterministic seed replay check passed (`1339, 1347, 1364`, tolerance `1e-6`).
- `TASK-4900`: environment snapshot + package fingerprint captured.
- `TASK-5000`: dataset immutability manifest + integrity checker added.
- `TASK-5100`: unified Phase-4 provenance ledger published.
- `TASK-5200`: isolated external reproducibility check completed; criteria passed (`CI95_low>0`, `negative_seed_rate<0.25`).
