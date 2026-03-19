# BDC Designer Native Contract Fix For Cockpit

## Mission
Convert the already measured Cockpit packet into a **native `BDC Designer` intake packet** without running a new measurement cycle.

This is a **contract-alignment pass only**.
Do not reopen architecture discussion.
Do not collect a new evidence round unless a required field is truly absent.

## Why The Last Run Still Failed
The packet was measured enough for an honest run, but `BDC Designer` still returned:
- `supported = false`
- `recommended_variant_id = null`
- `selective_outcome_class = abstain_need_more_evidence`

The reason was not empty metrics.
The reason was that the intake registry did not bind the current files to the native contract.
Everything stayed in `extras`, so the bundle saw:
- no `README.md`
- no native packet JSON
- no `unified_variant_comparison.csv`
- no `current_runtime_role_mapping.csv`
- no `current_slice_metrics.csv`
- no `failure_case_registry.csv`
- no `prompt_stage_matrix.csv`
- no `lead_architect_design_priorities.md`

## Required Final Folder Shape
The final folder must contain these exact files at top level:

1. `README.md`
2. `BDC_INPUT_PACKET_COCKPIT_RUNTIME_AUDIT.json`
3. `unified_variant_comparison.csv`
4. `current_runtime_role_mapping.csv`
5. `current_slice_metrics.csv`
6. `failure_case_registry.csv`
7. `prompt_stage_matrix.csv`
8. `lead_architect_design_priorities.md`

Keep these as supporting files:
- `RAW_EVIDENCE/`
- `runtime_truth.json`
- `open_gaps_and_missing_data.md`
- `bdc_packet_readiness_summary.md`

## Exact Source -> Target Remap

### 1. README
Create:
- `README.md`

Source:
- `01_WORKFLOW_DESCRIPTOR.md`
- `10_BDC_PACKET_READINESS_SUMMARY.md`

Required content:
- system name: `Cockpit`
- audit scope: current runtime / current orchestration truth
- runtime mode: `claude --print --output-format stream-json`
- current known strengths
- current known failures
- allowed interpretation: runtime/orchestration audit, not enterprise future-state claim

### 2. Native packet JSON
Create:
- `BDC_INPUT_PACKET_COCKPIT_RUNTIME_AUDIT.json`

Source:
- `01_WORKFLOW_DESCRIPTOR.md`
- `02_RUNTIME_TRUTH.json`
- `03_CURRENT_ARCHITECTURE_MAPPING.md`
- `08_DESIGN_PRIORITIES.md`
- `09_OPEN_GAPS_AND_MISSING_DATA.md`

Minimum fields to include:
- `schema_version`
- `case_id`
- `system_name`
- `task_type`
- `workflow_summary`
- `primary_objective`
- `functional_decomposition`
- `hard_constraints`
- `soft_constraints`
- `candidate_roles`
- `tested_variants`
- `quality_targets`
- `risk_map`
- `metadata.runtime_truth`

Recommended task type:
- `current_runtime_logical_redesign_decision`

### 3. Unified variant comparison
Create:
- `unified_variant_comparison.csv`

Source:
- `04_TESTED_VARIANTS.csv`
- `05_SLICE_METRICS.csv`
- `06_FAILURE_REGISTRY.md`

Required header:
```csv
variant_id,architecture_type,role_set,runtime_type,docs_improved_pct,naturalness_delta,semantic_pass_pct,runtime_min,cost_usd,llm_calls,revert_rate_pct,gate_pass_rate_pct,useful_rewrite_rate_pct,evidence_status,notes
```

Minimum variants to include:
1. `print_single_turn`
2. `resume_flow`
3. `interactive_flow`
4. `normalized_event_relay`
5. `multi_client_broadcast`

Rule:
- if a variant is not implemented, keep it in the CSV but mark evidence honestly as `missing` or `inferred_only`
- do not leave the table empty

### 4. Current runtime role mapping
Create:
- `current_runtime_role_mapping.csv`

Source:
- `03_CURRENT_ARCHITECTURE_MAPPING.md`

Required header:
```csv
runtime_component,logical_bdc_role,status,why_mapped_this_way
```

Minimum rows expected:
- websocket/session intake -> `orchestrator`
- session_manager -> `planner`
- cli_runner subprocess execution -> `editor`
- permission bridge / completion / file action bounding -> `guardian`

### 5. Current slice metrics
Create:
- `current_slice_metrics.csv`

Source:
- `05_SLICE_METRICS.csv`

The current file is measured, but not in native schema.
You must reshape it into a variant-centered table.

Required header:
```csv
variant_id,slice_id,accepted_rewrite_rate,revert_rate,no_op_rate,semantic_pass_proxy,useful_output_rate,latency,cost,evidence_status,notes
```

Minimum required rows:
- rows for `print_single_turn`
- rows for `normalized_event_relay`
- rows for `multi_client_broadcast`
- rows for failure slices like reconnect loss if they affect the variant

Important:
- `session_recovery_after_reload = 0/3` and `ws_reconnect_recovery = 0/3` must appear as real negative evidence
- do not hide failures by averaging them away

### 6. Failure case registry
Create:
- `failure_case_registry.csv`

Source:
- `06_FAILURE_REGISTRY.md`

Required header:
```csv
case_id,failure_mode,severity,status,note
```

Minimum rows:
- `FOLLOW_UP_CONTEXT_LOSS`
- `PAGE_RELOAD_SESSION_LOSS`
- `WS_RECONNECT_STATE_LOSS`
- `INVALID_PROJECT_PATH_HANDLING`
- `PERMISSION_DEADLOCK` (if not observed, still list honestly)

### 7. Prompt / stage matrix
Create:
- `prompt_stage_matrix.csv`

Source:
- `01_WORKFLOW_DESCRIPTOR.md`
- `03_CURRENT_ARCHITECTURE_MAPPING.md`
- raw traces

Required header:
```csv
stage_id,stage_name,objective,measured_output,evidence_status
```

Minimum rows:
- `session_create`
- `session_created`
- `stream_text`
- `tool_use/tool_result relay`
- `session_completion`
- `follow_up_session_query`
- `reconnect_or_reload_behavior`

### 8. Design priorities
Create:
- `lead_architect_design_priorities.md`

Source:
- `08_DESIGN_PRIORITIES.md`

This can be a direct rename with light cleanup.

## Required Naming Cleanup For Existing Files
After creating native files, keep these supporting names too:
- `runtime_truth.json` from `02_RUNTIME_TRUTH.json`
- `open_gaps_and_missing_data.md` from `09_OPEN_GAPS_AND_MISSING_DATA.md`
- `bdc_packet_readiness_summary.md` from `10_BDC_PACKET_READINESS_SUMMARY.md`

## One Important Governance Note
`runtime_truth.json` may still state:
- `LOCAL_UNVERSIONED_WORKSPACE_NO_GIT`

This is weak governance, but it is no longer a native intake blocker by itself.
Do not invent git hashes.
Carry the local/unversioned truth honestly.

## Final Readiness Test
Before zipping, run the packet so that native intake must recognize:
- `README.md`
- packet JSON
- all 6 CSV files
- `lead_architect_design_priorities.md`

The target is that `intake_manifest.json` no longer shows these fields as `null`.

## Final Packaging Rule
When the folder is remapped, package it as:
- `BDC_PACKET_NATIVE_READY.zip`

Do not send the old packet again.
Do not send another prep packet.
The next packet should be the native-aligned measured packet.

## Final Success Condition
This cycle is successful only if:
1. the packet remains measured and honest;
2. all required native contract files exist;
3. the intake registry binds them as required inputs;
4. the next `BDC Designer` run is evaluating the packet itself, not failing at file discovery.
