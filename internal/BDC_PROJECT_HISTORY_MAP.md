# BDC Project History Map

**Version:** 1.0  
**Date:** 2026-03-17  
**Status:** ACTIVE INTERPRETATION LAYER  
**Purpose:** Historical map of the BDC project from early digital-biology concepts through `BDC Designer` freeze.

---

## 1. Why This Document Exists

BDC has already passed through multiple identities:
- digital-biology concept,
- quaternary-logic and memory research program,
- `Paramecium / EDP1` experimental organism line,
- falsification and closure of the `hidden_rule` product path,
- restricted BDC theory,
- tooling and CLI,
- productized `BDC Designer`.

This document records that history as a single causal sequence so that future research does not restart from the wrong layer.

---

## 2. Reading Rule

This is an interpretation-layer map, not a replacement for canonical reports.

Primary source layers behind this map:
- `CANON.md`
- `docs/project/BDC_PROJECT_MAIN_DOC.MD`
- `docs/project/BDC_ROADMAP_Paramecium_MVP_TRL-3.md`
- `docs/EXPERIMENT_DNA_COMPRESSION.md`
- `docs/EXPERIMENT_QUATERNARY_LOGIC.md`
- `docs/EXPERIMENT_PISTREAM_V3.md`
- `docs/EXPERIMENT_EDP1_SYMBOLIC_RULE_EVOLUTION.md`
- `reports/analysis/TASK-1208-SCIENTIFIC-SNAPSHOT/EDP1_SCIENTIFIC_SNAPSHOT_1208.md`
- `reports/analysis/TASK-1400B-COMPLEXITY-AUDIT-ADDENDUM/TASK-1400B_BRIEF_REPORT.md`
- `decisions/ADR-0004-hidden-rule-closure.md`
- `decisions/ADR-0005-complexity-regime.md`
- `reports/analysis/TASK-6890-CAUSAL-ARCHITECTURE-DESIGN-RULEBOOK/TASK-6890_BRIEF_REPORT.md`
- `reports/analysis/TASK-6900-PAPER-READY-RESTRICTED-BDC-CONSOLIDATION/TASK-6900_BRIEF_REPORT.md`
- `reports/analysis/TASK-6980-BDC-TOOLING-PROTOTYPE/TOOL_SPEC.md`
- `reports/analysis/TASK-7020-BDC-DESIGNER-CLI/TASK-7020_BRIEF_REPORT.md`
- `reports/analysis/TASK-7550-BDC-CLI-V2-PRODUCTIZATION-AND-RELEASE/TASK-7550_BRIEF_REPORT.md`
- `docs/project/BDC_DESIGNER_FREEZE_STATE.md`

---

## 3. Executive Compression

The shortest accurate description of BDC history is:

1. BDC began as a digital-biology program built around quaternary logic, DNA-inspired memory, and an evolvable digital organism.
2. That program succeeded in building a reproducible evolution engine and proving several important engineering properties.
3. It then discovered a structural failure in its selection physics: the tested regime punished complexity so hard that architectural growth became mathematically impossible.
4. Instead of hiding this, the project converted the surviving useful core into a restricted theory of architecture priors and hybrid design guidance.
5. That restricted theory was then operationalized into `BDC Designer`.
6. `BDC Designer` became the first productized, client-facing subsystem to reach stable mainline status.

---

## 4. Phase Map

## Phase A — Genesis: Deep-Tech Biological Premise

### Core idea
BDC started as a serious attempt to build a digital-biology system rather than a generic AI tool.

The early premise combined:
- quaternary logic with explicit uncertainty states,
- DNA-inspired memory and encoding,
- deterministic streams (`PiStream`),
- and a future path toward digital organisms that adapt, specialize, replicate, and cooperate.

### Important early documents
- `docs/EXPERIMENT_QUATERNARY_LOGIC.md`
- `docs/EXPERIMENT_DNA_COMPRESSION.md`
- `docs/EXPERIMENT_PISTREAM_V3.md`
- `docs/project/BDC_PROJECT_MAIN_DOC.MD`
- `docs/project/BDC_ROADMAP_Paramecium_MVP_TRL-3.md`

### What mattered in this phase
- uncertainty was treated as a first-class computational state,
- memory was treated as an architectural subsystem,
- determinism and reproducibility were fixed very early,
- the project explicitly rejected hand-wavy AGI language.

### Phase verdict
This phase established the intellectual DNA of the whole project.
It did not yet produce a product, but it fixed the problem frame.

---

## Phase B — Embodiment: `Infusoria / Paramecium MVP`

### Core idea
The first concrete embodiment of the biological vision was `Paramecium MVP`, later operationalized through the `EDP1` symbolic evolution line.

### Engineering goal
Build a minimal digital organism stack with:
- environment,
- agent,
- genome,
- VM,
- deterministic mutation,
- selection,
- and measurable fitness.

### Important documents
- `docs/project/BDC_ROADMAP_Paramecium_MVP_TRL-3.md`
- `docs/EXPERIMENT_EDP1_SYMBOLIC_RULE_EVOLUTION.md`
- `EVOLUTION_ENGINE.md`
- `reports/analysis/TASK-1100-EDP1-SYMBOLIC-DIVERSITY-FIRST-SCAFFOLD/TASK-1100-EDP1_BRIEF_REPORT.md`

### What was really achieved
- deterministic evolution loop,
- fixed-seed reproducibility,
- N>=30 discipline,
- speciation,
- diversity shock,
- multiple genome versions,
- metrics decomposition and regression protection.

### Phase verdict
This was the first real engineering success of the project.
`Infusoria / EDP1` proved that BDC could build a disciplined experimental organism line.

---

## Phase C — Evidence Accumulation: EDP1 Maturity

### Core idea
The project moved from scaffold to measurement-heavy evolutionary analysis.

### Important sources
- `reports/analysis/TASK-1208-SCIENTIFIC-SNAPSHOT/EDP1_SCIENTIFIC_SNAPSHOT_1208.md`
- `docs/EDP1_METRICS_SPEC.md`
- `reports/analysis/TASK-1207C-FITNESS-DECOMPOSITION/TASK-1207C_BRIEF_REPORT.md`

### What became clear
- `v1_speciation` was the strongest validated baseline,
- `v2/MRTN` had higher representational capacity,
- but higher representational capacity did not translate into better fitness,
- decomposition discipline became necessary to understand why.

### Phase verdict
The project learned that “more expressive genome” is not enough.
The fitness physics and the architecture of selection matter more than representation alone.

---

## Phase D — Crisis: Complexity Barrier

### Core event
`TASK-1400B` established the decisive mathematical failure.

### Important sources
- `reports/analysis/TASK-1400-COMPLEXITY-AUDIT/TASK-1400_BRIEF_REPORT.md`
- `reports/analysis/TASK-1400B-COMPLEXITY-AUDIT-ADDENDUM/TASK-1400B_BRIEF_REPORT.md`

### What was proven
Under the legacy fitness regime:
- `fitness = accuracy - 0.01 * complexity`

the `v2` line became mathematically blocked:
- `required_accuracy_to_beat_v1 > 1.0`

### Why this mattered
This was not a normal failed experiment.
It was proof that the active selection physics structurally forbade complexity growth.

### Phase verdict
The old `hidden_rule` path could no longer honestly be treated as a product trajectory.

---

## Phase E — Governance Pivot: Closure Without Amnesia

### Core event
The project formally closed `hidden_rule` as a product direction while preserving it as a laboratory benchmark.

### Important sources
- `decisions/ADR-0004-hidden-rule-closure.md`
- `decisions/ADR-0005-complexity-regime.md`
- `docs/project/project_main_doc.md`
- `docs/project/project_roadmap.md`

### What was closed
- not all original hypotheses,
- not digital biology as a whole,
- but the specific product path built around `hidden_rule`.

### What was preserved
- `EDP1` as a benchmark and physics lab,
- determinism infrastructure,
- mutation/selection/speciation machinery,
- the discipline of explicit falsification.

### Phase verdict
The project survived because it accepted the falsification and preserved the useful parts.

---

## Phase F — Restricted Theory Formation

### Core idea
After the closure of the original active product line, BDC extracted a narrower and more defensible theory from the surviving positive results.

### Important sources
- `reports/analysis/TASK-6500-CAUSAL-LAW/TASK-6500_BRIEF_REPORT.md`
- `reports/analysis/TASK-6600-CAUSAL-ARCHITECTURE/TASK-6600_BRIEF_REPORT.md`
- `reports/analysis/TASK-6700-CAUSAL-DYNAMICS/TASK-6700_BRIEF_REPORT.md`
- `reports/analysis/TASK-6800-ROLE-DYNAMICS/TASK-6800_BRIEF_REPORT.md`
- `reports/analysis/TASK-6890-CAUSAL-ARCHITECTURE-DESIGN-RULEBOOK/TASK-6890_BRIEF_REPORT.md`
- `reports/analysis/TASK-6900-PAPER-READY-RESTRICTED-BDC-CONSOLIDATION/TASK-6900_BRIEF_REPORT.md`

### Key intellectual shift
BDC stopped trying to claim:
- universal transition-law portability,
- universal standalone dominance,
- or a single strong meta-law for all workflow families.

Instead it retained a restricted positive core:
- causal contribution matters,
- role weights can be predicted from task structure,
- architecture priors can be generated from causal geometry,
- hybrid use of those priors has practical value.

### Phase verdict
This was the scientific salvage phase.
The project transformed a broken universal theory attempt into a bounded, more credible architecture theory.

---

## Phase G — Public-Safe Consolidation

### Core idea
Before any tool/product spinout, the project explicitly froze what could be claimed and what had been falsified.

### Important sources
- `reports/analysis/TASK-6940-MANUSCRIPT-DRAFT-RESTRICTED-BDC/TASK-6940_BRIEF_REPORT.md`
- `reports/analysis/TASK-6960-SUBMISSION-READY-MANUSCRIPT-PACKAGE/TASK-6960_BRIEF_REPORT.md`
- `reports/analysis/TASK-7010-PUBLIC-RELEASE-PACKAGE/TASK-7010_BRIEF_REPORT.md`
- `reports/public_release/TASK-7010-PUBLIC-RELEASE-PACKAGE/PUBLIC_CLAIMS_SHEET.md`
- `reports/public_release/TASK-7010-PUBLIC-RELEASE-PACKAGE/SCOPE_STATEMENT_PUBLIC.md`

### What was achieved
- positive claims frozen,
- negative claims explicitly included,
- scope bounded,
- overclaim risk surfaced rather than hidden.

### Phase verdict
This phase made later productization possible without self-deception.

---

## Phase H — Tooling Spinout: `BDC Designer` v1

### Core idea
The restricted theory was converted into a practical tooling layer.

### Important sources
- `reports/analysis/TASK-6980-BDC-TOOLING-PROTOTYPE/TOOL_SPEC.md`
- `reports/analysis/TASK-7020-BDC-DESIGNER-CLI/TASK-7020_BRIEF_REPORT.md`
- `docs/BDC_DESIGNER_CLI_USAGE.md`
- `reports/analysis/TASK-7030-CASE-STUDY-REAL-DEPLOYMENT/TASK-7030_BRIEF_REPORT.md`
- `reports/analysis/TASK-7090-RELEASE-READY-CLI-BUNDLE/TASK-7090_BRIEF_REPORT.md`
- `reports/analysis/TASK-7110-REAL-TASK-VALIDATION-SUITE/TASK-7110_BRIEF_REPORT.md`
- `reports/analysis/TASK-7140-BDC-V1-RELEASE-CANDIDATE/TASK-7140_BRIEF_REPORT.md`
- `docs/BDC_V1_RELEASE_NOTES.md`

### What v1 really was
Not a universal design engine.
It was a restricted CLI that:
- consumed task descriptors,
- emitted role count and strategy priors,
- exposed caution flags,
- and worked best as part of a hybrid workflow.

### Why it mattered
This was the first product-like operational form of BDC.

### Phase verdict
`BDC Designer v1` was the first credible commercializable surface extracted from the research program.

---

## Phase I — Commercial and Client Operating Layer

### Core idea
The project then built the commercial shell around the tool:
- pilots,
- proof assets,
- GTM,
- vertical packaging,
- outreach,
- qualification,
- customer proof loops.

### Representative artifact families
- `docs/BDC_PILOT_PROGRAM.md`
- `docs/BDC_PAID_PILOT_POLICY.md`
- `docs/BDC_CUSTOMER_PROOF_SYSTEM.md`
- `docs/BDC_CLIENT_PRESENTATION_BRIEF.md`

### What changed here
BDC stopped behaving like only a research program and became:
- a pilotable product,
- a structured commercial offer,
- a system that could enter real buyer conversations.

### Phase verdict
This phase operationalized the business edge of the product but did not yet fully solve real packet intake and redesign guidance.

---

## Phase J — TextAI Trigger and v2 Hardening

### Core event
`TextAI_Auto` became the first serious client-like case that exposed the real operating mode of `BDC Designer`.

### What TextAI taught the project
- client packets arrive as folders, not clean native schema objects,
- evidence is mixed:
  - `measured`
  - `measured_from_historical_report`
  - `inferred`
  - `missing`
- clients need redesign guidance, not only winner ranking,
- historical prior and current runtime truth can diverge sharply,
- raw interpretation quality matters.

### Important sources
- `bdc_real_use_packets/BDC_CLI_V2_IMPLEMENTATION_PLAN.md`
- `reports/analysis/TASK-7440-BDC-CLI-V1-BASELINE-FREEZE/TASK-7440_BRIEF_REPORT.md`
- `reports/analysis/TASK-7550-BDC-CLI-V2-PRODUCTIZATION-AND-RELEASE/TASK-7550_BRIEF_REPORT.md`
- `docs/project/BDC_DESIGNER_POST_TEXTAI_ROADMAP.md`
- `docs/BDC_CLIENT_PACKET_WORKFLOW.md`

### What v2 added
- packet schema,
- validator and quality engine,
- real role ontology,
- evidence-aware scoring,
- strategy engine,
- confidence and diagnostics,
- explanation layer,
- LLM adapter as interpreter,
- benchmark suite,
- client bundle workflow,
- folder intake mode,
- redesign mode,
- measurement gap detection,
- sparse runtime evidence support.

### Phase verdict
This is where `BDC Designer` became a real client-operable system rather than a bounded prototype.

---

## Phase K — Freeze and Mainline

### Core event
The current `BDC Designer` line was frozen and merged as the mainline-ready subsystem.

### Important sources
- `docs/project/BDC_DESIGNER_FREEZE_STATE.md`
- `docs/releases/RELEASE_NOTES_MAIN_MERGE_2026-03-17_BDC_DESIGNER_FREEZE.md`

### What is frozen
- deterministic decision core,
- packet-first and folder-intake workflow,
- redesign guidance,
- confidence split,
- client bundle generation,
- claim-safe client/operator surfaces.

### Phase verdict
`BDC Designer` is now the current operational core of the repository.

---

## 5. Pivot Points

## Pivot 1 — From Concept to Experimental Organism

**From:** abstract quaternary / DNA-inspired concepts  
**To:** `Paramecium / EDP1`

Why it mattered:
- converted ideas into measurable engineering.

---

## Pivot 2 — From “more complex genome” optimism to complexity falsification

**From:** belief that richer representation will eventually win  
**To:** proof that current selection physics blocks architectural growth

Why it mattered:
- ended naive continuation of the old path.

---

## Pivot 3 — From universal ambition to restricted theory

**From:** broad biological/universal framing  
**To:** bounded, falsification-aware architecture theory

Why it mattered:
- preserved credibility and made productization possible.

---

## Pivot 4 — From theory to tooling

**From:** manuscript/rulebook/restricted claims  
**To:** descriptor-driven tool and CLI

Why it mattered:
- created the first practical operator surface.

---

## Pivot 5 — From CLI to client workflow system

**From:** architecture-prior tool  
**To:** evidence packet intake + redesign guidance + client bundle

Why it mattered:
- turned BDC into a real architecture partner workflow.

---

## 6. What Persisted Across All Phases

These themes survived every pivot:
- reproducibility over rhetoric,
- deterministic infrastructure,
- explicit uncertainty handling,
- anti-overclaim discipline,
- respect for failure as evidence,
- architecture as something that should be derived, not guessed.

This continuity matters: `BDC Designer` is not a random business pivot. It is a downstream operationalization of the same deep project principles.

---

## 7. What Was Truly Abandoned

These things were not merely postponed; they were effectively abandoned in their original form:
- treating the `hidden_rule` line as the direct product path,
- pretending linear complexity penalty was acceptable biological physics,
- claiming universal transition-law portability,
- claiming standalone BDC dominance over all engineering baselines.

---

## 8. What Was Preserved and Converted

The following survived and were transformed into `BDC Designer`:
- causal contribution thinking,
- role-weight emergence,
- coordination-cost sensitivity,
- explicit failure-mode mapping,
- bounded confidence,
- hybrid-search discipline,
- negative-result awareness.

In short:
the biological program lost its original delivery path, but its strongest design principles were distilled into a usable architecture system.

---

## 9. Current Interpretation

The project now has two distinct but causally connected lines:

### Line 1 — Operational line
`BDC Designer`

This is:
- productized,
- client-facing,
- mainline-ready,
- and already evidence-bearing.

### Line 2 — Research frontier
Original digital-biology / SuperCell ambition

This is:
- not dead,
- but no longer allowed to continue by inertia from the old `hidden_rule` path.

Any reboot of the scientific line must start from the historical lessons captured here.

---

## 10. Why This Map Matters for Reboot

Without this history map, a reboot would likely repeat one of three mistakes:

1. rebuilding the old organism line under the same broken selection physics,
2. forgetting that restricted BDC was created to preserve truth under falsification,
3. treating `BDC Designer` as a distraction instead of the most operationally mature descendant of the original program.

This document exists to prevent exactly those mistakes.

