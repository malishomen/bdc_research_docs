# BDC Packet Prep Final Corrective Checklist

## Purpose

This is the **last preparatory step** before the Cockpit case can be honestly sent to `BDC Designer`.

Current state:
- packet structure exists,
- architecture reading exists,
- variants inventory exists,
- but measured evidence is still missing.

So the goal of this checklist is **not** to redesign Cockpit.

The goal is:
- fill the packet with measured runtime truth,
- remove `UNKNOWN` / `MISSING` / `NOT_MEASURED_YET` from the critical evidence surfaces,
- and end the cycle with a packet that can be honestly run through `BDC Designer`.

## Current Blockers

These are the blockers visible in the current packet:

1. `02_RUNTIME_TRUTH.json`
- commit truth is `UNKNOWN`

2. `05_SLICE_METRICS.csv`
- all critical slices are `NOT_MEASURED_YET`

3. `07_RAW_EVIDENCE_MANIFEST.md`
- raw evidence is `MISSING`

4. `08_DESIGN_PRIORITIES.md`
- still `OWNER_INPUT_REQUIRED`

5. `10_BDC_PACKET_READINESS_SUMMARY.md`
- correctly says `NO`

## Non-Negotiable Rule

Do **not** start a new architecture discussion in this cycle.

Do **not** add new major features first.

Do **not** widen scope into:
- SDK migration,
- agent teams,
- new persistence models,
- new UI layers,
- MCP expansion.

This cycle is only for:
- measurement,
- trace capture,
- packet correction,
- final readiness check.

## One-Cycle Mission

At the end of this cycle, the packet must support a truthful answer:
- `send_to_bdc_now = yes`

If that is still not honest, the cycle is incomplete.

## Target Output Folder

Use the existing packet folder and finish it in place.

Working root:
- `D:\projects\Bio_Digital_Core\Designer\Agent_Studio\IN\BDC_PACKET_PREP_EXTRACTED\BDC_PACKET_PREP`

Add a new evidence subfolder:
- `D:\projects\Bio_Digital_Core\Designer\Agent_Studio\IN\BDC_PACKET_PREP_EXTRACTED\BDC_PACKET_PREP\RAW_EVIDENCE`

## Required Deliverables For This Final Prep Cycle

You must finish all of the following.

### 1. Freeze runtime truth

Update:
- `02_RUNTIME_TRUTH.json`

Required fields that must no longer be `UNKNOWN`:
- `measured_commit`
- `current_head_deployed_commit`
- `packet_state_commit`

Also confirm with explicit values:
- `exact_cli_invocation_command`
- `current_execution_mode`
- `follow_up_behavior`
- `session_completion_rule`
- `stdin_close`

Rule:
- every field must come from a real file, command, or runtime observation
- not from assumption

### 2. Run one bounded measured audit cycle

Perform a real Cockpit runtime audit on the current implementation.

Minimum run set:

1. **New session run** x3
- create project/session
- send first request
- wait for completion

2. **Follow-up run** x3
- send follow-up to an existing UI session
- observe whether context is preserved or lost

3. **Path validation run** x3
- one valid path
- one invalid path
- one edge-case path

4. **End-to-end real task run** x3
- a real coding task that causes:
  - stream text
  - at least one tool call
  - at least one tool result
  - final completion

5. **Reload / reconnect run** x3
- reload browser or reconnect WS during or after session
- record what survives and what does not

If permission flow is actually reachable in the current system:
- add **Permission round-trip run** x3

If permission flow is not reachable:
- mark it explicitly as `NOT_IMPLEMENTED_IN_CURRENT_RUNTIME`
- with evidence

### 3. Capture raw evidence artifacts

Under:
- `RAW_EVIDENCE`

Create at minimum:

#### A. Session traces
- `session_trace_01.jsonl`
- `session_trace_02.jsonl`
- `session_trace_03.jsonl`

Each should contain a full ordered event trail if available.

At least one trace must show:
- `session_create`
- `session_created`
- first `stream_text`
- `tool_use`
- `tool_result`
- `session_status(done)`
- `session_ended`

#### B. Backend logs
- `backend_log_01.txt`
- `backend_log_02.txt`

#### C. CLI stdout samples
- `cli_stdout_01.jsonl`
- `cli_stdout_02.jsonl`

#### D. WebSocket payload capture
- `ws_trace_01.json`
- `ws_trace_02.json`

#### E. Screenshots
- `step_01_create.png`
- `step_02_stream.png`
- `step_03_tool_use.png`
- `step_04_completion.png`
- `step_05_follow_up.png`
- `step_06_reload_or_reconnect.png`

#### F. Commands log
- `commands_run.md`

This file must record:
- exact commands
- exact order
- important outputs

### 4. Replace placeholder slice metrics with measured values

Update:
- `05_SLICE_METRICS.csv`

The following slices must have **real numeric values**, not placeholders:
- `new_session_success`
- `session_created_ack_latency`
- `first_visible_token_latency`
- `follow_up_success`
- `session_completion`
- `stdout_json_parse_integrity`
- `tool_event_pairing_integrity`
- `project_path_validation`
- `end_to_end_real_task_completion`

The following slices may remain non-successful, but must still be **explicitly measured or explicitly marked not implemented with evidence**:
- `permission_round_trip`
- `session_recovery_after_reload`
- `ws_reconnect_recovery`
- `browse_flow_success`

For required measured slices, these fields must be numeric:
- `attempts`
- `success_count`
- `failure_count`
- `median_latency_ms`
- `p95_latency_ms`
- `timeout_count`
- `manual_intervention_count`
- `disconnect_count`
- `dropped_event_count`
- `mismatched_event_pair_count`

Allowed values:
- real numbers / integers
- or `0`

Not allowed for required measured slices:
- `UNKNOWN`
- `NOT_MEASURED_YET`
- `NO_DATA`

### 5. Upgrade failure registry from inferred to measured

Update:
- `06_FAILURE_REGISTRY.md`

For each listed failure, add:
- `observed_in_measured_run = yes/no`
- `occurrence_count`
- `evidence_path`

Replace vague markers like:
- `MISSING`
- `UNKNOWN`

with one of:
- `OBSERVED_IN_MEASURED_RUN`
- `NOT_OBSERVED_IN_MEASURED_RUN`
- `NOT_IMPLEMENTED_IN_CURRENT_RUNTIME`

### 6. Replace raw evidence manifest with actual files

Update:
- `07_RAW_EVIDENCE_MANIFEST.md`

It must no longer say:
- `MISSING`

Instead it must list:
- each actual file under `RAW_EVIDENCE`
- what it proves
- which slice(s) it supports

### 7. Resolve design priorities with owner input

Update:
- `08_DESIGN_PRIORITIES.md`

This file is blocking.

You must resolve it with explicit owner-confirmed priorities.

At minimum rank:
- reliability
- latency
- operator continuity
- safe file actions
- auditability
- session persistence
- multi-session support

If the owner cannot answer immediately, the cycle is **not finished**.

Do not leave:
- `OWNER_INPUT_REQUIRED`

### 8. Update packet readiness summary honestly

Update:
- `10_BDC_PACKET_READINESS_SUMMARY.md`

It must answer:
- what is ready
- what is partially ready
- what is still missing
- `Can we send to BDC now?`

The correct target for this cycle is:
- `YES`

But only if the actual readiness criteria below are met.

## Final Readiness Gate

You may change the final summary to `YES` only if all of the following are true:

1. `02_RUNTIME_TRUTH.json`
- no critical commit fields are `UNKNOWN`

2. `05_SLICE_METRICS.csv`
- all required core slices have measured numeric values

3. `07_RAW_EVIDENCE_MANIFEST.md`
- references actual files that exist

4. `08_DESIGN_PRIORITIES.md`
- owner priorities are explicitly filled

5. At least one full-cycle trace exists
- from `session_create` through `session_ended`

6. `04_TESTED_VARIANTS.csv`
- still may include unmeasured variants,
- but current primary implemented path must be explicitly marked and evidenced

If any of those are false:
- do **not** mark the packet ready

## Final Self-Check Before Sending

Run these checks on the final packet:

### Check 1 — No unresolved placeholders in critical files
Search these files:
- `02_RUNTIME_TRUTH.json`
- `05_SLICE_METRICS.csv`
- `07_RAW_EVIDENCE_MANIFEST.md`
- `08_DESIGN_PRIORITIES.md`
- `10_BDC_PACKET_READINESS_SUMMARY.md`

Forbidden unresolved markers:
- `UNKNOWN`
- `MISSING`
- `NOT_MEASURED_YET`

Exception:
- allowed only in explicitly non-critical narrative notes,
- not in required fields

### Check 2 — Raw evidence files exist
Every file listed in:
- `07_RAW_EVIDENCE_MANIFEST.md`

must exist on disk.

### Check 3 — Core slices are numeric
Required slices in:
- `05_SLICE_METRICS.csv`

must not contain placeholders.

### Check 4 — Final summary says `YES` only if gate is satisfied
No optimistic wording.
No “almost ready”.

Either:
- `YES`
or
- `NO`

## Packaging Rule

When all checks pass:

Create final archive:
- `D:\projects\Bio_Digital_Core\Designer\Agent_Studio\OUT\BDC_PACKET_READY.zip`

Include:
- completed packet folder
- `RAW_EVIDENCE`
- final summary

Do not send the current `prep` zip again.

## Final Deliverable Expected From The Team

At the end of this cycle, the team should send exactly:

1. `BDC_PACKET_READY.zip`
2. a short note with:
   - `packet_ready = yes`
   - `measured_commit = ...`
   - `main_runtime_risk = ...`
   - `main_observed_failure = ...`
   - `send_to_bdc_now = yes`

## One-Line Rule

**No more architecture speculation, no more prep-only placeholders: fill the packet with measured runtime truth once, and make this the final preparation cycle before the real `BDC Designer` run.**
