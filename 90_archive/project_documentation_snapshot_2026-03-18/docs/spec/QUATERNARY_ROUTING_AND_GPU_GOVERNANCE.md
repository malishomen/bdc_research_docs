# Quaternary Routing And GPU Governance (Router v2)

This document formalizes a quaternary decision policy and a GPU governance scaffold.

Non-negotiables:
- CPU is always authoritative.
- GPU (until equivalence is proven) is replicate-only and MUST NOT affect PASS/FAIL. In routing terms, GPU can be `MAYBE_YES` but never "authoritative YES".
- Existing experiment semantics must not be changed by the router; the router only routes and writes decisions.

## Statuses (Quaternary)

Router v2 uses these statuses:
- `YES`: proceed (CPU authoritative).
- `NO`: blocked (do not run).
- `MAYBE_YES`: allowed only as non-authoritative replicate (typically GPU replicate).
- `MAYBE_NO`: do not proceed yet; needs additional evidence or diagnostics before upgrading to `YES`.

Interpretation:
- `YES`/`NO` are used for CPU-authoritative work.
- `MAYBE_*` are primarily used for non-authoritative work items (GPU replicate, or "needs diagnostics" CPU items).

## Evidence Levels

Evidence levels describe how strong a claim is and what is required to upgrade it.

- `L0` (Local / unverified):
  - Single-run or limited-seed observation.
  - No cross-device equivalence evidence.
  - Suitable for `MAYBE_NO` and `MAYBE_YES` only.

- `L1` (Reproduced / bounded):
  - CPU evidence reproduced on >= 2 independent runs OR >= 30 seeds on a stable runner.
  - Sanity controls are verified in the same run set.
  - Suitable to upgrade `MAYBE_NO -> YES` for CPU tasks.

- `L2` (Contracted equivalence):
  - CPU evidence is stable AND GPU equivalence is demonstrated under an explicit equivalence contract (see below).
  - Suitable to upgrade GPU from `MAYBE_YES -> YES` for non-authoritative acceleration, if ever allowed by canon.

Promotion rules (minimum):
- CPU routing:
  - `MAYBE_NO -> YES` requires `L1` evidence relevant to the failure mode.
  - Any `SANITY_BROKEN` remains `NO` until sanity is restored.
- GPU routing:
  - GPU is `MAYBE_YES` replicate-only until `L2` is met (equivalence contract satisfied).
  - Without `L2`, GPU results are "do_not_merge_results": true, and cannot flip CPU PASS/FAIL.

## GPU Governance

### GPU replicate-only rule

If a task defines `gpu_command`, the GPU route is:
- `gpu_status = MAYBE_YES` only if:
  - the task explicitly marks replicate-only intent, and
  - `do_not_merge_results == true`, and
  - a comparison mechanism exists (`compare_script` or documented compare procedure).
- otherwise `gpu_status = MAYBE_NO`.

GPU MUST NOT be marked authoritative in any task. If `authoritativeness != CPU`, the router returns `status=NO`.

### Equivalence contract (for upgrading GPU beyond MAYBE_YES)

The equivalence contract must define:
- Same inputs: identical queue/config, seed set, generations, and all relevant hyperparameters.
- Same observables: named artifacts (e.g. `metrics.csv`, `summary.csv`) and the columns to compare.
- Comparison method: a script that checks equality or tolerance bounds and reports PASS/FAIL.
- Determinism constraints: clear rules for any non-determinism (allowed epsilons, tie-breaking).
- Merge policy: explicit statement that GPU artifacts are not merged unless contract PASSes and governance says so.

The router does not enforce numerical equivalence; it only enforces that the contract fields exist before allowing GPU replicate.

## Rule Codes (Grounded in Batch-2 Hard-Mode Evidence)

Router v2 emits rule codes (stable identifiers) explaining why a task is allowed/blocked.

### `ZERO_MUTATION_OPERATOR`

Trigger (task fields and/or config id):
- `k_point_mutation` with `k == 0`, or
- `per_locus_flip` with `p == 0`, or
- config ids matching patterns like `_k0p0` / `_p0p0`.

Policy:
- For long-run/validation tasks: `status=NO`.
- Allowed only when explicitly labeled as a negative-control task.

Grounding:
- Batch-2 includes multiple `k0p0`/`p0p0` cases; these are not meaningful for "long-run success" and should not be treated as candidates.

### `KC1_FAIL_ALL_SEEDS`

Trigger (from an existing `summary.csv` row for the target config):
- `seeds_total >= 30`
- `kc1_fail_rate == 1.0`
- `threshold_fail_rate == 0.0`

Policy:
- `status=MAYBE_NO`.
- `next_actions` must request boundary-mapping diagnostics, not more long runs.

Grounding:
- Batch-2 shows configs with `overall_pass_rate==0.0` that are exclusively KC1-killed (`kc1_fail_rate==1.0`, `threshold_fail_rate==0.0`).

### `SANITY_BROKEN`

Trigger (from `summary.csv` sanity rows or explicit task flag):
- controls not passing (`control overall_pass_rate < 1.0`), or
- negative not failing (`negative overall_pass_rate > 0.0`), or
- explicit `sanity_broken=true`.

Policy:
- `status=NO` and stop. No further routing should proceed until sanity is restored.

## Task Format (Router Input)

Router v2 expects a JSONL queue of tasks. Each task SHOULD include:
- `task_id` (string; stable id)
- `task_type` (string; e.g. `long_run_validation`, `diagnostics`, `gpu_replicate`)
- `target_config_id` (string)
- `cpu_command` (string)
- `gpu_command` (optional string)
- `authoritativeness` (must be `CPU`)
- `evidence_level` (`L0`/`L1`/`L2`)
- `expected_artifacts` (list of strings)
- `compare_script` (optional string; required for GPU replicate to be `MAYBE_YES`)
- `do_not_merge_results` (bool; must be true when GPU replicate is present)
- `summary_csv_path` (optional string; enables ruleing based on prior outcomes)
- `mutation_operator` (optional object describing operator + params; enables `ZERO_MUTATION_OPERATOR`)

## Decision Format (Router Output)

Router v2 writes a JSONL decision log. Each decision MUST include:
- `task_id`
- `status` (YES/NO/MAYBE_YES/MAYBE_NO)
- `rule_codes` (list of strings)
- `reason` (human-readable, concise)
- `required_evidence` (object describing what evidence is required to upgrade)
- `next_actions` (list of action objects)

It MAY also include:
- `gpu_status` and `gpu_reason` (GPU replicate governance)
- `router_version`

