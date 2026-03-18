# Canonical Documents Map - Bio_Digital_Core

**Version:** 2.0  
**Last Updated:** 2026-01-27  
**Purpose:** Complete inventory and relationship mapping of all canonical documents for architectural analysis

---

## Document Classification

### ARCHITECTURE (Core Definitions)

**Root Documents:**
- **`CANON.md`** - **ROOT DOCUMENT** - Single source of truth for process rules and discipline
  - Defines: Main principles, evidence standards, change control, canonical structure
  - Referenced by: All other documents
  - Status: ACTIVE

- **`docs/project/BDC_PROJECT_MAIN_DOC.MD`** - Main project documentation
  - Expands on: CANON.md
  - Contains: Scientific rationale, formal model, hypotheses, TRL roadmap
  - Status: ACTIVE

- **`SEMANTICS.md`** - Value semantics definition
  - Defines: S = {T, F, MY, MN}, conflict_flag semantics
  - Referenced by: qcore implementations, experiment specs
  - Status: ACTIVE

- **`VERSIONING.md`** - Versioning rules
  - Defines: Change classes (R0, R1, R2), experiment versions, TRL versions
  - Status: ACTIVE (with UNVERIFIED/TODO items)

**Supporting Architecture:**
- **`docs/project/CANON_DISCIPLINE_SOURCE_RU.md`** - Original Russian canonical discipline source
- **`docs/project/Каноническая дисциплина реализации проекта BDC.md`** - Russian canonical implementation discipline
- **`docs/project/BDC_ROADMAP_Paramecium_MVP_TRL-3.md`** - TRL-3 roadmap
- **`docs/project/BDC_EXTENSIONS_PACK_BEP-1.md`** - BEP-1 extensions pack
- **`docs/project/PHASE_TRL-7 (WIKI-ADAPTATION).MD`** - TRL-7 phase documentation

### PROTOCOLS (Operational Specifications)

- **`docs/COGNITIVE_PROTOCOL.md`** - TRL-8 canonical knowledge exchange protocol
  - Version: 0.8.1
  - Defines: Knowledge package format, transfer protocol, belief updating, social learning
  - Status: CANONICAL & OPERATIONAL
  - Related: TRL8_SPECIFICATION.md

- **`docs/TRL8_SPECIFICATION.md`** - TRL-8 Cognitive Co-Evolution Framework specification
  - Version: 0.8.1-trl8-bootstrap
  - Defines: Cognitive agent architecture, co-evolutionary environment, self-organization
  - Status: ACTIVE
  - Related: COGNITIVE_PROTOCOL.md

- **`docs/WP7.5_SPECIFICATION.md`** - WP7.5 Advanced Evolution Experiments specification
  - Version: 1.0
  - Defines: Competition manager, transfer matrix, 200-episode framework
  - Status: SPECIFICATION PHASE

- **`docs/b4_bus_protocol.md`** - B4 bus protocol specification
- **`docs/simulation_toolchain.md`** - Simulation toolchain documentation (Icarus Verilog)

### POLICIES (Rules and Constraints)

- **`docs/GIT_ARTIFACT_POLICY.md`** - Git artifact storage policy
  - Defines: What can/cannot be stored in git, size limits
  - Status: ACTIVE

- **`docs/TRAINING_RUNTIME_RULES.md`** - Training runtime rules
  - Defines: Checkpoint handling, external storage requirements
  - Status: ACTIVE

- **`SEED_POLICY.md`** - PiStream seed policy
  - Defines: Stream separation (ENV, INIT, NOISE, MUT_DECISION, MUT_MAGNITUDE, QUERY)
  - Status: ACTIVE

- **`REPRODUCIBILITY.md`** - Reproducibility requirements
  - Defines: Toolchain versions, deterministic seeding, experiment protocol
  - Status: ACTIVE

- **`docs/SEED_POLICY.md`** - Duplicate/alternative seed policy (if exists)

### EXPERIMENTS (Experimental Data and Specifications)

**Experiment Specifications:**
- **`experiments/exp_0001_h1_calibration/EXPERIMENT_SPEC.md`** - H1 calibration experiment
- **`experiments/exp_0001_h1_calibration/RUN_COMMANDS.md`** - Run commands for exp_0001
- **`experiments/exp_0002_memory_validation/EXPERIMENT_SPEC.md`** - Memory validation experiment
- **`experiments/exp_0002_memory_validation/RUN_COMMANDS.md`** - Run commands for exp_0002
- **`experiments/exp_0003_h2_seed_paramecium/EXPERIMENT_SPEC.md`** - Seed Paramecium experiment
- **`experiments/exp_0003_h2_seed_paramecium/RUN_COMMANDS.md`** - Run commands for exp_0003
- **`experiments/exp_0004_multigeneration/EXPERIMENT_SPEC.md`** - Multigeneration experiment
- **`experiments/exp_0004_multigeneration/RUN_COMMANDS.md`** - Run commands for exp_0004
- **`experiments/exp_0006_wiki_adaptation/EXPERIMENT_SPEC.md`** - Wiki adaptation experiment
- **`experiments/exp_0007_pistream_v3_phase0_sweep/EXPERIMENT_SPEC.md`** - PiStream v3 Phase-0 sweep (canonical, aligned to SEED_POLICY.md)
- **`experiments/exp_0008_quaternary_router_skeleton/EXPERIMENT_SPEC.md`** - Quaternary Router skeleton (deterministic routing, no GPU execution)
- **`experiments/exp_0009_kc1_diagnostics/EXPERIMENT_SPEC.md`** - KC1 diagnostics for exp_0007 dead configs (CPU-only evidence)
- **`experiments/exp_0010_kc1_variants_evaluation/EXPERIMENT_SPEC.md`** - KC1 variants evaluation (pre-registered, CPU-only)
- **`experiments/exp_0011_pistream_v3_phase0_vnext_kc1_ttt/EXPERIMENT_SPEC.md`** - Phase-0 vNext with KC1_TTT (time-to-threshold)
- **`experiments/exp_0012_kc2_diagnostics/EXPERIMENT_SPEC.md`** - KC2 diagnostics (CPU-only, no tuning)

### REPORTS (Logs and Status Reports)

- **`WEEKLY_STATUS.md`** - **PRIMARY STATUS TRACKER** - Accumulated phase and task reports
  - Format: Append-only ## sections
  - Contains: TRL-6 through TRL-10.1 execution summaries
  - Status: ACTIVE

- **`AGENTS_LOG.md`** - **PRIMARY EXECUTION LOG** - Canonical log of all agent executions
  - Format: Append-only table with timestamps, task IDs, results, artifacts
  - Status: ACTIVE

- **`EXECUTION_SUMMARY_TRL10_1.md`** - TRL-10.1 execution summary
  - Contains: 8-hour Wikipedia training execution details
  - Status: COMPLETE

- **`reports/AUDIT_INDEPENDENT_EXPERTISE_2026_01.md`** - Independent audit report
  - Contains: Analysis of canonical hypotheses vs. actual TRL 7-10 results
  - Status: COMPLETE

- **`reports/GIT_TAGS_AND_BLOAT_AUDIT.md`** - Git tags and bloat audit
- **`reports/TRL10_1_FINAL_REPORT.txt`** - TRL-10.1 final report (text format)
- **`docs/GITHUB_SETTINGS_REPORT_2026-01-07.md`** - GitHub settings report
- **`docs/REPO_AUDIT_REPORT_2026-01-07.md`** - Repository audit report

### DECISIONS (Architecture Decision Records)

- **`decisions/ADR-0001-docs-sources-of-truth.md`** - ADR: Documentation sources of truth
  - Date: 2026-01-07
  - Decision: Canonical files in root, reference files in docs/project/

- **`decisions/ADR-0002-bep1-scope-gating.md`** - ADR: BEP-1 scope gating
- **`decisions/ADR-0003-append-only-agents-weekly.md`** - ADR: Append-only agents/weekly logs

### ARCHITECTURE (New Canonical Documents - 2026-01-27)

- **`ARCHITECTURE.md`** - **ROOT ARCHITECTURAL DOCUMENT** - Constitutional document defining purpose, task classes, organogram, scaling limits, autonomy boundaries, architectural invariants
  - Priority: ABSOLUTE (all other docs reference this)
  - Status: CANONICAL & OPERATIONAL
  - Created: 2026-01-27

- **`RESEARCH_METHODOLOGY.md`** - Formal research standard
  - Defines: Kill-criteria, PiStream validation, infrastructure vs cognitive success separation
  - Status: CANONICAL & OPERATIONAL
  - Created: 2026-01-27

- **`EVOLUTION_ENGINE.md`** - Evolutionary mechanisms
  - Defines: Mutation strength, selection pressure, diversity enforcement, PiStream v1 stagnation root cause
  - Status: CANONICAL & OPERATIONAL
  - Created: 2026-01-27

- **`CHECKPOINT_SYSTEM_V2.md`** - Sharded checkpoint architecture
  - Defines: V2 design, TRL-10.1 failure acknowledgment, resume-safe checkpoints
  - Status: CANONICAL & OPERATIONAL
  - Created: 2026-01-27

- **`POPULATION_AND_SCALING.md`** - Population limits and scaling
  - Defines: Agent count limits by task class, Population Governor, stop-scaling criteria
  - Status: CANONICAL & OPERATIONAL
  - Created: 2026-01-27

- **`BDC_HIVE_ARCHITECTURE.md`** - Distributed island-model architecture
  - Defines: Queen/Drone roles, minimal-trust API, redundancy validation, client boundaries
  - Status: CANONICAL (DESIGN PHASE)
  - Created: 2026-01-27

- **`USER_INTERACTION_MODEL.md`** - User-facing behavior
  - Defines: Collective cognition, confidence, disagreement, refusal of impossible tasks
  - Status: CANONICAL & OPERATIONAL
  - Created: 2026-01-27

- **`CANONICAL_LIMITS_AND_PROHIBITIONS.md`** - Forbidden tasks
  - Defines: Explicit list of impossible tasks and how BDC explains impossibility
  - Status: CANONICAL & OPERATIONAL
  - Created: 2026-01-27

### EXPERIMENTS (Next-Generation Research Directions - 2026-01-27)

- **`docs/EXPERIMENT_PISTREAM_V3.md`** - PiStream v3 Diversity-First Evolution architecture
  - Defines: Three-phase evolution (Diversity Accumulation → Evolution with Selection → Stabilization)
  - Status: SPECIFICATION
  - Created: 2026-01-27
  - Related: PiStream v2.x (CLOSED), ARCHITECTURE.md, EVOLUTION_ENGINE.md
  - Priority: HIGH (mandatory after v2.x closure)

- **`docs/EXPERIMENT_QUATERNARY_LOGIC.md`** - Quaternary logic delayed decision architecture
  - Defines: Four states (YES/NO/MAYBE_YES/MAYBE_NO), GPU exploration + CPU orchestration
  - Status: RESEARCH SPECIFICATION
  - Created: 2026-01-27
  - Related: SEMANTICS.md, qcore/, ARCHITECTURE.md
  - Priority: MEDIUM (separate research direction)

- **`docs/EXPERIMENT_DNA_COMPRESSION.md`** - DNA-inspired memory compression research
  - Defines: Hierarchical encoding, latent representations, mutational deltas, storage/computation separation
  - Status: RESEARCH SPECIFICATION
  - Created: 2026-01-27
  - Related: memory/, ARCHITECTURE.md, EVOLUTION_ENGINE.md
  - Priority: MEDIUM (separate research direction)

- **`docs/EXPERIMENT_VISUALIZATION_PACMAN.md`** - Pac-Man learning visualization metaphor
  - Defines: Real-time visualization using Pac-Man game metaphor, quaternary state colors
  - Status: UX SPECIFICATION
  - Created: 2026-01-27
  - Related: ui/, ARCHITECTURE.md, WEEKLY_STATUS.md
  - Priority: LOW (infrastructure tool, optional)

- **`docs/BDC_HIVE_COMPUTE_MODEL.md`** - CPU Queen + GPU Drones compute model extension
  - Defines: Web interface for task submission, pre-installed GPU configs, user resource limits
  - Status: ARCHITECTURE EXTENSION
  - Created: 2026-01-27
  - Related: BDC_HIVE_ARCHITECTURE.md, ARCHITECTURE.md, POPULATION_AND_SCALING.md
  - Priority: MEDIUM (optional extension, post-core validation)

---

## Document Relationships

### Dependency Graph

```
ARCHITECTURE.md (ABSOLUTE PRIORITY - ROOT ARCHITECTURAL DOCUMENT)
    ├─→ RESEARCH_METHODOLOGY.md (implements ARCHITECTURE.md principles)
    ├─→ EVOLUTION_ENGINE.md (implements Class 1/2 requirements)
    ├─→ CHECKPOINT_SYSTEM_V2.md (implements artifact policy)
    ├─→ POPULATION_AND_SCALING.md (implements scaling limits)
    ├─→ BDC_HIVE_ARCHITECTURE.md (optional extension)
    ├─→ USER_INTERACTION_MODEL.md (implements autonomy boundaries)
    └─→ CANONICAL_LIMITS_AND_PROHIBITIONS.md (implements refusal rules)

CANON.md (PROCESS ROOT - referenced by ARCHITECTURE.md)
    ├─→ SEMANTICS.md (defines value semantics)
    ├─→ SEED_POLICY.md (defines seeding)
    ├─→ REPRODUCIBILITY.md (defines reproducibility)
    ├─→ VERSIONING.md (defines versioning)
    ├─→ BDC_PROJECT_MAIN_DOC.MD (expands architecture - historical)
    │   ├─→ TRL8_SPECIFICATION.md (implements cognitive layer)
    │   │   └─→ COGNITIVE_PROTOCOL.md (defines knowledge exchange)
    │   └─→ WP7.5_SPECIFICATION.md (defines evolution experiments)
    ├─→ ADR-0001 (defines doc structure)
    ├─→ GIT_ARTIFACT_POLICY.md (defines artifact storage)
    └─→ TRAINING_RUNTIME_RULES.md (defines runtime rules)

WEEKLY_STATUS.md (tracks progress)
    ├─→ References all TRL phases
    └─→ Links to experiment results

AGENTS_LOG.md (execution log)
    ├─→ References all tasks and commits
    └─→ Links to artifacts and results
```

### Relationship Types

- **ROOT** - CANON.md is the foundational document
- **EXPANDS** - BDC_PROJECT_MAIN_DOC.MD expands on CANON.md
- **IMPLEMENTS** - TRL8_SPECIFICATION.md implements concepts from CANON.md
- **DEFINES** - Protocol documents define operational procedures
- **TRACKS** - WEEKLY_STATUS.md and AGENTS_LOG.md track execution
- **VALIDATES** - Experiment specs validate hypotheses from CANON.md
- **MODIFIES/CLARIFIES** - ADRs modify or clarify architectural aspects

### Historical Evolution

1. **Initial Phase (TRL-2 to TRL-3):**
   - CANON.md, SEMANTICS.md, SEED_POLICY.md established
   - Basic qcore and memory modules
   - Paramecium MVP experiments

2. **Evolution Phase (TRL-4 to TRL-6):**
   - Memory validation experiments
   - Multigeneration evolution
   - Adaptive mutation mechanisms

3. **Real Data Phase (TRL-7):**
   - WikiText-2 integration
   - Data pipeline validation
   - Neuro-evolution integration

4. **Advanced Evolution (WP7.5):**
   - Competition manager
   - Transfer learning
   - Extended experiments

5. **Cognitive Phase (TRL-8):**
   - Cognitive agents with reasoning
   - Co-evolutionary environment
   - Self-organization system

6. **Meta-Cognitive Phase (TRL-9):**
   - Meta-reflection capabilities
   - Autonomous reflection experiments

7. **Real-World Training (TRL-10):**
   - Full Wikipedia corpus training
   - Knowledge integration

---

## Document Status Summary

| Category | Count | Status |
|----------|-------|--------|
| ARCHITECTURE | 9 | All active |
| PROTOCOLS | 5 | All active/canonical |
| POLICIES | 5 | All active |
| EXPERIMENTS | 9+ | Various completion states |
| NEXT-GEN EXPERIMENTS | 5 | Specification phase (2026-01-27) |
| REPORTS | 7 | Complete/active |
| DECISIONS | 3 | Complete |
| **TOTAL** | **43+** | |

---

## Notes for Architectural Analysis

1. **Canonical Hierarchy:**
   - CANON.md is the absolute root
   - All other documents derive authority from CANON.md
   - ADRs modify canonical rules

2. **Evidence Standard:**
   - All claims require EXPERIMENT_SPEC.md, SEEDS.md, RUN_COMMANDS.md, RESULTS
   - Kill-criteria are law (from CANON.md)
   - Reproducibility is mandatory

3. **TRL Progression:**
   - TRL-2: qcore verification
   - TRL-3: Paramecium MVP
   - TRL-4: Memory validation
   - TRL-5: Multigeneration
   - TRL-6: Adaptive mutation
   - TRL-7: Wiki adaptation
   - TRL-8: Cognitive co-evolution
   - TRL-9: Meta-cognition
   - TRL-10: Real-world training

4. **Key Innovations:**
   - Quarternary logic (T, F, MY, MN) with conflict_flag
   - PiStream deterministic seeding
   - DNA-inspired memory architecture
   - Cognitive co-evolution framework
   - Self-organization emergence
   - Diversity-First Evolution (PiStream v3)
   - GPU exploration + CPU orchestration (Quaternary Logic)
   - DNA-inspired compression (hierarchical, latent, deltas)
   - Distributed compute model (CPU Queen + GPU Drones)

5. **Critical Policies:**
   - Git artifact policy (no checkpoints, no binaries >50MB)
   - Append-only logs (WEEKLY_STATUS.md, AGENTS_LOG.md)
   - Single source of truth (ADR-0001)

---

**Document Map Status:** COMPLETE  
**Last Inventory:** 2026-01-27  
**Next-Gen Experiments Added:** 2026-01-27 (PiStream v3, Quaternary Logic, DNA Compression, Visualization, HIVE Compute Model)  
**Next Review:** After major architectural changes
