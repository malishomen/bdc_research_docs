# EXP-0802: R2 Controlled Task Environment

## Status
- Date: 2026-03-19
- Status: ACTIVE SCIENTIFIC PACKAGE
- Depends on:
  - `docs/project/BDC_RESEARCH_REBOOT_PLAN.md`
  - `docs/project/BDC_RESEARCH_REBOOT_CHARTER.md`
  - `docs/project/BDC_SCIENTIFIC_PREEXPERIMENT_GATE_PROTOCOL.md`
  - `docs/experiments/BDC_R1_FULL_SWEEP_PREEXPERIMENT_GATE.md`
  - `results/selection_physics_reboot_r1_full/aggregates/r1_gate_decision.json`
  - `docs/experiments/BDC_R1_FULL_RESULT_PACKET/BDC_CLIENT_BUNDLE_OUTPUT/bundle_result.json`

## Purpose

`Phase R2` defines the next bounded scientific question after the successful completion of `R1`.

`R1` answered only this:
- a bounded non-legacy selection-physics family can support feasible growth and therefore justify progression.

`R2` must answer the next narrow question:
- what is the smallest controlled task environment, richer than `hidden_rule`, that is still scientifically interpretable and suitable for the reboot line.

`R2` does not authorize organism assembly.
It does not authorize cell rhetoric.
It does not reopen `SuperCell` construction.

## Why R2 exists now

The reboot plan explicitly required:
1. `R1` first to validate selection physics,
2. then `R2` to define a post-`hidden_rule` controlled environment.

`R1` has now produced the bounded verdict:
- `PASS_TO_R2`

That means the project is no longer blocked on selection physics.
It is now blocked on environment honesty.

## R2 scientific question

The question is not:
- "Can we already build a digital cell?"

The question is:
- "What controlled environment is rich enough to pressure memory, uncertainty, and adaptation, while remaining causal enough to support mechanism-level interpretation?"

## R2 decision gate

`R2` must end with one of two bounded outcomes:
- `APPROVE_R2_ENVIRONMENT`
- `REMAIN_IN_R2`

No softer rhetorical verdicts are allowed.

## Required properties of an admissible R2 environment

An `R2` candidate environment must satisfy all of the following.

1. More meaningful than `hidden_rule`
- not a single static boolean label function
- not a trivial parameter-count toy

2. Mechanistically interpretable
- input-output relations must be inspectable
- failure should be attributable to identifiable causes

3. Deterministic
- same seed -> same dataset / same environment surface

4. Supports bounded pressure on at least one reboot-relevant mechanism
- memory pressure,
- uncertainty handling,
- resource budgeting,
- or staged adaptation

5. Baseline-comparable
- simple non-evolution baselines must be definable
- random/no-op/trivial baselines must exist

6. Compatible with bounded measurement
- pass/fail metrics must be explicit
- no vague emergent-story scoring

## Candidate environment families

`R2` should compare candidate families before selecting the canonical environment.

### Candidate A - Controlled sequence memory
- deterministic symbol-sequence task
- requires short-horizon memory and recall
- remains fully inspectable

### Candidate B - Controlled abstention / uncertainty task
- deterministic classification or decision task with explicit ambiguous cases
- pressures quaternary-style abstention logic
- allows measured abstain-vs-error tradeoffs

### Candidate C - Micro-corpus cloze task
- bounded, deterministic, synthetic or tightly curated text snippets
- richer than boolean `hidden_rule`
- still small enough for causal inspection and baseline comparison

## What R2 must not do

The following are prohibited in `R2`:
- full messy Wikipedia-scale environment claims,
- organism assembly,
- cell language without formal semantics,
- post-hoc threshold tuning,
- broad architecture search,
- reopening the old `hidden_rule` line as if it were still the active environment.

## Minimum required R2 measurements

Every candidate environment must provide, at minimum:
- deterministic generation proof,
- baseline score table,
- trivial-strategy exposure,
- failure-mode inventory,
- explicit mechanism pressure description,
- evidence of causal inspectability.

## R2 acceptance criteria

An environment may be approved for downstream reboot work only if it:
1. is deterministic,
2. exceeds `hidden_rule` in meaningful pressure,
3. remains bounded and interpretable,
4. has explicit baselines and stop-rules,
5. does not smuggle in organism-level claims.

## Preferred use of BDC Designer in R2

`BDC Designer` must be used first as:
- the narrowing layer,
- the evidence-state layer,
- the false-direction layer,
- and the decision-gate partner.

Direct experiment execution only begins after that pre-experiment gate is explicit.

## Immediate next step after this package

The next correct action is not implementation-first.

The next correct action is to execute the bounded `R2` task chain:
1. candidate environment matrix and selection criteria,
2. baseline and measurement harness spec,
3. final `APPROVE_R2_ENVIRONMENT` vs `REMAIN_IN_R2` gate package.
