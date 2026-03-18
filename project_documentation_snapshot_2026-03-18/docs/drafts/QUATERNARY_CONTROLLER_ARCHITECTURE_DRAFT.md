# QUATERNARY CONTROLLER/EXECUTOR ARCHITECTURE (DRAFT)

Status: DRAFT (not canonical)

Purpose
Define Controller vs Executor roles for Quaternary Logic routing with deterministic
decisions, evidence tracking, and auditability.

Roles
- Controller:
  - Accepts task descriptors and evidence context.
  - Produces deterministic routing decisions (CPU/GPU).
  - Emits a decision record with hashes and rationale.
- Executor:
  - Executes routed task (CPU or GPU).
  - Logs execution metadata and outputs.
  - Does not change routing policy.

Inputs
Task Descriptor (json-like dict):
- task_type (e.g., evidence_analysis, acceleration, hypothesis_eval)
- priority (low/med/high)
- requires_evidence (bool)
- acceleration_allowed (bool)
- tags (list)

Evidence Context:
- exp_0007_analysis_present (bool)
- exp_0007_metrics_sha256 (str)
- exp_0007_summary_sha256 (str)
- analysis_doc_path (str)
- commit_hash (str)

Outputs
Decision:
- cpu_decision: YES/NO
- gpu_decision: MAYBE_YES/MAYBE_NO/YES/NO
- gates_required: list
- rationale: string
- evidence_refs: dict

Decision Record Schema (append-only)
```
{
  "timestamp_utc": "...",
  "controller_commit": "...",
  "task_descriptor": {...},
  "evidence_context": {...},
  "decision": {...},
  "run_hashes": {
    "metrics_sha256": "...",
    "summary_sha256": "..."
  },
  "executor_plan": {
    "device": "cpu|gpu",
    "budget": "...",
    "replication": 2
  }
}
```

Logging & Auditing
- Controller logs every decision with hashes.
- Executor logs device info, runtime, and determinism checks.
- Failures are recorded as ABORTED with reason; no deletions.

Determinism Rules
- No random routing; decision is pure function of inputs.
- JSON serialization with sorted keys is used for deterministic output bytes.

Notes
- Infra success is isolated from cognitive claims.
- No adaptive tuning in Controller; policy only.
