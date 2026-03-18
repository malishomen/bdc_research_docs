# BDC Client Presentation Brief

## Purpose
This document is a professional presentation brief for creating a client-facing slide deck about `BDC Designer`.

The presentation must explain the system clearly to technical and business stakeholders without overstating unsupported results.

Primary use cases:
- partner introduction
- enterprise architecture call
- pilot qualification
- technical buyer education
- paid architecture audit positioning

---

## 1. Positioning

### What BDC Designer is
`BDC Designer` is a decision system for cooperative AI architecture design.

It does not train models.
It does not replace the underlying LLM.
It does not claim universal optimization.

It analyzes workflow structure, evidence from tested variants, and current runtime behavior to recommend:
- how many logical roles a system should use,
- which roles should exist,
- how to structure planner/editor/guardian/orchestrator behavior,
- what strategy mode to use,
- what evidence is still missing before stronger deployment claims are made.

### What BDC Designer is not
Do not position it as:
- AGI
- autonomous software engineer replacement
- prompt generator
- generic chatbot builder
- black-box architecture oracle
- "one-click best AI system"

### One-line description
`BDC Designer helps teams design and validate multi-agent AI workflows from task structure and measured evidence instead of architecture guesswork.`

---

## 2. Audience

Primary audience:
- CTO
- Head of AI
- AI engineering lead
- workflow automation owner
- technical founder with multi-stage AI process risk

Secondary audience:
- product lead for AI workflows
- innovation lead
- pilot sponsor

Non-fit audience:
- teams looking for a simple one-prompt chatbot
- buyers expecting magic without baseline metrics
- non-technical buyers with no workflow ownership

---

## 3. Core Client Problem

The presentation must frame the problem this way:

Most teams build cooperative AI systems by layering prompts, gates, and tools until the workflow becomes hard to reason about.

This creates recurring failures:
- too many stages with unclear role boundaries
- expensive coordination overhead
- wrong prompt family in the wrong slice
- safety gates that are either too weak or too blunt
- no clean link between architecture choice and measured outcome

BDC Designer exists to reduce that architectural guesswork.

---

## 4. What Must Be Claimed

These are the claim-safe pillars to present.

### Claim 1 — Architecture prior, not architecture fantasy
BDC Designer can recommend a disciplined logical architecture prior for a multi-agent or staged AI workflow.

### Claim 2 — Evidence-aware guidance
BDC Designer separates:
- historical evidence
- current runtime evidence
- inferred structure
- missing measurements

### Claim 3 — Redesign guidance, not only ranking
BDC Designer can output:
- winner prior
- logical redesign guidance
- measurement gaps
- client-facing redesign memo

### Claim 4 — Practical client workflow
BDC Designer can ingest a client evidence folder and produce a normalized packet, recommendation, redesign output, and follow-up measurement request.

### Claim 5 — Scope discipline
BDC Designer can explicitly say when confidence is limited and when a stronger claim is not yet justified.

---

## 5. What Must Not Be Claimed

Do not claim:
- universal best architecture for all workflows
- guaranteed lift
- automatic production optimization
- model-level intelligence gains
- zero-human architecture selection
- that BDC replaces experimentation

Do not present a pilot or experiment as broader proof than the measured evidence supports.

---

## 6. System Description for Clients

### Inputs BDC consumes
The presentation must show that BDC works from structured evidence, not vibes.

Typical inputs:
- workflow description
- tested architecture variants
- current runtime role mapping
- slice-level metrics
- failure registry
- prompt/stage matrix
- design priorities
- deployment truth

### Outputs BDC produces
- normalized packet
- validation report
- recommended architecture prior
- role count and role set
- redesign guidance
- confidence split:
  - prior confidence
  - deployability confidence
- measurement gap list
- client-ready memo

### System workflow
Use a simple visual sequence:

`Client evidence packet -> BDC intake -> normalization -> evidence-aware reasoning -> recommendation -> redesign guidance -> next measurement request`

---

## 7. Proof Model

The deck must use proof in three layers.

### Layer A — Scientific discipline
Show that BDC is disciplined about:
- evidence labels
- non-claims
- reproducibility
- explicit uncertainty

### Layer B — Product workflow proof
Show that BDC can actually process client packets end-to-end.

### Layer C — Case proof
Use `TextAI_Auto` as the first concrete case.

Claim-safe framing for TextAI_Auto:
- BDC kept the 4-role frame fixed
- BDC correctly excluded harmonizer expansion
- BDC identified editor/prompt behavior as the active bottleneck
- BDC deprioritized mid-AI after measured failure
- BDC kept guidance narrow and evidence-safe

Do not claim TextAI_Auto as final commercial success if the measured outcome does not support that.

---

## 8. Recommended Deck Structure

Recommended size:
- 10 to 14 slides

### Slide 1 — Title
Message:
- Architecture for cooperative AI systems should come from task structure and measured evidence, not trial-and-error layering.

### Slide 2 — Problem
Message:
- Most multi-stage AI systems are built by accumulation, not by architecture logic.

### Slide 3 — What BDC Does
Message:
- BDC Designer takes a workflow packet and returns architecture guidance, redesign guidance, and missing measurements.

### Slide 4 — What BDC Does Not Do
Message:
- It does not replace LLMs, invent certainty, or claim universal optimality.

### Slide 5 — How the System Works
Message:
- Folder intake, validation, evidence-aware recommendation, redesign output, measurement gap request.

### Slide 6 — Output Surfaces
Message:
- Show normalized packet, recommendation, redesign memo, measurement gaps.

### Slide 7 — Why This Is Different
Message:
- BDC distinguishes prior confidence from deployability confidence.

### Slide 8 — TextAI_Auto Case
Message:
- The system helped keep the architecture frame stable and locate the true bottleneck in the editor layer.

### Slide 9 — What BDC Concluded in the Case
Message:
- keep 4-role frame
- do not add harmonizer
- deprioritize mid-AI
- focus next cycle on narrow prompt refinement

### Slide 10 — What a Client Engagement Looks Like
Message:
- packet intake -> architecture audit -> redesign guidance -> next-cycle measurement discipline

### Slide 11 — Who It Is For
Message:
- teams with expensive workflow design mistakes, not chatbot hobby use.

### Slide 12 — CTA
Message:
- request architecture audit
- submit workflow packet
- run a pilot inside measured constraints

Optional appendix slides:
- evidence labeling model
- confidence model
- measurement gap logic
- sample client packet structure

---

## 9. Visual Direction

Tone:
- deep-tech
- precise
- premium
- technical
- low-hype

Visual style:
- dark or neutral enterprise theme
- strong diagrams over stock photos
- architecture blocks, workflow graphs, confidence split visuals
- use 1-2 proof tables, not dense spreadsheets

Avoid:
- generic SaaS illustrations
- exaggerated AI imagery
- cartoon agents
- inflated futurist language
- feature walls without evidence structure

---

## 10. Presentation Rules

Every slide must answer one of three things:
- what problem exists,
- what BDC does about it,
- what evidence supports that statement.

For every proof slide:
- name whether the claim is measured, inferred, or constrained
- include at least one explicit limitation when relevant

For every case slide:
- separate architecture result from product result
- separate observability gain from rewrite-lift gain

---

## 11. Required Appendix Material

The presenter/designer should have access to:
- `docs/BDC_CLIENT_PACKET_WORKFLOW.md`
- `docs/BDC_PAID_PILOT_POLICY.md`
- `docs/BDC_PILOT_PROGRAM.md`
- `reports/public_release/TASK-7030-CASE-STUDY-REAL-DEPLOYMENT/FLAGSHIP_CASE_STUDY.md`
- `reports/public_release/TASK-7120-REAL-CASEBOOK-V1/BDC_REAL_CASEBOOK_V1.md`
- `reports/public_release/TASK-7050-BDC-SALES-OFFER-PACK/BDC_ONE_PAGE_OFFER.md`
- `reports/public_release/TASK-7060-BDC-LANDING-PAGE-COPY/BDC_LANDING_PAGE_COPY.md`

For TextAI-specific proof, use only currently measured BDC outputs and architect-approved packet materials.

---

## 12. Deliverable Requested From Designer Or Presentation Team

Preferred output package:
- master presentation deck
- short version (5-6 slides)
- appendix version
- speaker notes version

The deck must be usable by:
- BDC founder / lead architect
- technical sales lead
- pilot operator in a client meeting

---

## 13. Final Standard

A good client presentation for BDC should leave the audience with this exact understanding:

`BDC Designer is not a black-box AI product. It is a disciplined system for deciding how a cooperative AI workflow should be structured, what has actually been validated, and what still needs to be measured before stronger deployment claims are justified.`
