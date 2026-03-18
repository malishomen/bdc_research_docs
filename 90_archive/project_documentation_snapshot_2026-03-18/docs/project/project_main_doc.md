# BIO-DIGITAL CORE (BDC) — Master Project Document

**Version:** 2.0  
**Date:** 2026-02-27  
**Status:** CANONICAL  
**Branch:** test  
**Supersedes:** `docs/project/BDC_PROJECT_MAIN_DOC.MD` (v1, Paramecium MVP focus)  
**Change Class:** R2 (hypothesis/strategy change)

---

## Current Mainline Product Status (2026-03-17)

`BDC Designer` is now the repository's current productized architecture-design subsystem and is frozen for merge to `main`.

Canonical freeze reference:
- `docs/project/BDC_DESIGNER_FREEZE_STATE.md`

Current operator/product references:
- `docs/BDC_CLI_V2_USER_GUIDE.md`
- `docs/BDC_CLIENT_PACKET_WORKFLOW.md`
- `docs/BDC_CLIENT_PRESENTATION_BRIEF.md`

Current state summary:
- deterministic decision core remains primary,
- packet-first and folder-intake workflows are operational,
- logical redesign guidance is part of the canonical output surface,
- TextAI-driven product hardening is integrated into the frozen line.

---

## 1. Project Identity

**BIO-DIGITAL CORE (BDC)** is a research-engineering program in digital biology.

| Attribute | Definition |
|-----------|-----------|
| **What BDC IS** | A disciplined framework for evolving digital organisms capable of adaptation, specialization, cooperation, and demonstrable real-world utility |
| **What BDC is NOT** | A machine learning classifier, an "AGI" project, a neural architecture optimization exercise, or artificial life simulation without measurable external purpose |
| **Core Innovation** | Quaternary logic S={T, F, MY, MN} with conflict_flag, enabling controlled abstention under uncertainty |
| **Discipline** | Strict engineering: TRL-gated validation, reproducibility by default, kill-criteria as law, N>=30 independent seeds for all claims |
| **Ultimate Test** | If the system is given Wikipedia, it must become measurably better at answering, reasoning, and transferring knowledge — not merely processing text statistically |

---

## 2. Mission

Build a self-evolving digital biology system where:

1. A seed organism (**SuperCell**) can be placed into an environment ("broth")
2. It produces adapted agents through evolution, mutation, and selection
3. Agents develop specialization and cooperation
4. Organisms extracted from one environment perform better in a new environment (**digital panspermia**)
5. The system demonstrates **measurable external utility** on real-world knowledge tasks

**This is not simulation for its own sake. This is digital biology that must work in the real world.**

---

## 3. Foundational Hypotheses

### Original Hypotheses (preserved from v1)

| ID | Hypothesis | Kill Criterion | Status |
|----|-----------|---------------|--------|
| H1 | Quaternary logic improves calibration and reduces false confidence | ECE/Brier improvement < 10% vs binary baseline | **UNTESTED** by canonical standard (no N>=30 experiment) |
| H2 | DNA-inspired memory yields scalable long context with exact recall | Exact recall < 99.9% on fixed test length | **PARTIALLY VALIDATED** (PiStream exact recall PASS; not at scale) |
| H3 | Self-replication/regeneration without error accumulation | Recovery rate < 70% on formalized small damage | **UNTESTED** by canonical standard |

### New Hypotheses (post-TASK-1400B)

| ID | Hypothesis | Kill Criterion | Requires ADR |
|----|-----------|---------------|-------------|
| H4 | Biological selection physics (resource-based, not linear parameter tax) enables architectural complexity growth | No complexity regime across 5 candidates allows v2-class architectures to be feasible (`required_accuracy <= 1.0`) | ADR-0005 |
| H5 | Organisms evolved in environment A adapt faster in environment B than organisms started from scratch | `time_to_threshold(transfer) >= time_to_threshold(de_novo)` across N>=30 seeds | ADR-0006 |
| H6 | Collective performance of specialized agents exceeds best single-agent performance | `collective_fitness <= best_individual_fitness` across N>=30 seeds | ADR-0007 |

---

## 4. Evidence Base — What We Have Proven (L0 Facts)

### 4.1 Evolution Engine (EDP1)

| Capability | Status | Evidence |
|------------|--------|----------|
| Deterministic evolution loop | PROVEN | Same seed -> same trajectory (verified across all experiments) |
| Multi-seed validation (N=30) | PROVEN | All major experiments use N=30 |
| Speciation mechanism | PROVEN | TASK-1102B: species_count > 10 stable, largest_species_fraction ~ 0.17-0.20 |
| Diversity shock | PROVEN | Plateau pushed from gen ~30 to gen 100 |
| Metrics integrity pipeline | PROVEN | TASK-1207: decomposition, errata system, regression tests |
| Genome v1 (LTF) baseline | PROVEN | max_accuracy_mean ~ 0.824, max_fitness_mean ~ 0.788 |
| Genome v2 (MRTN) representational capacity | PROVEN | best_single_accuracy > LTF ceiling; functional diversity 0.99 |
| Complexity barrier | PROVEN | TASK-1400B: required_accuracy_to_beat_v1 ~ 1.13 > 1.0 |

### 4.2 Wiki Pipeline

| Capability | Status | Evidence |
|------------|--------|----------|
| Deterministic data pipeline | PROVEN | simplified_wiki_v0, 278k docs |
| Cloze comprehension metric | PROVEN | TASK-0139 |
| Crash-safe training harness | PROVEN | Numeric progress policy, recovery |
| LM training stability | **FAIL** | entropy_collapse, perplexity 5.6e101 |

### 4.3 Infrastructure

| Capability | Status | Evidence |
|------------|--------|----------|
| HIVE distributed system | PROVEN | Queen server, drone protocol, viz dashboard |
| PiStream determinism | PROVEN | Bit-exact reproducibility across runs |
| Governance framework | PROVEN | 178 tasks tracked, 143 SUCCESS, append-only logs |
| Git artifact discipline | PROVEN | No binaries in repo, clean artifact policy |

### 4.4 What Failed

| Item | Status | Root Cause |
|------|--------|-----------|
| v2 (MRTN) fitness superiority | FAIL | Complexity penalty structurally prohibits victory (TASK-1400B) |
| v1.5 (interaction terms) | FAIL | Accuracy dropped to 0.812, penalty increased to 0.140 (TASK-1300) |
| Wiki LM pilot | FAIL | entropy_collapse — learning without understanding |
| Staged evolution (truth table freeze) | FAIL | Marginal change, max_fitness_mean 0.553->0.552 (TASK-1206) |
| H1, H2, H3 formal validation | NOT ATTEMPTED | No canonical N>=30 experiments with proper EXPERIMENT_SPEC |

---

## 5. The Critical Discovery: TASK-1400B

### The Mathematics

For v2 (MRTN) under current penalty model `fitness = accuracy - lambda * sum(|w|)` (lambda = 0.01):

```
final_max_complexity_mean(v2)  ~ 34.19
penalty_mean(v2)               ~ 0.3419
required_accuracy_to_beat_v1   ~ 1.13
```

Since accuracy is bounded within [0, 1], **v2 cannot beat v1 even with perfect accuracy**.

### What This Means

We created a digital world where:

- Architectural growth is linearly punished
- Complexity always loses to simplicity
- Composition (multicellularity) is forbidden by the laws of physics

This is **fundamentally incompatible** with:

- Biological evolution (which produces increasing complexity)
- The BDC mission (digital organisms that grow, specialize, cooperate)
- Digital panspermia (transfer requires adaptable, non-trivial organisms)

### The Biological Lesson

DNA does NOT optimize accuracy. It optimizes:

- **Survival** — homeostasis, not collapse
- **Replicability** — faithful copying
- **Structural integrity** — error correction, repair
- **Recovery** from mutations
- **Energy efficiency** — not parameter count minimization

Our fitness function `accuracy - lambda * sum(|w|)` is a machine learning regression metric, not a biological selection pressure. This is the **wrong physics** for a digital biology system.

---

## 6. Strategic Pivot

### From

Optimizing accuracy of linear classifiers on a synthetic boolean function (`hidden_rule`), competing genome versions (v1 vs v2) within a complexity regime that structurally forbids architectural growth.

### To

Building digital organisms that evolve under biologically-inspired selection pressures, adapt to information-rich environments (Wikipedia), and demonstrate measurable functional competence.

### What Changes

| Aspect | Before | After |
|--------|--------|-------|
| Task | `hidden_rule` (12-bit boolean) | Wiki-derived evolution tasks (cloze, inference) |
| Fitness | `accuracy - lambda * sum(\|w\|)` | Resource-bounded survival + task utility |
| Complexity cost | Linear penalty on parameter count | Energy budget (complexity costs energy, not fitness) |
| Success metric | accuracy / fitness | Functional competence + transfer + cooperation |
| Organism model | Genome-only (no metabolism/energy) | SuperCell (genome + energy + memory + communication) |
| Environment | Static boolean function | Dynamic information environment (Wikipedia corpus) |

### What Stays

- Evolution engine architecture (speciation, shock, determinism)
- Wiki pipeline infrastructure (simplified_wiki_v0, cloze metric)
- HIVE distributed system
- PiStream seed protocol
- Canon discipline (reproducibility, kill-criteria, N>=30)
- Governance (AGENTS.md, append-only logs, ADRs)
- H1-H3 as foundational hypotheses (to be tested within new architecture)

---

## 7. The Five Layers of BDC Architecture

```
+-----------------------------------------------+
|  Layer 5: META-GOAL                           |
|  Digital Panspermia, Collective Intelligence  |
+-----------------------------------------------+
|  Layer 4: ECOSYSTEM                           |
|  Multi-role populations, cooperation, HIVE    |
+-----------------------------------------------+
|  Layer 3: CELL                                |
|  SuperCell v0: genome + energy + memory       |
+-----------------------------------------------+
|  Layer 2: GENOME                              |
|  Modular architecture, mutation operators     |
+-----------------------------------------------+
|  Layer 1: PHYSICS OF SELECTION                |
|  Complexity regime, resource model, fitness   |
+-----------------------------------------------+
```

### Layer 1: Physics of Selection

The laws governing what survives and what dies. Must permit architectural growth.

**Current status:** BROKEN (TASK-1400B). Fix is Phase 1 of the roadmap.

**Key properties required:**
- Complexity growth must be possible (not structurally penalized)
- More complex organisms must be able to outcompete simpler ones when they are more effective
- The cost of complexity must be biological (energy/resources), not artificial (fitness subtraction)

### Layer 2: Genome

The encoding of organism behavior and structure.

**Current status:** Multiple representations proven (v1/LTF, v1.5/interaction, v2/MRTN). Representational capacity exists. Blocked by Layer 1.

**What exists:** RuleGenome (v1), RuleGenomeV1_5 (v1.5), MultiRuleGenome (v2) in `evolution/edp1_symbolic/genome.py`. Mutation operators, crossover (v2 subrule swap), speciation distance function.

### Layer 3: Cell (SuperCell v0)

The minimal digital organism. **Not a 9-component monolith** — components are added incrementally, one at a time, validated individually.

Minimal component set:

| Component | Purpose | Phase |
|-----------|---------|-------|
| **Genome** | Behavioral/architectural encoding | Exists (Layer 2) |
| **Energy** | Resource budget constraining computation | Phase 3 |
| **Memory** | State persistence across interactions | Phase 4+ |
| **Communication** | Signal exchange with other cells | Phase 4 |

Additional components (only after minimal set validated):

| Component | Purpose | Phase |
|-----------|---------|-------|
| Metabolism | Learning/processing capability | Phase 5+ |
| Membrane | Environment boundary / perception filter | Future |
| Replication control | Genome integrity during copying | Future |

**Current status:** Only genome (partial) exists. Each additional component requires its own validation experiment with kill criteria.

### Layer 4: Ecosystem

Population dynamics, role differentiation, collective fitness.

**Current status:** Speciation and diversity mechanisms proven. Collective fitness untested.

**What exists:** `speciation.py` (genome_distance, greedy clustering, per-species selection), diversity shock, lineage tracking.

### Layer 5: Meta-Goal (Digital Panspermia)

Transfer between environments, strengthening through diversity of experience.

**Current status:** Conceptual. No experiments. First test in Phase 5.

**Core thesis:** An organism evolved in environment A, when transferred to environment B, adapts faster than an organism started from scratch in B. After adaptation in B, the organism is "stronger" — it has gained capabilities that persist.

---

## 8. Bio-Inspired Design Principles

Analysis based on DNA engineering principles (OpenStax Biology source):

### Structural Analogies

| DNA Concept | BDC Analog | Engineering Principle |
|-------------|-----------|----------------------|
| Nucleotide (A, T, G, C) | Quaternary Logic (T, F, MY, MN) | Minimum information unit with built-in uncertainty handling |
| Sugar-Phosphate Backbone | Base architecture (evolution engine) | Rigid structural scaffold allowing internal variation |
| Complementary Pairing | HIVE Quorum protocol | Redundancy-based validation (2-of-3 agreement) |
| Antiparallel Chains | Dual Head (Language/Logic) | Separation of knowledge and decision functions |
| Histones / Nucleosomes | Tensor population vectorization | Compact representation for computational efficiency |

### Functional Analogies

| DNA Concept | BDC Analog | Engineering Principle |
|-------------|-----------|----------------------|
| Replication | Genome Blockchain | Cryptographic integrity chain for evolutionary lineage |
| Transcription / Translation | Genome Interpretability | Ability to "read" and understand organism decisions |
| Mutation + Natural Selection | Baldwin Effect (Hybrid Learning) | Evolution selects for learning ability, not just fixed behavior |
| Error Correction (DNA repair) | ECC / checksum in genome | Self-repair after damage (H3) |

### The Critical DNA Lesson

> DNA is minimalist but encodes enormous complexity through **structural organization**, not through more parameters.

Biology does not penalize complexity linearly by parameter count. Biology taxes **energy consumption**. A more complex organism succeeds if it uses its complexity efficiently — higher utility per unit energy.

**Canonical design principle:** Complexity is paid for with energy (resource consumption), not with direct fitness penalty proportional to parameter count.

### Biological Macromolecule Analogy for BDC Subsystems

| Biological Class | Function in Life | BDC Analog |
|-----------------|-----------------|------------|
| Carbohydrates | Quick energy source | Immediate computational budget per generation |
| Lipids | Long-term energy storage, membrane structure | Persistent state, environment boundary |
| Proteins | Diverse functional execution (enzymes, structure) | Genome-encoded behavioral strategies |
| Nucleic Acids (DNA/RNA) | Information storage and transfer | Genome encoding and replication protocol |

---

## 9. Success Criteria & Metrics Framework

### Operational Metrics (defined, measurable, reproducible)

| Metric | Definition | Baseline Required | Phase |
|--------|-----------|-------------------|-------|
| Cloze Accuracy | Fraction of correctly predicted masked tokens | Random predictor, frequency baseline | Phase 2 |
| Adaptation Speed | Generations to reach fitness threshold in new environment | De novo evolution (no transfer) | Phase 5 |
| Collective Advantage | Ratio of collective fitness to best individual fitness | Best single-agent performance | Phase 4 |
| Lineage Persistence | Fraction of founding lineages surviving N generations | Random extinction model | Phase 3+ |
| Functional Diversity | Unique prediction vector ratio in population | Monoclonal population | Phase 2+ |
| Energy Efficiency | Task utility per unit energy consumed | Random strategy energy cost | Phase 3 |
| Complexity Distribution | Variance and shape of complexity values across population | Uniform distribution | Phase 3 |
| Transfer Advantage | `time_to_adapt(de_novo) / time_to_adapt(transfer)` | De novo baseline in target environment | Phase 5 |

### Metrics NOT Yet Operationally Defined

These are proposed for future development. They may NOT be used for pass/fail decisions until formally specified.

| Proposed Metric | Status | Prerequisite |
|----------------|--------|-------------|
| Knowledge Graph Extraction Score | UNDEFINED | Formal extraction protocol + gold standard |
| Cross-Article Inference Score | UNDEFINED | Inference benchmark + scoring rubric |
| Task Transfer Score | UNDEFINED | Transfer protocol + baseline comparison |
| External Benchmark Comparison | UNDEFINED | Benchmark selection + access |
| Emergent Role Diversity | UNDEFINED | Role classification method + threshold |
| Stability Under Domain Shift | UNDEFINED | Domain shift protocol + degradation threshold |

**Canon rule:** No metric may be used for pass/fail decisions until it has: formula, baseline, threshold, reproducible measurement procedure, and ADR approval.

---

## 10. Relationship to Original Hypotheses

The strategic pivot does NOT abandon H1-H3. It **reframes** them within the digital biology context:

| Hypothesis | Original Context | New Context | Integration Point |
|-----------|-----------------|-------------|-------------------|
| H1 (Quaternary Logic) | Standalone calibration test on synthetic tasks | Cell's decision-making layer — "abstain" when uncertain about wiki cloze tasks | Phase 2: optional quaternary prediction layer in ClozeGenome |
| H2 (DNA-Memory) | Standalone exact recall test with PiStream | Cell's memory system — persistent knowledge across generations | Phase 3+: memory as resource within energy model |
| H3 (Self-Replication) | Standalone recovery test with formalized damage | Cell's integrity system — genome repair after transfer/mutation | Phase 5: repair during panspermia transfer |

**Required governance:**

- ADR-0004 must document the closure of `hidden_rule` line AND the relationship between closed line and ongoing H1-H3 validation within the new architecture
- H1-H3 are NOT closed. They are deferred to later phases where they can be tested in a meaningful context (real tasks, not toy boolean functions)
- If H1-H3 are never tested within the new architecture by Phase 6, they must be formally addressed (test or close via ADR)

---

## 11. Honest State Assessment

### What Works

- Evolution engine is production-quality (deterministic, reproducible, instrumented)
- Wiki pipeline produces clean, deterministic data (278k docs)
- HIVE infrastructure enables distributed computation
- Governance framework prevents self-deception (178 tasks tracked)
- Team has demonstrated ability to diagnose and correct errors (TASK-1202, TASK-1207)
- Kill-criteria discipline has been enforced consistently

### What Does Not Work

- Current fitness function structurally forbids complexity growth (TASK-1400B)
- Wiki LM training collapses catastrophically (entropy collapse)
- No organism has ever "understood" anything — all results are pattern matching
- `hidden_rule` is a toy task disconnected from real-world utility

### What Is Untested

- Whether ANY complexity regime enables v2 to beat v1
- Whether evolved strategies can outperform baselines on cloze tasks
- Whether energy-bounded evolution produces stable complexity distributions
- Whether collective performance exceeds individual performance
- Whether transfer between environments accelerates adaptation
- Whether H1 (quaternary logic) provides measurable calibration benefit
- Whether H3 (self-replication) works at canonical standard

### Key Risks

| Risk | Severity | Mitigation |
|------|----------|-----------|
| Complexity regime sweep finds nothing | HIGH | Kill criterion: if no regime works, problem is deeper than formula |
| Cloze task too hard for symbolic evolution | HIGH | Start with simplest genome; use baselines to calibrate expectations |
| Energy model collapses to trivial strategies | MEDIUM | Sweep energy parameters; kill criterion on distribution shape |
| Scope creep into 9-component SuperCell | HIGH | One component at a time; each with its own validation |
| Cathedral syndrome (grand architecture, no evidence) | HIGH | Gated phases; kill criteria at every gate |
| Wiki LM entropy collapse not diagnosed | MEDIUM | Parallel investigation track; does not gate main phases |

---

## 12. Experiment Documentation Layer

Key roadmap experiments must have a concept-level EXP document in `docs/experiments/` in addition to task-level reports.

Rules:
- Task reports (`reports/analysis/TASK-*`) remain the primary L0 execution evidence.
- EXP documents provide consolidated scientific interpretation across multiple tasks and ADRs.
- Naming and structure standard is defined in `docs/experiments/README.md`.

Current phase artifact:
- `docs/experiments/EXP-0300_COMPLEXITY_REGIME_SWEEP_2026-02-27.md` (Phase 1 complexity sweep summary).

---

## 13. Canonical References

| Document | Role | Priority (per AGENTS.md) |
|----------|------|--------------------------|
| `CANON.md` | Process rules (highest authority) | 1 |
| `SEMANTICS.md` | Value set definitions | 2 |
| `SEED_POLICY.md` | PiStream protocol | 2 |
| `KILL_CRITERIA.yaml` | Hypothesis kill criteria | 2 |
| `REPRODUCIBILITY.md` | Reproducibility contract | 2 |
| `VERSIONING.md` | Version control rules | 2 |
| `ARCHITECTURE.md` | System structure and invariants | 2 |
| `decisions/ADR-*` | Architecture decision records | 3 |
| `docs/GIT_ARTIFACT_POLICY.md` | Artifact management | 4 |
| `AGENTS.md` | Agent operational rules | 5 |
| `docs/project/BDC_PROJECT_MAIN_DOC.MD` | Predecessor document (v1) | Historical |
| `docs/project/BDC_ROADMAP_Paramecium_MVP_TRL-3.md` | Predecessor roadmap | Historical |

---

## 14. Document Governance

- **Version control:** This document is version-controlled in git on branch `test`
- **Change class:** R2 changes require ADR + roadmap revision
- **Supersedes:** `docs/project/BDC_PROJECT_MAIN_DOC.MD` for strategic direction and project identity
- **Does NOT supersede:** `CANON.md`, `SEMANTICS.md`, `ARCHITECTURE.md` (those have higher authority per AGENTS.md section 1)
- **Old documents preserved:** as historical artifacts; not deleted
- **Companion document:** `docs/project/project_roadmap.md` (operational execution plan)

### Append-Only Change Log

| Date | Change |
|------|--------|
| 2026-02-27 | v2.0 — Initial creation. R2 strategic realignment post-TASK-1400B. Pivot from classifier optimization to digital biology. Added H4-H6. Five-layer architecture model. Bio-inspired design principles from DNA analysis. |

---

## Current Applied Productization Track (2026-03-16)

After the first real client case TextAI_Auto, BDC opened a dedicated applied roadmap for BDC Designer hardening.

Reference:
- docs/project/BDC_DESIGNER_POST_TEXTAI_ROADMAP.md

This track focuses on:
- folder-based client packet intake,
- evidence-status-aware weighting,
- logical redesign guidance for current-runtime systems,
- automatic measurement-gap detection,
- repeatable client delivery flow.

The scientific project identity and core research hypotheses in this document remain unchanged. The new roadmap operationalizes the validated BDC core for real client delivery.
