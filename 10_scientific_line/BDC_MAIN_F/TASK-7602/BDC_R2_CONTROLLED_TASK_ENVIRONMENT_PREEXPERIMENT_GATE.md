# BDC R2 Controlled Task Environment Pre-Experiment Gate

## Cycle Identity
- Cycle ID: `BDC_R2_CONTROLLED_TASK_ENVIRONMENT`
- Scientific phase: `R2 - Controlled Task Environment`
- Date: `2026-03-19`
- Owner: `BDC / CODEX`

## Hypothesis
- Primary hypothesis:
  - At least one controlled post-`hidden_rule` environment family can be defined that is more scientifically meaningful than the old toy task while remaining deterministic, baseline-comparable, and causally interpretable.
- Secondary hypothesis:
  - `BDC Designer` can help narrow the candidate environment family without replacing direct scientific validation.
- Out-of-scope hypotheses:
  - organism assembly,
  - digital cell viability,
  - SuperCell claims,
  - cooperation advantage,
  - transfer between environments.

## Decision Gate
- What decision must this cycle support?
  - Whether a candidate environment should be approved as the canonical bounded reboot environment for downstream implementation.
- What decision is explicitly not being made?
  - It does not decide whether the reboot has already validated memory, uncertainty, or any organism-level mechanism.

## Evidence State
- Measured evidence:
  - `R1` full canonical gate passed with `PASS_TO_R2`.
  - `BDC Designer` accepted the full `R1` result packet as `supported`.
- Historical prior evidence:
  - `hidden_rule` is exhausted as the active line.
  - Old complexity physics was structurally insufficient for honest growth.
- Inferred evidence:
  - The next honest bottleneck is environment design, not more physics reinterpretation.
- Missing evidence:
  - no approved post-`hidden_rule` controlled environment exists yet,
  - no canonical baseline table exists for R2 candidate families,
  - no final R2 environment gate has been executed.
- Contradicted evidence:
  - none yet for the bounded R2 question.

## False Directions To Exclude
- Do not reinterpret `R1 PASS_TO_R2` as permission to build a cell immediately.
- Do not jump to full Wikipedia-scale organism claims.
- Do not choose an environment by aesthetics alone.
- Do not let `BDC Designer` winner-prior output replace direct scientific environment validation.

## Minimal Execution Scope
- Smallest valid cycle:
  - define candidate environment families,
  - define baseline and metric contract,
  - decide `APPROVE_R2_ENVIRONMENT` vs `REMAIN_IN_R2`.
- Allowed implementation surface:
  - docs, deterministic task specs, baseline contracts, gate packet, and bounded scaffolding scripts.
- Forbidden scope expansion:
  - organism components,
  - rich multi-mechanism assembly,
  - broad architecture search,
  - deployment/product claims.

## Required Measurements
- deterministic generation proof,
- baseline comparison surface,
- trivial strategy exposure,
- failure registry,
- mechanism pressure declaration,
- explicit gate criteria.

## Verdict Contract
- PASS means:
  - at least one candidate environment is approved as the bounded canonical R2 environment.
- FAIL means:
  - the candidate comparison or metric contract is broken and no valid gate packet can be produced.
- REMAIN_IN_PHASE means:
  - the comparison ran honestly, but no candidate environment is yet good enough to be approved.

## Canonical Attachments
- `docs/experiments/EXP-0802_R2_CONTROLLED_TASK_ENVIRONMENT.md`
- `results/selection_physics_reboot_r1_full/aggregates/r1_gate_decision.json`
- `docs/experiments/BDC_R1_FULL_RESULT_PACKET/BDC_CLIENT_BUNDLE_OUTPUT/bundle_result.json`

## Integrity Note
`R2` exists because `R1` passed.
It does not inherit permission to widen claims beyond a controlled environment-selection phase.
