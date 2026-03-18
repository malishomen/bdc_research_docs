# EXP_0011 QUATERNARY SCHEDULING REPORT

## Evidence Basis
- exp_0011 smoke report: reports/analysis/EXP_0011_VNEXT_SMOKE_REPORT.md
- exp_0011 smoke pointer: experiments/exp_0011_pistream_v3_phase0_vnext_kc1_ttt/RESULTS/LATEST_POINTER.md

## Decision
- Full sweep for exp_0011 is **deferred** in this task.
- Next steps are scheduled via Quaternary queues: KC2 diagnostics (CPU) and optional acceleration-only (GPU MAYBE).

## Queues
- KC2 diagnostics CPU queue: experiments/exp_0008_quaternary_router_skeleton/QUEUES/exp0011_kc2_diagnostics_cpu_queue.jsonl
  - sha256: ab100ee8403222390696c27ed90a05094a3bbfeb0f6e71f17cc1c75af33b9da2
  - tasks: 11 (dead configs)
- Accel candidates queue: experiments/exp_0008_quaternary_router_skeleton/QUEUES/exp0011_accel_candidates_gpu_maybe_queue.jsonl
  - sha256: 7a306a6ef9bbf7cd40532c31b9fad14b0a2526dc90540d06e0a45f3694d9802c
  - tasks: 2 (controls from exp_0011 smoke)

## Routing (REDO logs)
- decisions_exp0011_kc2_REDO.jsonl: CPU YES, GPU NO (evidence-critical)
- decisions_exp0011_accel_REDO.jsonl: CPU YES, GPU MAYBE_NO (gates missing)

## GPU Gates
- GPU promotion requires: gpu_budget_ok + device_logging_ok + cpu_reference_exists.
- Current accel tasks keep gates false (MAYBE_NO).
