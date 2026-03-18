# TASK-0110 Post-Outage Verification Report

- timestamp_utc: 2026-01-28 06:50:23 UTC
- branch: test
- head: 8cb41fc

## Repo State (L0)
- status: modified file: experiments/exp_0007_pistream_v3_phase0_sweep/REPORT_TEMPLATE.md
- TASK-0109 commits present: ce8072a, d1291a6, 8cb41fc

## Tests (V1)
- pytest -q: PASS (29 passed)

## Queue Determinism (V2)
- dead_queue_sha256: eeb839afc3582ac928edbbc9d56c15513328f8f7472aeddd5d34856ec744597f
- dead_queue_sha256_2: eeb839afc3582ac928edbbc9d56c15513328f8f7472aeddd5d34856ec744597f
- accel_queue_sha256: 53022dd861055daa89b7ffe5ceb3d25055b38cc3354a2cf6a4c5ad7739b0fad0
- accel_queue_sha256_2: 53022dd861055daa89b7ffe5ceb3d25055b38cc3354a2cf6a4c5ad7739b0fad0

## Queue Content (V3)
- dead_queue_lines: 11
- dead_configs: si128_clonal_init_k_point_mutation_k1p0, si128_clonal_init_k_point_mutation_k2p0, si128_clonal_init_k_point_mutation_k4p0, si128_clonal_init_per_locus_flip_p0p01, si128_clonal_init_per_locus_flip_p0p02, si128_clonal_init_per_locus_flip_p0p05, si64_clonal_init_k_point_mutation_k1p0, si64_clonal_init_k_point_mutation_k2p0, si64_clonal_init_per_locus_flip_p0p01, si64_clonal_init_per_locus_flip_p0p02, si64_clonal_init_per_locus_flip_p0p05
- accel_queue_lines: 5
- accel_task_types_sample: acceleration_only

## Decision Logs (V4)
- dead_bad_lines: 0
- accel_bad_lines: 0
- dead_sample_cpu/gpu: YES / NO
- accel_sample_cpu/gpu: YES / MAYBE_NO

## Verdict
- Ready to proceed with TASK-0109: PASS
- Ready to proceed beyond TASK-0109: PASS
