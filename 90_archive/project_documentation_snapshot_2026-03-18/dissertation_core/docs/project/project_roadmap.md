# BDC Project Roadmap v2

**Version:** 2.0  
**Date:** 2026-02-27  
**Status:** ACTIVE  
**Branch:** test  
**Supersedes:** `docs/project/BDC_ROADMAP_Paramecium_MVP_TRL-3.md`  
**Companion:** `docs/project/project_main_doc.md` (master project document)  
**Continuity Sources:** CONTINUITY_HANDOFF_20260226, PROJECT_FULL_TASK_REGISTRY_20260227, PROJECT_KNOWLEDGE_CONSOLIDATED_20260227, TASK-1400B results

---

## Current Execution Status (2026-03-17)

The original digital-biology roadmap below remains preserved as historical strategic context.

Current active productized line for operator/client delivery:
- `BDC Designer`

Canonical current-state reference:
- `docs/project/BDC_DESIGNER_FREEZE_STATE.md`

Recent completed execution line:
- `docs/project/BDC_DESIGNER_POST_TEXTAI_ROADMAP.md`

Current practical meaning:
- `BDC Designer` is frozen as the mainline-ready subsystem,
- client intake, redesign guidance, and delivery bundle workflows are operational,
- future execution should branch from this freeze state rather than reinterpret the older roadmap as the active delivery line.

---

## 0. Non-Negotiables (Canon Alignment)

1. **No claims without artifacts.** Any metric statement must point to files from reproducible runs.
2. **Reproducibility anchor.** Canonical PASS/FAIL is `summary.json.kill_status` (runtime) unless an ADR states otherwise.
3. **Append-only logs.** `AGENTS_LOG.md`, `WEEKLY_STATUS.md` are append-only.
4. **Main is protected.** Work in `test`. Merge to main only on explicit command `MERGE_MAIN_NOW`.
5. **No scope creep.** New ideas become new experiments/epics; do not mix experiments.
6. **FAIL is valuable.** Stop when a kill criterion triggers and record it.
7. **Each phase is gated.** Proceed to Phase N+1 only if Phase N passes its success criteria.
8. **One component at a time.** No multi-component "SuperCell v0" until individual components are validated.

---

## 1. Executive Summary — Where We Are (L0 Facts)

### Two working systems exist but are not connected

| System | Status | Proven Capabilities |
|--------|--------|---------------------|
| **Evolution Engine** (EDP1) | Working | Determinism, N=30 validation, speciation, diversity shock, lineage logging, metrics integrity, 3 genome versions |
| **Wiki Pipeline** | Working | 278k docs (simplified_wiki_v0), cloze metric, crash-safe harness, deterministic pipeline |

### The decisive result: TASK-1400B

```
v2 (MRTN) under fitness = accuracy - 0.01 * sum(|w|):
  final_max_complexity_mean  ~ 34.19
  penalty_mean               ~ 0.3419
  required_accuracy           ~ 1.13 (> 1.0)
  feasibility_flag            = FALSE
```

**Conclusion:** Current physics structurally forbids architectural growth. The `hidden_rule` line is exhausted. Strategy must change.

### hidden_rule line exhausted

| Genome | max_accuracy_mean | max_fitness_mean | Verdict |
|--------|------------------|-----------------|---------|
| v1 (LTF) | ~0.824 | ~0.788 | Baseline. Ceiling reached. |
| v1.5 (interaction) | ~0.812 | ~0.764 | FAIL. Accuracy dropped, penalty increased. |
| v2 (MRTN) | ~0.789 | ~0.553 | Accuracy competitive. Fitness crushed by complexity. |
| v2 staged | ~0.789 | ~0.552 | Marginal change. Phase separation ineffective. |

### Strategic principle

**Minimum viable bridge between two working systems** — connect Evolution Engine + Wiki Pipeline before inventing a third system from scratch.

---

## 2. Where We're Going (Strategic North Star)

BDC is a digital biology research program. The path forward:

1. Fix the physics of selection (allow complexity growth)
2. Connect evolution to a real-world task (wiki cloze)
3. Make complexity pay for itself through energy, not fitness penalty
4. Enable role differentiation and collective performance
5. Test transfer between environments (digital panspermia)

---

## 3. Phase Overview

```
Phase 0  -->  Phase 1  -->  Phase 2  -->  Phase 3  -->  Phase 4  -->  Phase 5  -->  Phase 6
Closure       Physics      New Task      Energy       Cooperation   Panspermia   Evaluation
(1-2d)        (3-5d)       (5-7d)        (5-7d)       (7-10d)       (7-10d)      Gate
              GATE -->     GATE -->      GATE -->     GATE -->      GATE -->
```

**Each arrow is a gate.** Phase N+1 begins only if Phase N PASS.

**Parallel tracks** (do not gate main phases):

- Wiki LM entropy collapse investigation
- HIVE integration planning

## Experiment Documentation Requirement

At completion of each major phase gate, create or update a matching EXP document in `docs/experiments/` using the standard in `docs/experiments/README.md`.

Minimum requirement:
- one EXP file per key phase experiment,
- explicit links to supporting `TASK-*` reports and ADR decisions,
- concise interpretation layer separate from raw run artifacts.

---

## Phase 0 — Formal Closure & Governance

**Duration:** 1-2 days  
**Type:** R0 documentation + governance  
**Goal:** Close the exhausted `hidden_rule` direction. Preserve code as benchmark and physics lab.

### TASK-1500: R2 Formal Closure of EDP1 hidden_rule Line

**Steps:**

1. Create `decisions/ADR-0004-hidden-rule-closure.md`:
   - Document exhaustion evidence: v1 ceiling, v2/v1.5 FAIL, TASK-1400B impossibility proof
   - Declare `hidden_rule` line closed as a product direction
   - Preserve as benchmark lab (controlled variable for Phase 1)
   - Document relationship between closed line and H1-H3 ongoing validation
2. Update `KILL_CRITERIA.yaml`: mark `hidden_rule` line closed; preserve artifact references
3. Declare `v1_speciation` as permanent baseline for this lab task
4. Update `ARCHITECTURE.md` with closure note

**Deliverables:**

- `decisions/ADR-0004-hidden-rule-closure.md`
- Updated `KILL_CRITERIA.yaml`
- Updated `ARCHITECTURE.md`
- `reports/analysis/TASK-1500-CLOSURE/TASK-1500_BRIEF_REPORT.md`

**Success criteria:** ADR-0004 committed to `test`. No experimental code changes.

**Kill criteria:** N/A (governance-only task).

**Rollback:** Revert ADR + kill criteria file changes.

---

## Phase 1 — Physics Fix: Complexity Regime Sweep

**Duration:** 3-5 days  
**Type:** R2 proposal + experiment  
**Prerequisite:** Phase 0 complete  
**Goal:** Find a complexity regime that does not structurally forbid composition. Not "pick one formula by taste" — run an empirical sweep.

### TASK-1501: Complexity Regime Experiment (exp_0300)

**Candidate regimes:**

| ID | Formula | Property |
|----|---------|----------|
| A (current) | `complexity = sum(\|w\|)` | Linear size tax (control) |
| B (normalized) | `complexity = mean(\|w\|)` | Normalized by parameter count |
| C (sub-linear) | `complexity = sum(\|w\|) / sqrt(K)` | Sub-linear scaling (K = param count) |
| D (per-class) | `fitness = accuracy - lambda_class * sum(\|w\|)` | Per-architecture lambda |
| E (ablation) | `penalty = 0` | No penalty (diagnostic baseline) |

**Protocol:**

- Environment: `hidden_rule` (controlled variable — same task as before for comparability)
- Genomes: v1, v1.5, v2
- Runs: N=30, G=100, P=100 for each (regime x genome) = 15 configurations x 30 seeds = 450 runs
- Metric decomposition: accuracy, complexity, penalty, fitness reported separately for every run
- All existing evolution engine features active (speciation, shock)

**Success criteria:**

1. At least one regime makes v2 **mathematically feasible**: `required_accuracy_to_beat_v1 <= 1.0`
2. At least one regime makes v2 **empirically competitive**:
   - `final_max_accuracy_mean(v2) >= final_max_accuracy_mean(v1)`, OR
   - best_single_accuracy above LTF ceiling in >= 10/30 seeds

**Kill criteria:**

- If NO regime enables feasibility for v2 -> problem is not physics alone; v2 architecture or mutation operators need fundamental redesign
- If regime E (no penalty) shows no accuracy improvement -> v2's search dynamics are broken regardless of physics
- If all regimes produce trivial strategies (accuracy collapse under no penalty) -> penalty-free evolution not viable

**Deliverables:**

- `results/edp1_exp0300_complexity_sweep/` — full run artifacts per regime per genome
- `reports/analysis/TASK-1501-COMPLEXITY-SWEEP/` — feasibility table, cross-regime comparison, BRIEF_REPORT.md
- `decisions/ADR-0005-complexity-regime.md` — chosen regime with evidence (or documented rejection of all candidates)

**Rollback:** All regimes implemented behind CLI flags; default remains regime A until ADR-0005 accepted.

---

## Phase 2 — New Task: Wiki-Derived Evolution

**Duration:** 5-7 days  
**Type:** R2 (new task class)  
**Prerequisite:** Phase 1 PASS (at least one regime enables feasibility)  
**Goal:** Bridge Evolution Engine and Wiki Pipeline. Replace toy boolean task with real-world language task.

### TASK-1600: Cloze Evolution Task on simplified_wiki_v0 (exp_0400)

**Design principle:** Minimal bridge using existing infrastructure. No "SuperCell v0" scope explosion.

| Component | Source | New Work |
|-----------|--------|----------|
| Data | `simplified_wiki_v0` (278k docs, exists) | Deterministic subset selection via PiStream |
| Metric | Cloze accuracy (exists from TASK-0139) | Adapter to evolution fitness function |
| Evolution | EDP1 engine (exists) | Minimal modifications (new fitness function, new genome type) |
| Genome | **New: ClozeGenome v0** | Small genome parameterizing cloze prediction strategy |

**ClozeGenome v0 — candidate strategy families (start simplest, expand only on evidence):**

1. **Token frequency weights** — genome encodes weights for frequency-based prediction
2. **Context window rules** — genome encodes attention weights for surrounding tokens
3. **Feature heuristics** — genome encodes rules based on token features (length, capitalization, position)
4. **(Optional, Phase 2b)** Quaternary decision layer — "abstain" on low-confidence predictions, penalize abstention (first H1 integration test)

**Genome specification:** Document in `docs/CLOZE_GENOME_SPEC.md` before implementation. Include: encoding, mutation operators, complexity calculation, interpretation rules.

**Protocol:**

- N=30 seeds
- G=50 generations (shorter — new territory, conserve compute)
- P=100 population
- Complexity formula: best candidate from Phase 1 (per ADR-0005)
- Environment: deterministic subset of simplified_wiki_v0 (100 documents, selected via PiStream)
- Speciation and diversity shock: active (reuse existing implementation)

**Baselines (minimum 3):**

1. Random predictor (uniform random token selection)
2. Frequency baseline (always predict most common token in corpus)
3. Trivial always-same-token baseline (always predict a fixed token)
4. (Optional) Bigram baseline (predict based on previous token frequency)

**Success criteria:**

1. Evolved strategies exceed best baseline by >= 5% absolute cloze accuracy with 95% CI
2. Fitness trajectory shows progressive improvement (slope > 0 across generation ranges)
3. Population maintains functional diversity > 0.3 at final generation

**Kill criteria:**

- Evolved strategies do not exceed baselines -> genome representation not suitable for language tasks; redesign genome
- Fitness plateaus before generation 10 -> search dynamics broken in this space
- All seeds converge to identical strategy -> diversity mechanisms insufficient for this task
- Accuracy is random (< baseline + 1%) in > 25/30 seeds -> task-genome mismatch

**Deliverables:**

- `evolution/cloze_symbolic/` — new evolution task module (genome, evaluate, task, run_generations)
- `results/edp1_exp0400_cloze/` — full run artifacts
- `reports/analysis/TASK-1600-CLOZE-EVOLUTION/` — baseline comparison, fitness trajectory, BRIEF_REPORT.md
- `docs/CLOZE_GENOME_SPEC.md` — canonical genome specification

**Rollback:** None; experiment is additive. All new code in separate module. Old `edp1_symbolic` untouched.

---

## Phase 3 — Resource-Bounded Evolution

**Duration:** 5-7 days  
**Type:** R2 (new selection mechanism)  
**Prerequisite:** Phase 1 AND Phase 2 PASS  
**Goal:** Replace artificial fitness penalty with biological resource pressure. Complexity costs energy, not fitness.

### TASK-1700: Resource-Bounded Evolution (exp_0500)

**Minimal energy model (ONE component — not 9-component SuperCell):**

```
Each individual has:
  energy_budget = E_0  (fixed per generation, configurable)

Each computation costs energy:
  energy_cost = f(complexity)  (monotonically increasing)

Reproduction rule:
  if energy_remaining > 0 AND fitness_rank in top-K:
    reproduce (with mutation)
  else:
    do not reproduce

Key difference from current regime:
  fitness = task_accuracy  (NO penalty subtracted)
  complexity affects survival through energy, not through fitness arithmetic
```

**What this achieves:**

- Complex organisms can win IF they use complexity efficiently (high accuracy per energy unit)
- Simple organisms have more energy budget remaining, allowing more reproduction attempts
- Natural pressure: quality (complex, accurate) vs quantity (simple, prolific)
- No artificial ceiling on required accuracy

**Energy parameter sweep:**

| Parameter | Values |
|-----------|--------|
| E_0 (budget) | Low (tight constraint), Medium, High (loose constraint) |
| Cost function | Linear `f(c) = alpha * c`, Sub-linear `f(c) = alpha * sqrt(c)`, Step `f(c) = alpha * ceil(c/threshold)` |

**Protocol:**

- Task: Cloze task from Phase 2
- Genome: ClozeGenome v0
- N=30 seeds, G=100, P=100
- 3 x 3 = 9 energy configurations

**Success criteria:**

1. Stable distribution of complexity levels emerges (not all trivial, not all maximal; measured by complexity variance > threshold)
2. Population maintains survival (no mass extinction: population > 50% of P at gen 100 in >= 25/30 seeds)
3. Task accuracy improves over generations (monotonic trend in mean accuracy per 10-gen window)
4. Higher-complexity individuals appear and persist in at least 50% of seeds

**Kill criteria:**

- All seeds collapse to minimal complexity -> energy model too restrictive (simplicity always wins)
- Unbounded complexity growth in all seeds -> energy model too permissive (no constraint)
- Mass extinction (population < 20% of P) in > 15/30 seeds -> energy budget fundamentally miscalibrated
- No accuracy improvement over random baseline -> energy model disrupts learning

**Deliverables:**

- `evolution/energy_model.py` — energy system module (budget, cost function, reproduction gate)
- `results/edp1_exp0500_energy/` — full run artifacts per configuration
- `reports/analysis/TASK-1700-ENERGY-MODEL/` — complexity distribution analysis, survival curves, BRIEF_REPORT.md
- Updated `KILL_CRITERIA.yaml` with energy model criteria

**Rollback:** Energy model behind `--energy-model` flag; flag-off restores Phase 2 behavior.

---

## Phase 4 — Specialization & Cooperation

**Duration:** 7-10 days  
**Type:** R2 (collective fitness)  
**Prerequisite:** Phase 2 PASS + ADR-0009 closure accepted (Phase 3 energy model formally closed at current scale)  
**Goal:** Demonstrate division of labor and collective advantage — the first step toward digital multicellularity.

### TASK-1800: Multi-Role Evolution (exp_0600)

**Spec:** `reports/analysis/TASK-1800-MULTI-ROLE/TASK-1800_SPEC.md` (2-task MVP: cloze + entity; category deferred)

**Design:**

- Population contains organisms with different genome types or strategy profiles
- Fitness depends on **collective performance** across a suite of wiki-derived micro-tasks
- Roles emerge from evolution, not from assignment

**Micro-task suite (minimum 3):**

1. **Cloze prediction** (existing from Phase 2)
2. **Entity detection** — predict whether a masked token is a named entity (binary task derived from wiki markup)
3. **Category classification** — predict the Wikipedia category of a document from token features

**Collective fitness function:**

```
collective_fitness(population) = weighted_mean(
  best_cloze_accuracy(population),
  best_entity_accuracy(population),
  best_category_accuracy(population)
)

individual_fitness(organism) = contribution_to_collective(organism)
```

**Protocol:**

- N=30 seeds, G=100, P=200 (larger population for role emergence)
- Energy model from Phase 3
- Speciation active (already implemented — naturally creates niches)
- 3 micro-tasks, equal weight initially

**Success criteria:**

1. `collective_performance > best_single_role_individual_performance` with 95% CI (cooperation advantage exists)
2. Stable role diversity: >= 2 distinct functional groups in >= 24/30 seeds at gen 100
3. Role necessity: removing any functional group degrades collective performance by >= 5%

**Kill criteria:**

- `collective_performance <= best_individual_performance` -> cooperation not emerging
- Mono-role dominance (one role > 90% of population) in > 20/30 seeds -> specialization not occurring
- Roles are interchangeable (removing one doesn't degrade performance > 2%) -> division is superficial
- Mass extinction of minority roles -> ecosystem not stable

**Deliverables:**

- `evolution/collective_fitness.py` — collective evaluation module
- `evolution/micro_tasks/` — entity detection and category classification modules
- `results/edp1_exp0600_multirole/` — full run artifacts
- `reports/analysis/TASK-1800-MULTI-ROLE/` — role analysis, cooperation metrics, BRIEF_REPORT.md

**Rollback:** Collective fitness behind `--collective` flag; flag-off restores individual fitness.

---

## Phase 5 — Digital Panspermia Transfer Test

**Duration:** 7-10 days  
**Type:** R2 (new hypothesis validation — H5)  
**Prerequisite:** Phase 4 PASS  
**Goal:** Test the CORE BDC thesis — organisms evolved in one environment adapt faster when transferred to a new environment.

### TASK-1900: Digital Panspermia Experiment (EXPERIMENT-PAN-001)

**Design:**

- **Environment A (Broth A):** Wiki subset from domain X (e.g., biology articles from simplified_wiki_v0)
- **Environment B (Broth B):** Wiki subset from domain Y (e.g., physics/chemistry articles)
- Both subsets selected deterministically via PiStream, non-overlapping
- Same genome type, same energy model, same evolution parameters

**Protocol:**

1. **Evolve in A:** N=30 seeds, G=100, P=200 -> extract top-K organisms per seed (SuperCells)
2. **Transfer A->B:** Seed Environment B with extracted SuperCells -> measure time-to-threshold
3. **Control (de novo B):** Start fresh in Environment B with random initialization -> measure time-to-threshold
4. **Reverse transfer B->A (optional):** Test "strengthening" effect

**Metrics:**

| Metric | Definition |
|--------|-----------|
| Time-to-adapt | Generations to reach fitness threshold (e.g., baseline + 10%) in new environment |
| Transfer advantage | `time_to_adapt(de_novo) / time_to_adapt(transfer)` — ratio > 1.0 means transfer helps |
| Lineage persistence | Fraction of transferred lineages surviving at gen 50 in new environment |
| Peak fitness comparison | `max_fitness(transfer, gen=100) vs max_fitness(de_novo, gen=100)` |
| Robustness | Performance stability under diversity shock in new environment |

**Success criteria:**

1. `transfer_advantage > 1.0` with 95% CI (transferred organisms adapt faster)
2. Lineage persistence > 30% at gen 50 (transferred organisms don't immediately die)
3. Transferred population achieves higher peak fitness than de novo within G=100 in >= 20/30 seeds

**Kill criteria:**

- `transfer_advantage <= 1.0` -> transfer provides no benefit; panspermia concept not validated at this level
- Mass extinction of transferred organisms (lineage persistence < 10% at gen 20) -> organisms overfit to source environment
- Transferred organisms converge to same strategies as de novo by gen 50 -> no knowledge transfer occurring (only survival of generic strategies)

**Deliverables:**

- `results/edp1_pan001_transfer/` — full run artifacts (both transfer and control)
- `reports/analysis/TASK-1900-PANSPERMIA/` — transfer analysis, lineage tracking, BRIEF_REPORT.md
- `decisions/ADR-0006-panspermia-validation.md` — validation or rejection of H5

**Rollback:** None; experiment is additive.

---

## Phase 6 — Evaluation Gate & Roadmap Revision

**Purpose:** Comprehensive review of Phases 0-5 results to determine next strategic direction.

**At this gate, and only here:**

1. Assess cumulative results: which phases PASS, which FAIL, what patterns emerge
2. Evaluate whether "functional competence" can be operationally defined from Phase 2-5 metrics
3. Decide whether SuperCell v0 (full multi-component organism) is justified by evidence
4. Assess partial H1-H3 validation status within new architecture
5. Decide on HIVE-scale distributed experiments
6. Decide on Nano-LLM / Dual-Head architecture investigation
7. Propose next ADRs based solely on L0 evidence
8. Revise this roadmap for next cycle

**Possible outcomes:**

| Outcome | Condition | Next Step |
|---------|-----------|-----------|
| **A: Full success** | Phases 1-5 all PASS | Design SuperCell v0 multi-component integration; plan Nano-LLM investigation |
| **B: Partial success** | Some phases PASS, some FAIL | Analyze root causes; redesign failed components; re-run failed phases |
| **C: Physics works, task doesn't** | Phase 1 PASS, Phase 2 FAIL | Redesign genome for language tasks; consider Nano-LLM for Phase 2 retry |
| **D: Nothing works** | Phase 1 FAIL | Fundamental v2 architecture problem; consider clean genome redesign or H1-H3 direct validation |

---

## Phase 2 — Current Status and TASK-1606 Decision Tree (2026-02-28)

**Phase 2 Gate Result (TASK-1605):** PARTIAL FAILURE

| Criterion | Result | Verdict |
|---|---|---|
| 1. delta >= 5% absolute accuracy (95% CI) | lower_CI = 0.022 < 0.05 | **FAIL** |
| 2. Positive fitness slope | 30/30 seeds | PASS |
| 3. Functional diversity > 0.3 | 30/30 seeds | PASS |
| Kill criteria | None triggered | PASS |

**Diagnosis:** Representational ceiling with 3-sensor v2 architecture (freq, bigram, rev_bigram). Consistent ~2.4% improvement over bigram baseline, but < 5% threshold.

### TASK-1606: Sensor Enrichment Diagnostic (IN PROGRESS)

**Purpose:** Determine whether adding skip-bigram sensors and/or more generations can break the ceiling.

**4-arm sweep:**

| Arm | Sensors | Generations | Purpose |
|---|---|---|---|
| arm_3s_G50 | 3 (control) | 50 | Reproduce TASK-1605 baseline |
| arm_5s_G50 | 5 (+skip-bigram) | 50 | Test sensor enrichment |
| arm_3s_G100 | 3 | 100 | Test convergence headroom |
| arm_5s_G100 | 5 | 100 | Combined |

**Decision matrix:**

```
TASK-1606 Results
  |
  +--[Arm reaches lower_CI(delta) >= 0.05]
  |    |
  |    +--[arm_5s only]--> Re-run gate with 5-sensor, N=30
  |    +--[arm_G100 only]--> Re-run gate with G=100, N=30
  |    +--[arm_5s_G100]--> Re-run gate with 5-sensor G=100, N=30
  |
  +--[No arm reaches 0.05]
       |
       v
       R2 Decision Required:
         Option A: Revise 5% threshold (with justification)
         Option B: Fibonacci context windows (Proposal 5 from φ-analysis)
         Option C: Genome v3 redesign
         Option D: Accept current performance, proceed to Phase 3
```

### TASK-1607: ADR-0008 + 5-Sensor Gate Re-run (COMPLETED)

**Governance update:** `ADR-0008` accepted. Phase 2 Criterion 1 revised from `>=5%` to `>=3%` absolute delta (95% CI).

**Gate re-run configuration:** `v2 --use_skip_bigram`, `hard`, `top_k=8`, `N=30`, `G=50`, `P=100`, `subset_size=100`.

**Gate re-run result (TASK-1607):**

| Criterion | Result | Verdict |
|---|---|---|
| 1. revised delta >= 3% absolute accuracy (95% CI) | lower_CI = 0.03087 >= 0.03 | **PASS** |
| 2. Positive slope | 30/30 seeds | PASS |
| 3. Functional diversity > 0.3 | 30/30 seeds | PASS |
| Kill criteria | None triggered | PASS |

**Phase 2 status:** COMPLETE (under ADR-0008).  
**Phase 3 status:** UNBLOCKED.

---

## Phase 3 — Current Status and Closure (2026-03-01)

**Phase 3 Run Result (TASK-1700-RUN):** FAILURE

| Item | Evidence | Verdict |
|---|---|---|
| Config coverage | 9 configs x 10 seeds = 90 runs | PASS (execution complete) |
| Success criteria | 0/9 configs satisfy all Phase 3 success checks | **FAIL** |
| Kill criteria | Mass extinction triggered in 5/9 configs | **FAIL** |
| Complexity differentiation | Complexity variance remains narrow; no reliable energy-driven gradient | **FAIL** |

**Governance decision:** `ADR-0009` accepted.

- Phase 3 energy model is closed as FAIL at current genome scale.
- Energy model remains preserved behind `--energy_model` for future larger-genome experiments.
- Phase 4 is unblocked under the proven Phase 2 penalty regime (`ADR-0005`, Regime B, `lambda=0.01`), with explicit governance exception documented by ADR-0009.

---

## Phase 4 — Interim Status After Metric Fix (2026-03-02)

**Input run:** `TASK-1803-RUN` (`N=30`, `G=100`, `P=200`, 2-task MVP: cloze+entity).  
**Governance update:** `ADR-0007` accepted (collective comparator fix).

### Comparator correction

- Old comparator used in TASK-1803:
  - `delta_old = collective_score - max_individual_collective_fitness`
- Under Scheme S1 (`collective = mean(best_cloze, best_entity)`, individual best = `max(...)`), `delta_old` is structurally non-positive.
- Therefore old comparator is retired for gate decisions.

### Canonical metrics (ADR-0007)

- `A1_i = gain_cloze_i + gain_entity_i`
- `A2_i = min(gain_cloze_i, gain_entity_i)` (primary gate metric)
- `A3`: Pareto rate (`gain_cloze_i > 0 && gain_entity_i > 0`) + Pareto magnitude

### N=30 re-analysis facts

- Artifact: `results/edp1_exp0600_multirole/aggregates/phase4_advantage_recomputed_n30.json`
- `A1` CI95: `[0.0126133312, 0.0280607879]`
- `A2` CI95: `[0.0001794477, 0.0064231588]`
- `A3` Pareto rate: `0.50`

### Status

- **Interim:** no formal PASS/FAIL declared in this step.
- **Mandatory next step:** role-ablation test and explicit gate policy decision on 2-task finalization vs adding 3rd task.

---

## Phase 4 — Role-Ablation Findings and Task-Suite Policy (2026-03-02)

**Input artifacts:**
- `results/edp1_exp0600_multirole/aggregates/phase4_advantage_recomputed_n30.json`
- `results/edp1_exp0600_multirole/aggregates/phase4_role_ablation_n30.json`

### Role-ablation facts (N=30)

Collective-score degradation under role removal:

| Ablation | Mean degrade | CI95 | degrade>=5% rate | interchangeable<=2% rate |
|---|---:|---|---:|---:|
| Remove cloze-role specialist | 0.0186277691 | [0.0138617264, 0.0233938118] | 0.0000 | 0.4000 |
| Remove entity-role specialist | 0.0081892915 | [0.0027833123, 0.0135952706] | 0.0333 | 0.9667 |

### Policy decision (task suite before final Phase 4 gate)

- **Decision:** 2-task final gate is **not accepted**.
- **Required:** add a 3rd micro-task before final Phase 4 PASS/FAIL decision.
- Rationale:
  - role-necessity evidence is insufficient under 2-task MVP (`>=5%` degradation criterion rarely triggered),
  - high interchangeability under entity ablation indicates weak necessity signal.

### Mandatory next step

1. Implement/enable 3rd micro-task in Phase 4 suite.
2. Re-run Phase 4 gate metrics under ADR-0007 comparator governance.
3. Repeat role-ablation with updated task suite and then finalize PASS/FAIL.

---

## Phase 4 — 3-Task Preparation Status (2026-03-02)

**Task:** `TASK-1806-3TASK-PREP` (R1 integration prep, no full gate run).

What is now ready:
- deterministic category proxy task (doc-level binary),
- optional 3-task collective wiring (`--use_category_task`),
- category weight support in collective scoring,
- smoke orchestration path for 3-task mode.

What is not done yet:
- full N=30 3-task gate run,
- 3-task role-ablation rerun and final Phase 4 PASS/FAIL decision.

---

## Phase 4 — 3-Task Governance Closure and Re-analysis (2026-03-04)

**Input run status:** `RUN COMPLETE` (`N=30`, seeds `1337..1366`).

**Governance update:** `ADR-0010` accepted for strict 3-task gate logic.

### Canonical 3-task metrics (ADR-0010)

- `gain_cloze_i = max_accuracy_i - best_baseline_accuracy_i`
- `gain_entity_i = max_entity_accuracy_i - best_entity_baseline_accuracy_i`
- `gain_category_i = max_category_accuracy_i - best_category_baseline_accuracy_i`
- `A1_3_i = gain_cloze_i + gain_entity_i + gain_category_i`
- `A2_3_i = min(gain_cloze_i, gain_entity_i, gain_category_i)` (primary)
- `A3_3_i = 1[gain_cloze_i>0 && gain_entity_i>0 && gain_category_i>0]`

### Recomputed N=30 facts (no retraining)

- Artifact: `results/edp1_exp0600_multirole_3task/aggregates/phase4_advantage_recomputed_3task_n30.json`
- `A1_3` CI95: `[0.0044028572, 0.0128146495]`
- `A2_3` CI95: `[-0.0040268661, -0.0003959994]`
- `A3_3` Pareto rate: `0.0333333333` (Wilson CI in artifact)
- `gain_category` CI95: `[-0.0001524435, 0.0004442013]`

### 3-role ablation facts

- Artifact: `results/edp1_exp0600_multirole_3task/aggregates/phase4_role_ablation_3task_n30.json`
- Role verdicts (ADR-0010 necessity rule):
  - `cloze`: `NOT_NECESSARY`
  - `entity`: `NOT_NECESSARY`
  - `category`: `NOT_NECESSARY`

### Official gate status

- `RUN STATUS`: **RUN COMPLETE**
- `GATE STATUS`: **FAIL** (under ADR-0010)
  - Triggered by `A2_3_ci95_high <= 0` and multiple non-necessary roles.

### Mandatory next step

1. Redesign task suite and/or role structure (R2, ADR-gated).
2. Execute a new Phase 4 run only after governance-approved changes.
3. Keep current N=30 artifacts as frozen baseline for comparison.

---

## Phase 4 — Baseline Freeze Before Redesign (2026-03-04)

- Freeze document:
  - `reports/analysis/TASK-1899-P4-FREEZE/PHASE4_BASELINE_FREEZE_2026-03-04.md`
- Policy:
  - do not run any new full `N=30` Phase 4 gate before root-cause dossier + redesign ADR + smoke/determinism gate.
- This freeze anchors all Phase 4R work to:
  - `ADR-0010` governance,
  - current baseline verdict (`RUN COMPLETE`, `GATE FAIL`).

---

## Phase 4R — Minimal Redesign Protocol (2026-03-04)

- Design ADR: `decisions/ADR-0011-phase4r-design.md`
- Primary arm (`P4R_MINIMAL_ARM_A`):
  - balanced category metric,
  - gain-based collective scheme,
  - role-balance bonus.
- Fallback arm (`P4R_MINIMAL_ARM_B`) is pre-registered and may be used only after primary smoke stop-rule fail.
- Governance invariant:
  - final gate still uses `ADR-0010`; no threshold/formula change is allowed without new ADR.

---

## Phase 4R — Smoke/Determinism Gate Outcome (2026-03-04)

- Task: `TASK-1903-P4R-SMOKE-DETERMINISM-GATE`
- Protocol:
  - baseline control smoke (`N=5`, seeds `1337..1341`),
  - primary arm A smoke (`N=5`),
  - fallback arm B smoke (`N=5`),
  - full recompute + role-ablation + provenance on smoke artifacts,
  - deterministic replay check (repeated identical seed run).

### L0 smoke facts

- Determinism check:
  - repeated seed produced identical core final metrics (`max_accuracy`, `max_entity_accuracy`, `max_category_accuracy`, `collective_score`, `max_individual_collective_fitness`).
- Primary arm A (`balanced_accuracy + s1_gain + role_balance_bonus=0.15`):
  - `gain_category_mean = 0.0`,
  - `A2_3_mean = -0.0057969843`.
- Fallback arm B (A + `role_balance_bonus=0.30`, `collective_category_weight=1.50`):
  - `gain_category_mean = 0.0`,
  - `A2_3_mean = -0.0057969843`.
- Baseline control smoke:
  - `A2_3_mean = -0.0091229183`.
- Role-ablation output schema valid in both arms:
  - `cloze_ablation`, `entity_ablation`, `category_ablation` sections present,
  - necessity verdicts present for all roles.

### Stop-rule decision

- `ADR-0011` smoke stop-rule #3 failed for both arms because `gain_category_mean > 0` was not satisfied.
- Consequence:
  - no full `N=30` redesign run (`TASK-1904`) was authorized,
  - no redesign gate decision from fresh `N=30` (`TASK-1905`) was produced.

---

## Phase 4R — Hypothesis Closure (2026-03-04)

- Task: `TASK-1907-HYPOTHESIS-CLOSURE`.
- Decision ADR: `decisions/ADR-0012-phase4r-hypothesis-closure.md`.
- Closure statement:
  - `P4R_MINIMAL_ARM_A` and `P4R_MINIMAL_ARM_B` are rejected for gate progression at current scope.
  - Phase 4 remains:
    - `RUN STATUS`: **RUN COMPLETE**
    - `GATE STATUS`: **FAIL** (per `ADR-0010`)
- Governance implication:
  - no additional full `N=30` rerun is permitted for this redesign line without a new ADR and a new pre-registered hypothesis.

---

## Parallel Applied Track — EXP-0700 (GPU+CPU) (2026-03-04)

- Governance ADR:
  - `decisions/ADR-0013-applied-gpu-cpu-track.md`
  - `decisions/ADR-0014-applied-gpu-recovery.md`
- Experiment spec:
  - `docs/experiments/EXP-0700_APPLIED_GPU_CPU_2026-03-04.md`
- Separation rule:
  - Applied outcomes do **not** rewrite Phase 4 scientific verdict.

### Applied Track status (iteration v1)

- Smoke parity (`TASK-2003`): **PASS**
  - schema/manifest/determinism/fallback checks passed.
- Diagnostic `N=10`:
  - Pilot A (GPU): **FAIL**
    - `CI95_low(delta_gpu) < 0`
    - `stability_fail_rate = 0.6` (> 0.10 limit).
  - Pilot B (CPU): **PASS**
    - `CI95_low(delta_cpu) > 0`
    - `stability_fail_rate = 0.0`.
- Gate `N=30` (`TASK-2006`): **NOT EXECUTED**
  - blocked by ADR-0013 stop-rule (both pilots must pass diagnostic).

### Applied Track recovery (iteration v2, TASK-2100..2108)

- GPU blocker forensic + hardening:
  - `TASK-2100`: root-cause confirmed (`softmax` strict assert in AMP path).
  - `TASK-2101`: numeric hardening added (`dtype-aware audit`, finite guards, `--strict_numeric_asserts`).
  - `TASK-2102`: run-contract upgraded to row-level `run-index-v3`.
  - `TASK-2103`: calibrated GPU profile selected (`opt_amp_bs8`) under fixed rule.
  - `TASK-2104`: ADR-0014 accepted before rerun.
- Diagnostic rerun `N=10` (`TASK-2105`):
  - Pilot A (GPU): **FAIL**
    - `mean_delta_gpu = 0.31609`
    - `CI95 = [-0.67478, 1.30696]`
    - `stability_fail_rate = 0.0`
  - Pilot B (CPU): **PASS**
    - `mean_delta_cpu = 0.09293`
    - `CI95 = [0.08906, 0.09680]`
    - `stability_fail_rate = 0.0`
- Gate `N=30` (`TASK-2106`): **NOT EXECUTED**
  - blocked by ADR-0013 + ADR-0014 (both pilots must pass diagnostic).

### Applied readiness implication (latest)

- Practical Readiness Decision v2 (`TASK-2107`): **FAIL**.
- GPU crash instability was removed, but statistical pass condition for GPU pilot remains unmet.
- Next step requires a new applied-iteration task scope (no post-hoc threshold changes).

---

## Parallel Track: φ/Fibonacci Engineering

**Source:** `docs/PHI_FIBONACCI_BDC_ANALYSIS.md` (research-to-code mapping)
**Policy:** φ/Fibonacci constants are engineering tools (deterministic distribution, mutation scaling, selection balance), NOT claims about "intelligence" or "meaning."

### Already Applied (6 mechanisms)

| Mechanism | Files | Status |
|---|---|---|
| Fibonacci hash (Knuth constant) | `fibonacci.py` | ✅ Active |
| Fibonacci table sizes (8, 5) | `genome.py` | ✅ Active (v1) |
| φ-scaled mutation σ (φ⁻², φ⁻¹, 1.0) | `mutate.py` | ✅ Active |
| Golden section selection (38.2%/61.8%) | `select.py` | ✅ Active |
| 3-acid genome (A/T/G + backbone) | `genome.py` | ✅ Active |
| Apoptosis self-repair | `mutate.py`, `run_generations.py` | ✅ Active |

### Planned Additions (prioritized)

| Priority | Proposal | Level | Dependency | Phase |
|---|---|---|---|---|
| **HIGH** | P3: Fibonacci experiment budget ladder (21/13, 55/34, 89/55, 144/89) | R0 | None | Convention, immediate |
| **HIGH** | P2: FFT spectral diagnostics (drift/stagnation detection) | R0 | None | Post-processing tool |
| MEDIUM | P1: φ-genome integrity checksums | R1 | TASK-1606 results | Phase 2 remediation |
| MEDIUM | P7: Variance-triggered φ-rebalance (soft apoptosis) | R1 | TASK-1606 results | Phase 2 remediation |
| LOW | P5: Fibonacci-distance context windows (skip ∈ {1,2,3,5,8}) | R1 | TASK-1606 FAIL | Phase 2 alt path |
| LOW | P4: Nucleosome-inspired memory chunking | R2 | Phase 4+ | Future |
| LOW | P6: Quasicrystal population topology | R2 | P > 1000 | Future |

### Integration Rules

1. R0 proposals (P2, P3) can be applied immediately without ADR
2. R1 proposals require L0 evidence from TASK-1606 before implementation
3. R2 proposals require separate ADR and are not scheduled until Phase 4+
4. All φ-engineering must be documented in `docs/PHI_FIBONACCI_BDC_ANALYSIS.md`

---

## Parallel Track: Compute Topology

**Policy:** Queen orchestrates, does NOT compute. Local PC + future remote nodes compute.

| Node | Role | CPU | GPU | RAM | Status |
|---|---|---|---|---|---|
| **Queen** (laptop) | Orchestrator | i5-4200U 2C/4T | Disabled (GT 740M dead) | 12 GB | ✅ Optimized (TASK-QUEEN-OPT) |
| **Local PC** | Compute | i7-6700 4C/8T | GTX 1080 Ti 11GB | 24 GB | ✅ Ready (PyTorch 2.5.1+cu121) |
| **MacBook M4 Pro** | Future compute | M4 Pro | M4 Pro GPU | TBD | 🔲 Planned (CF tunnel) |

- Phases 0-3: Local PC only
- Phase 4+: Consider distributed via HIVE + CF tunnels

---

## Parallel Track: Wiki LM Investigation

The Wiki LM pilot (entropy_collapse, perplexity 5.6e101) is a separate investigation that does **not gate** the main roadmap.

**Policy:**

- Do NOT declare Wikipedia "primary soup" for long-running LM training until collapse mechanism is understood
- Phase 2 uses wiki-derived **evaluation** (cloze accuracy), not wiki LM **training** (next-token prediction with backpropagation)
- LM investigation runs independently and reports findings to Phase 6 evaluation

**Investigation tasks:**

1. Diagnose entropy collapse root cause (architecture mismatch? learning rate? data preprocessing?)
2. Propose fix candidates (smaller model, different architecture, curriculum learning, gradient clipping)
3. Run diagnostic experiments (N=3, short runs, cheap)
4. Document findings in `reports/analysis/WIKI-LM-INVESTIGATION/`

---

## Parallel Track: HIVE Integration

HIVE infrastructure (queen server, drone protocol, viz dashboard) is proven but not yet used for main experiments.

**Policy:**

- **Phases 0-3:** All experiments run locally (controlled, reproducible environment)
- **Phase 4+:** HIVE integration considered (distributed population across nodes)
- **Before integration:**
  - Verify determinism is maintained across HIVE nodes
  - Test queen/drone protocol with new fitness functions (cloze, collective)
  - Ensure `viz.bdc-hive.com` can display new metrics (cloze accuracy, energy, roles)
  - Create HIVE integration test suite

---

## Governance Artifacts Required

| Artifact | Phase | Purpose |
|----------|-------|---------|
| `decisions/ADR-0004-hidden-rule-closure.md` | Phase 0 | Close hidden_rule line |
| `decisions/ADR-0005-complexity-regime.md` | Phase 1 | Choose complexity regime |
| `decisions/ADR-0006-panspermia-validation.md` | Phase 5 | Validate or reject H5 |
| `decisions/ADR-0007-collective-fitness.md` | Phase 4 | Validate or reject H6 |
| `decisions/ADR-0010-phase4-3task-gate-governance.md` | Phase 4 | Canonical 3-task gate formulas, role necessity, and threshold governance |
| `decisions/ADR-0013-applied-gpu-cpu-track.md` | Parallel Applied Track | Canonical applied pilot metrics, budgets, and stop-rules |
| `decisions/ADR-0015-applied-fairness-twolevel.md` | Parallel Applied Track | Two-level fairness governance (hard parity + advisory checks) for EXP-0700 v4 |
| `KILL_CRITERIA.yaml` updates | Each phase | Add new kill criteria per phase |
| `docs/EDP1_METRICS_SPEC.md` | Maintained | Canonical metric definitions |
| `docs/CLOZE_GENOME_SPEC.md` | Phase 2 | New genome specification |
| Errata (if needed) | As discovered | Corrections without history rewriting |
| `AGENTS_LOG.md` entries | Each task | Append-only task log |
| `WEEKLY_STATUS.md` entries | Each phase | Append-only status updates |

---

## What We Will NOT Do

1. **No 9-component SuperCell v0** without gated single-component validation
2. **No "functional competence" claims** without formulas, baselines, and thresholds
3. **No "utility" proven** from a single best-run metric
4. **No silent kill criteria changes** — changes require ADR
5. **No mixing experiments** — each phase is a clean, isolated experiment
6. **No premature HIVE scaling** — local experiments first, distribute only when proven
7. **No hardware work** (FPGA, memristors, bio-hybrid) until Phase 6 gate is passed
8. **No silent post-hoc threshold tuning** — threshold changes require ADR with empirical evidence
9. **No abandoning H1-H3** without formal ADR closure
10. **No main branch changes** without explicit `MERGE_MAIN_NOW` command
11. **No new genome versions** without documented `GENOME_SPEC.md` and mutation operator tests
12. **No claims about "understanding"** without operational definition and baseline comparison

---

## Appendix A: TRL Mapping

The new roadmap uses gated phase numbering, not the original TRL 1-9 from the Paramecium MVP vision. Approximate mapping for reference:

| New Phase | TRL Equivalent | Description |
|-----------|---------------|-------------|
| Phase 0 | — | Governance closure |
| Phase 1 | TRL 1-2 | Physics validation (foundational rules) |
| Phase 2 | TRL 3 | New MVP on real task (first organism on real data) |
| Phase 3 | TRL 3+ | Organism mechanics (energy model) |
| Phase 4 | TRL 4 | Multi-agent ecosystem mechanics |
| Phase 5 | TRL 5 | Cross-environment transfer validation |
| Phase 6 | — | Strategic evaluation gate |

---

## Appendix B: Compute Estimates

| Phase | Configurations | Seeds | Generations | Population | Estimated Total Runs |
|-------|---------------|-------|-------------|-----------|---------------------|
| Phase 1 | 15 (5 regimes x 3 genomes) | 30 | 100 | 100 | 450 |
| Phase 2 | 1 | 30 | 50 | 100 | 30 |
| Phase 3 | 9 (3 budgets x 3 cost functions) | 30 | 100 | 100 | 270 |
| Phase 4 | 1 | 30 | 100 | 200 | 30 |
| Phase 5 | 2 (transfer + control) | 30 | 100 | 200 | 60 |
| **Total** | | | | | **~840 runs** |

Phase 1 is the most compute-intensive. Consider running in batches (one regime at a time) with early kill if regime A/E results are sufficient to make decisions.

---

## Appendix C: Decision Tree

```
START
  |
  v
Phase 0: Close hidden_rule line
  |
  v
Phase 1: Complexity regime sweep
  |
  +--[ALL FAIL]--> Problem is architecture, not physics
  |                 |
  |                 v
  |                 Option: Redesign genome v3 from scratch
  |                 Option: Validate H1-H3 directly (return to Paramecium MVP)
  |
  +--[>= 1 PASS]--> Select best regime (ADR-0005)
                      |
                      v
                    Phase 2: Cloze evolution
                      |
                      +--[FAIL]--> Genome can't do language tasks
                      |             |
                      |             v
                      |             Option: Try Nano-LLM genome
                      |             Option: Try different task (entity detection only)
                      |
                      +--[PASS]--> Phase 3: Energy model
                                    |
                                    +--[FAIL]--> Energy model invalid
                                    |             |
                                    |             v
                                    |             Option: Different cost function
                                    |             Option: Keep penalty model from Phase 1
                                    |
                                    +--[PASS]--> Phase 4: Cooperation
                                                  |
                                                  +--[FAIL]--> No collective advantage
                                                  |             |
                                                  |             v
                                                  |             Phase 5 still possible
                                                  |             (individual transfer)
                                                  |
                                                  +--[PASS]--> Phase 5: Panspermia
                                                                |
                                                                +--[FAIL]--> No transfer benefit
                                                                |             Digital panspermia
                                                                |             not validated
                                                                |
                                                                +--[PASS]--> Phase 6: Gate
                                                                              |
                                                                              v
                                                                              SuperCell v0 design
                                                                              Nano-LLM investigation
                                                                              HIVE-scale experiments
```

---

## Append-Only Change Log

| Date | Change |
|------|--------|
| 2026-02-27 | v2.0 — Initial creation. Post-TASK-1400B strategic realignment. 6 gated phases + 2 parallel tracks. Replaces TRL-based Paramecium MVP roadmap. Added Phase 5 (Panspermia), compute estimates, decision tree. |
| 2026-02-28 | v2.1 — Phase 2 status update: TASK-1605 gate FAILED (criterion 1). TASK-1606 sensor enrichment diagnostic in progress. Added Parallel Track: φ/Fibonacci Engineering (from PHI_FIBONACCI_BDC_ANALYSIS.md). Added Phase 2 decision tree branch for TASK-1606 outcomes. Compute topology documented (Queen orchestrator + Local PC GTX 1080 Ti + future MacBook M4 Pro via CF tunnel). |
| 2026-03-01 | v2.2 — ADR-0008 accepted: Phase 2 Criterion 1 revised from 5% to 3% absolute delta (95% CI). TASK-1607 5-sensor gate re-run (`N=30,G=50,P=100`) PASSED all criteria; Phase 2 marked COMPLETE and Phase 3 unblocked. |
| 2026-03-01 | v2.3 — ADR-0009 accepted: Phase 3 standard energy sweep (`TASK-1700-RUN`) formally closed as FAIL at current genome scale (`0/9` pass, mass extinction in `5/9`). Phase 4 unblocked via governance exception with fallback to proven Phase 2 penalty regime (`ADR-0005`, Regime B, `lambda=0.01`). |
| 2026-03-02 | v2.4 — ADR-0007 accepted: Phase 4 comparator fixed (old `collective - max_individual` retired as structurally biased under S1). Added reproducible N=30 re-analysis section (`A1/A2/A3`) and set interim Phase 4 status pending role-ablation + 2-task/3-task gate decision. |
| 2026-03-02 | v2.5 — TASK-1805 role-ablation completed on existing N=30 artifacts: necessity signal under 2-task MVP insufficient (`degrade>=5%` rates low, high interchangeability on entity ablation). Policy decision recorded: 3-task suite required before final Phase 4 gate PASS/FAIL. |
| 2026-03-02 | v2.6 — TASK-1806 3-task preparation complete: deterministic category proxy integrated and optional 3-task collective path wired with smoke validation. Full N=30 3-task gate + repeated ablation remains required before final Phase 4 verdict. |
| 2026-03-04 | v2.7 — ADR-0010 accepted: strict 3-task gate governance (`A1_3/A2_3/A3_3`, role necessity rule, no post-hoc threshold tuning without ADR). |
| 2026-03-04 | v2.8 — TASK-1811/1812 reproducible re-analysis completed on existing 3-task N=30 artifacts (no retraining). |
| 2026-03-04 | v2.9 — TASK-1813 official Phase 4 verdict recorded: `RUN COMPLETE`, `GATE FAIL` under ADR-0010. |
| 2026-03-04 | v2.10 — TASK-1899 baseline freeze established before Phase 4R redesign; no new full N=30 runs until root-cause + ADR-0011 + smoke gate. |
| 2026-03-04 | v2.11 — ADR-0011 accepted: minimal, flag-gated Phase 4R redesign protocol with pre-registered primary/fallback arms and smoke stop-rules. |
| 2026-03-04 | v2.12 — TASK-1903 smoke/determinism gate executed: both ADR-0011 arms failed stop-rule #3 (`gain_category_mean` stayed `0.0`), therefore no TASK-1904/TASK-1905 N=30 redesign run was authorized. |
| 2026-03-04 | v2.13 — ADR-0012 accepted: Phase 4R minimal redesign hypothesis formally closed; Phase 4 baseline verdict remains `RUN COMPLETE` / `GATE FAIL` under ADR-0010. |
| 2026-03-04 | v2.14 — ADR-0013 + EXP-0700 opened parallel Applied Track (GPU+CPU) with explicit paired-delta metrics and diagnostic/gate budgets; scientific Phase 4 verdict remains unchanged. |
| 2026-03-04 | v2.15 — Applied diagnostic N=10 completed: GPU pilot failed stability/CI stop-rule, CPU pilot passed; gate N=30 blocked by governance. |
| 2026-03-04 | v2.16 — ADR-0014 accepted for applied recovery iteration: numeric hardening + run-contract v3 + calibrated GPU profile, with unchanged ADR-0013 thresholds and explicit rerun stop-rules. |
| 2026-03-04 | v2.17 — Applied recovery diagnostic rerun N=10 completed: GPU technical crashes removed but statistical criterion still failed (`CI95_low(delta_gpu)<0`), CPU passed; gate N=30 remained blocked, Practical Readiness v2 = FAIL. |
| 2026-03-05 | v2.18 — ADR-0015 accepted (two-level fairness, token/examples budget parity). Applied v4 rerun results: GPU diagnostic PASS (`CI95_low>0`), GPU gate N=30 PASS with stable uplift; Practical Readiness v3 = PASS (parallel applied track only, scientific Phase 4 verdict unchanged). |
| 2026-03-05 | v2.19 — Phase-4 closure package executed (TASK-4100..4600): reference profile locked, robustness metric `negative_seed_rate` operationalized, negative-seed forensic artifacts generated, predeclared profile-space published, and reproducibility N=30 run passed (`CI95_low>0`, `negative_seed_rate<0.25`). Final report published at `reports/PHASE4_FINAL_REPORT.md`. Scientific verdict unchanged (`RUN COMPLETE / GATE FAIL`). |
| 2026-03-05 | v2.20 — Phase-4 hardening block completed (TASK-4700..5200): immutable reference lock guard, deterministic replay verification, environment fingerprint, dataset integrity manifest, Phase-4 provenance ledger, and isolated external reproducibility check documented. Scientific verdict and applied thresholds unchanged. |

---

## BDC Designer Applied Roadmap (2026-03-16)

A new applied roadmap was opened after the first real client case TextAI_Auto.

Reference:
- docs/project/BDC_DESIGNER_POST_TEXTAI_ROADMAP.md

Purpose:
- harden BDC Designer as a real client-facing architecture analysis system,
- support folder-based client evidence intake,
- separate historical prior evidence from current runtime truth,
- add logical redesign guidance and measurement-gap output.

This applied roadmap does **not** replace the scientific BDC roadmap above. It is a product-hardening companion track derived from live client evidence.
