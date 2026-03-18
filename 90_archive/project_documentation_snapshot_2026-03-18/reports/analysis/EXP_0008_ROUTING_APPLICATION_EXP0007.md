# EXP_0008 Routing Application — exp_0007 Phase-0 Evidence

Purpose
Apply Quaternary Router to exp_0007 evidence: generate deterministic CPU and GPU-acceleration queues and define routing gates.

Inputs
- exp_0007 analysis: reports/analysis/EXP_0007_PHASE0_FULLSWEEP_ANALYSIS.md
- Dead configs (pass_rate=0.0) list sourced from analysis doc

Queues
- CPU queue: QUEUES/exp0007_dead_configs_cpu_queue.jsonl
  - Intent: diagnose_kc1_region (CPU-only)
- GPU acceleration queue: QUEUES/acceleration_candidates_gpu_maybe_queue.jsonl
  - Intent: more_seeds_same_policy (acceleration-only; no logic changes)

Routing Rules (summary)
- Evidence-critical tasks → CPU YES, GPU NO.
- Acceleration-only tasks → CPU YES; GPU MAYBE_YES only if:
  - gpu_budget_ok == true
  - device_logging_ok == true
  - cpu_reference_exists == true

Runbook (deterministic)
1) Build queues
   python experiments/exp_0008_quaternary_router_skeleton/src/queue_builder.py --out_dir experiments/exp_0008_quaternary_router_skeleton/QUEUES
2) Route CPU queue
   python experiments/exp_0008_quaternary_router_skeleton/src/route_cli.py --in experiments/exp_0008_quaternary_router_skeleton/QUEUES/exp0007_dead_configs_cpu_queue.jsonl --mode queue --decision_log experiments/exp_0008_quaternary_router_skeleton/RESULTS/decisions_dead.jsonl
3) Route acceleration queue (dry run)
   python experiments/exp_0008_quaternary_router_skeleton/src/route_cli.py --in experiments/exp_0008_quaternary_router_skeleton/QUEUES/acceleration_candidates_gpu_maybe_queue.jsonl --mode queue --no_record

Notes
- Outputs are deterministic JSONL with sorted keys.
- No adaptive tuning; CPU remains authoritative.
