# BIO-DIGITAL CORE (BDC) Architecture

**Version:** 1.0  
**Status:** CANONICAL  
**Last Updated:** 2026-01-27  
**Priority:** ABSOLUTE — This document has absolute priority over all other architectural documentation.

---

## Purpose

BIO-DIGITAL CORE (BDC) is a disciplined framework for building systems that handle uncertainty as a first-class computational state. BDC validates technical hypotheses through reproducible experiments, kill-criteria, and evidence-based development.

**Core Innovation:** Quaternary logic S={T, F, MY, MN} with conflict_flag, enabling controlled abstention without degrading computation chains.

---

## Task Classes

BDC operates on distinct task classes, each with specific constraints and validation requirements:

### Class 1: Core Validation (TRL 1-5)
- **Purpose:** Validate foundational hypotheses (H1, H2, H3)
- **Scope:** qcore, memory, agent, evolution, Paramecium MVP
- **Validation:** PiStream tests, exact recall, recovery rate
- **Hardware:** CPU/simulation only (no GPU until TRL5 closed)

### Class 2: Cognitive Co-Evolution (TRL 6-9)
- **Purpose:** Cognitive agents, self-organization, meta-cognition
- **Scope:** Cognitive frameworks, knowledge exchange, collective intelligence
- **Validation:** Fitness, diversity, emergence metrics
- **Hardware:** CPU/simulation; GPU allowed for acceleration (not core validation)

### Class 3: Knowledge Integration (TRL 10+)
- **Purpose:** Real-world data training, knowledge extraction
- **Scope:** Wikipedia corpus, neural architectures, population dynamics
- **Validation:** Comprehension, entity discovery, knowledge diversity
- **Hardware:** GPU-accelerated (exception to "no hardware until TRL5" with explicit justification)

**Critical Rule:** Infrastructure success (Class 2/3) does NOT imply cognitive success (Class 1). Each class must be validated independently.
**EDP1 Governance Rule (2026-02-27):** `hidden_rule` is no longer a product direction. It is a laboratory-only benchmark for controlled selection-physics checks; roadmap progress must come from new architectural lines.

---

## Organogram

```
BDC System
├── Core Layer (Class 1)
│   ├── qcore/          # Quaternary logic (S={T,F,MY,MN}, conflict_flag)
│   ├── memory/         # DNA-inspired memory (index, integrity, random access)
│   ├── env/            # Deterministic environment generation (ENV_PISTREAM)
│   ├── agent/          # Paramecium MVP (genome, VM, controller)
│   └── evolution/      # Evolutionary loop (MUT_DECISION, MUT_MAGNITUDE streams)
│
├── Cognitive Layer (Class 2)
│   ├── cognitive/      # Cognitive agents, co-evolution, self-organization
│   └── evolution/      # Advanced evolution (competition, transfer learning)
│
├── Knowledge Layer (Class 3)
│   ├── cognitive/      # TRL-10 GPU training, knowledge extraction
│   └── datasets/       # Real-world data (Wikipedia, etc.)
│
└── Infrastructure
    ├── experiments/    # Experiment specifications and protocols
    ├── decisions/      # Architecture Decision Records (ADRs)
    ├── docs/           # Documentation (protocols, policies, reports)
    └── scripts/        # Automation and verification tools
```

**EDP1 hidden_rule lab stand:** canonical baseline is `v1_speciation` (permanent reference); newer `hidden_rule` configurations are comparative lab probes, not target product milestones.

---

## Scaling Limits

### Agent Count Limits by Task Class

| Task Class | Max Agents | Rationale | Stop-Scaling Criteria |
|------------|-----------|-----------|----------------------|
| **Class 1 (Core)** | 30 (TRL-3) | Statistical validity (N≥30), deterministic PiStream | Signal-to-noise ratio < 0.1 |
| **Class 2 (Cognitive)** | 50 (TRL-8/9) | Co-evolution complexity, cluster formation | Diversity < 0.15, convergence > 95% |
| **Class 3 (Knowledge)** | 50 (TRL-10) | GPU memory constraints, population dynamics | GPU utilization < 50%, OOM errors |

### Population Governor

The **Population Governor** is a mandatory component that enforces agent count limits and stop-scaling criteria:

- **Function:** Monitor signal-to-noise ratio, diversity, convergence, resource utilization
- **Action:** Automatically stop scaling when criteria are met
- **Override:** Requires explicit ADR and justification

### Noise vs Signal Rules

- **Signal:** Measurable improvement in target metrics (fitness, recall, recovery)
- **Noise:** Variance, drift, random fluctuations
- **Threshold:** Signal-to-noise ratio must be ≥ 0.1 for continued scaling
- **Measurement:** Statistical tests (t-test, confidence intervals) required

---

## Autonomy Boundaries

### What BDC Can Do

1. **Answer questions** via collective cognition with confidence scores
2. **Express disagreement** when agents have conflicting beliefs
3. **Refuse impossible tasks** with explanation (see CANONICAL_LIMITS_AND_PROHIBITIONS.md)
4. **Request clarification** when uncertainty (MY/MN) is high
5. **Learn from feedback** through evolutionary and cognitive mechanisms

### What BDC Cannot Do

1. **Violate physics** (perpetual motion, energy creation, etc.)
2. **Guarantee outcomes** without evidence
3. **Operate without kill-criteria** validation
4. **Skip PiStream tests** for Class 1 tasks
5. **Store artifacts in git** (checkpoints, binaries, logs)

---

## Architectural Invariants

These invariants MUST be preserved across all changes:

1. **Reproducibility:** Same commit + same seeds + same environment → same results (within tolerances)
2. **Kill-criteria are law:** If a kill-criterion triggers, direction is closed or redefined
3. **Separation of contours:** qcore, memory, env, agent, evolution are isolated; no hidden dependencies
4. **Pi is deterministic only:** PiStream is a seed source, not a "magical meaning source"
5. **Evidence standard:** All claims require EXPERIMENT_SPEC.md, SEEDS.md, RUN_COMMANDS.md, RESULTS, REPORT.md
6. **No hardware until TRL5:** Exception for Class 3 (GPU) requires explicit ADR justification
7. **Infrastructure ≠ Cognitive:** Success in Class 2/3 does not validate Class 1 hypotheses
8. **Hidden_rule closure invariant:** EDP1 `hidden_rule` remains available only as a laboratory stand (benchmark/physics diagnostics). It must not be used as a strategic product endpoint.

---

## Relationship to Other Documents

- **CANON.md:** Process rules and discipline (referenced, not superseded)
- **RESEARCH_METHODOLOGY.md:** Formal research standard (implements ARCHITECTURE.md principles)
- **EVOLUTION_ENGINE.md:** Evolutionary mechanisms (implements Class 1/2 requirements)
- **CHECKPOINT_SYSTEM_V2.md:** Checkpoint architecture (implements artifact policy)
- **POPULATION_AND_SCALING.md:** Detailed scaling rules (implements limits above)
- **BDC_HIVE_ARCHITECTURE.md:** Distributed system (optional extension)
- **USER_INTERACTION_MODEL.md:** User-facing behavior (implements autonomy boundaries)
- **CANONICAL_LIMITS_AND_PROHIBITIONS.md:** Forbidden tasks (implements refusal rules)

---

## Change Control

Any change to this document requires:
1. **ADR** documenting the rationale
2. **Impact analysis** on all dependent documents
3. **Validation** that invariants are preserved
4. **Update** of all referencing documents

**Change Classes:**
- **R0:** Refactor (no numerical change; requires regression verification)
- **R1:** Method change (new experiment version)
- **R2:** Hypothesis/kill-criteria change (roadmap revision)

---

**ARCHITECTURE.md Status:** CANONICAL & OPERATIONAL  
**Next Review:** After major architectural changes or kill-criteria updates
