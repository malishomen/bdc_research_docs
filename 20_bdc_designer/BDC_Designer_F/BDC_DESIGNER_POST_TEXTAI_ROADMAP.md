# BDC Designer Post-TextAI Roadmap

**Version:** 1.0  
**Date:** 2026-03-16  
**Status:** COMPLETED  
**Branch:** test  
**Type:** Applied product hardening roadmap  
**Trigger Case:** `TextAI_Auto` first real client engagement  
**Companion Documents:** `docs/project/project_main_doc.md`, `docs/project/project_roadmap.md`

---

## 1. Purpose

This roadmap captures the nearest execution plan for tuning `BDC Designer` after the first real client case: `TextAI_Auto`.

The goal is not to redesign BDC theory. The goal is to harden the product shell around the validated BDC core so it can:
- ingest real client evidence packages,
- separate historical evidence from current runtime truth,
- produce architecture guidance for current-runtime redesign,
- request the minimum missing measurements needed to raise confidence,
- support paid client delivery without manual packet assembly each time.

---

## 2. What TextAI_Auto Taught Us (L0 Facts)

### Stable product facts

1. BDC core survived a real client case.
2. Raw client inputs arrive as a folder-based evidence packet, not as native `BDC_PACKET_V2`.
3. Real cases contain mixed evidence layers:
   - `measured`
   - `measured_from_historical_report`
   - `inferred`
   - `missing`
4. Historical prior and current runtime truth can diverge sharply.
5. Live LLM interpretation materially improves intake quality versus heuristic parsing.
6. Clients need redesign guidance, not only winner selection.

### TextAI_Auto result anchors

Relevant artifacts:
- `D:\projects\Text_AI_auto_check\BDC_TESTS\TEXTAI_AUTO_BDC_PACKET_V2_1\TEXTAI_AUTO_BDC_V2_1_RECOMMENDATION.json`
- `D:\projects\Text_AI_auto_check\BDC_TESTS\TEXTAI_AUTO_BDC_PACKET_V2_1\TEXTAI_AUTO_BDC_V2_1_EXPLANATION.json`
- `D:\projects\Text_AI_auto_check\BDC_TESTS\TEXTAI_AUTO_BDC_PACKET_V2_1\TEXTAI_AUTO_BDC_V2_1_ANALYSIS_REPORT.md`
- `D:\projects\Text_AI_auto_check\BDC_TESTS\TEXTAI_AUTO_BDC_PACKET_V2_1\TEXTAI_AUTO_BDC_PACKET_V2_1_ROLEMAPPED.json`

Observed BDC outcome on role-mapped target-project packet:
- winner: `D`
- role set: `orchestrator + planner + editor + guardian`
- role count: `4`
- strategy: `full_hybrid_search`
- confidence: `high`

---

## 3. Non-Negotiables

1. BDC decision core remains deterministic and primary.
2. LLM adapter remains interpreter-only, never final decision-maker.
3. No hiding evidence status. Historical vs current truth must remain explicit.
4. No client recommendation without machine-readable diagnostics.
5. No release of stronger claims than artifacts support.
6. No harmonizer-like role expansion without positive evidence.

---

## 4. Nearest Roadmap

Execution order is strict.

### Phase A — Folder Intake Mode

**Goal:** Let BDC ingest a real client folder directly instead of requiring manual packet assembly.

**Scope:**
- Input path: folder containing `README`, packet json, csv tables, role mapping, failure registry, design priorities.
- Automatic file discovery.
- Intake manifest.
- Evidence coverage report.
- Draft normalized packet generation.

**Deliverables:**
- `src/bdc_designer_v2/intake/folder_loader.py`
- `src/bdc_designer_v2/intake/file_registry.py`
- `src/bdc_designer_v2/intake/normalization_profile.py`
- `docs/BDC_FOLDER_INTAKE_MODE.md`
- regression fixtures for `TextAI_Auto`

**Definition of Done:**
- Folder-based packet loads with one command.
- Required files are detected or reported missing cleanly.
- A normalized packet can be emitted without manual editing for `TextAI_Auto`-style intake.
- All outputs contain explicit evidence-status fields.

**Acceptance Standard:**
- `TextAI_Auto` V2.1 folder can be ingested into a valid normalized packet in one run.
- Missing-file behavior is deterministic and human-readable.
- No silent file assumptions.

---

### Phase B — Evidence-Status-Aware Weighting

**Goal:** Make scoring, confidence, and strategy explicitly sensitive to `measured` vs `historical` vs `inferred` evidence.

**Scope:**
- Introduce evidence-status weighting.
- Penalize winner certainty when dominant evidence is historical and active runtime support is sparse.
- Preserve strong winner selection when current runtime evidence aligns.

**Deliverables:**
- `src/bdc_designer_v2/evidence_status.py`
- updates to scoring / confidence / strategy layers
- `docs/BDC_EVIDENCE_STATUS_WEIGHTING.md`
- calibration tests on `TextAI_Auto`

**Definition of Done:**
- Scoring pipeline consumes evidence status explicitly.
- Confidence responds to mixed-truth cases in a predictable way.
- Historical prior strength and current-runtime deployability are separated in output.

**Acceptance Standard:**
- Same case can distinguish between:
  - best prior winner
  - deployability confidence
- Output must not collapse those two into one number.

---

### Phase C — Logical Redesign Mode

**Goal:** Add a first-class mode that recommends how to redesign a current runtime logically, not only which historical architecture won.

**Scope:**
- Input: current runtime role mapping + current measured slices + historical prior evidence.
- Output:
  - recommended logical role split,
  - current component mapping,
  - recommended first architecture test,
  - planner/editor/guardian/orchestrator guidance.

**Deliverables:**
- `src/bdc_designer_v2/redesign_mode.py`
- `src/bdc_designer_v2/redesign_contract.py`
- `docs/BDC_LOGICAL_REDESIGN_MODE.md`
- `TEXTAI_AUTO` redesign-mode snapshot

**Definition of Done:**
- BDC can output redesign guidance for current-runtime systems.
- Output includes component-to-role mapping.
- Output includes next test recommendation.

**Acceptance Standard:**
- `TextAI_Auto` can be answered directly in system output with:
  - what to formalize first,
  - which role split to test first,
  - where guardian should sit,
  - what not to introduce yet.

---

### Phase D — Measurement Gap Detector

**Goal:** Let BDC say exactly which missing measurements are blocking stronger guidance.

**Scope:**
- Detect metric insufficiency by decision type.
- Emit smallest next measurement set.
- Tie measurement gaps to architecture questions.

**Deliverables:**
- `src/bdc_designer_v2/measurement_gaps.py`
- `docs/BDC_MEASUREMENT_GAP_DETECTOR.md`
- output schema updates

**Definition of Done:**
- Every low-confidence or mixed-confidence recommendation includes explicit missing measurements.
- Measurement requests are ranked by expected decision value.

**Acceptance Standard:**
- For `TextAI_Auto`, BDC must name the minimum additional set needed to move beyond current redesign guidance.

---

### Phase E — Sparse Runtime Metrics Support

**Goal:** Support real packages where current-runtime evidence is partially numeric and partially verdict-like.

**Scope:**
- Accept sparse metrics cleanly.
- Accept verdict-level evidence without schema breakage.
- Preserve uncertainty instead of failing closed.

**Deliverables:**
- schema updates
- sparse-metric normalization rules
- `docs/BDC_SPARSE_RUNTIME_EVIDENCE.md`
- regression fixtures from H5.x style packets

**Definition of Done:**
- Sparse runtime tables are accepted without manual repair.
- Unknown metrics remain explicit.
- Decision outputs degrade gracefully.

**Acceptance Standard:**
- `TextAI_Auto` H5.x-style data can be consumed without contradiction inflation caused by representational mismatch.

---

### Phase F — Operator and Client Delivery Hardening

**Goal:** Turn the above into a repeatable client-delivery path.

**Scope:**
- one-command client packet run,
- opinionated output bundle,
- lead-architect request template,
- intake checklist,
- redesign memo template.

**Deliverables:**
- `docs/BDC_CLIENT_PACKET_WORKFLOW.md`
- `templates/BDC_CLIENT_REQUEST_TEMPLATE.md`
- `templates/BDC_REDESIGN_MEMO_TEMPLATE.md`
- CLI command docs for folder intake and redesign mode

**Definition of Done:**
- New client packet can be processed end-to-end without bespoke analyst assembly.
- Output bundle is suitable for direct delivery to technical client stakeholders.

**Acceptance Standard:**
- `TextAI_Auto` full flow can be reproduced from raw folder -> normalized packet -> recommendation -> redesign memo.

---

## 5. Project-Level Definition of Done

This post-TextAI roadmap is complete only if all of the following are true:

1. `BDC Designer` ingests folder-based client evidence directly.
2. Mixed historical/current truth is handled explicitly in scoring and confidence.
3. `BDC Designer` can output logical redesign guidance, not only winner ranking.
4. Measurement gaps are emitted automatically.
5. Sparse runtime evidence is accepted without manual analyst repair.
6. Client-facing delivery flow is reproducible on the first case (`TextAI_Auto`).

---

## 6. Acceptance Standards

A phase is accepted only if:
- implementation artifacts exist,
- tests exist,
- `TextAI_Auto` regression passes,
- no existing validated BDC v2 behavior is regressed,
- output remains evidence-disciplined.

### Minimum L0 verification per phase
- py_compile or equivalent import check passes
- phase-specific pytest suite passes
- `TextAI_Auto` regression packet run passes
- brief report produced
- append-only logs updated

### Failure conditions
A phase fails if:
- it requires manual packet surgery for `TextAI_Auto` after declared completion,
- it hides evidence status,
- it allows LLM output to override deterministic BDC decisions,
- it claims stronger certainty than artifacts support.

---

## 7. Out of Scope

This roadmap does not include:
- new scientific theory claims,
- harmonizer-first architecture lines,
- replacing the BDC core with an LLM agent,
- a generic consumer UX for arbitrary non-technical users.

---

## 8. Immediate Execution Trigger

The roadmap should start from the first product-hardening task after `TextAI_Auto`.

First mandatory implementation target:
- **Folder Intake Mode**

Reason:
`TextAI_Auto` already proved that real clients deliver evidence as folder packages, not native BDC packets.

---

## 9. Append-Only Change Log

| Date | Change |
|------|--------|
| 2026-03-16 | v1.0 — Initial creation. Roadmap created from first real client case `TextAI_Auto` with explicit phases, DoD, and acceptance standards for BDC Designer hardening. |
| 2026-03-16 | v1.1 — Roadmap completed. Phases A-F implemented and `BDC Designer` prepared for next `TextAI_Auto` folder intake. |

---

## 10. Completion Status (2026-03-16)

The roadmap is implemented in full on branch `test`.

### Completed phases

- **Phase A — Folder Intake Mode**
  - `src/bdc_designer_v2/intake/folder_loader.py`
  - `src/bdc_designer_v2/intake/file_registry.py`
  - `src/bdc_designer_v2/intake/normalization_profile.py`
  - `docs/BDC_FOLDER_INTAKE_MODE.md`

- **Phase B — Evidence-Status-Aware Weighting**
  - `src/bdc_designer_v2/evidence_status.py`
  - scoring, confidence, strategy, explanation updates
  - `docs/BDC_EVIDENCE_STATUS_WEIGHTING.md`

- **Phase C — Logical Redesign Mode**
  - `src/bdc_designer_v2/redesign_mode.py`
  - `src/bdc_designer_v2/redesign_contract.py`
  - `docs/BDC_LOGICAL_REDESIGN_MODE.md`

- **Phase D — Measurement Gap Detector**
  - `src/bdc_designer_v2/measurement_gaps.py`
  - `docs/BDC_MEASUREMENT_GAP_DETECTOR.md`

- **Phase E — Sparse Runtime Metrics Support**
  - `src/bdc_designer_v2/sparse_runtime.py`
  - intake and validator updates
  - `docs/BDC_SPARSE_RUNTIME_EVIDENCE.md`

- **Phase F — Operator and Client Delivery Hardening**
  - `src/bdc_designer_v2/client_delivery.py`
  - `docs/BDC_CLIENT_PACKET_WORKFLOW.md`
  - `templates/BDC_CLIENT_REQUEST_TEMPLATE.md`
  - `templates/BDC_REDESIGN_MEMO_TEMPLATE.md`
  - CLI command: `client-bundle`

### Final readiness statement

`BDC Designer` is now prepared to accept the next `TextAI_Auto` evidence packet through a folder-based client workflow and produce:
- normalized packet output,
- evidence-aware recommendation,
- logical redesign guidance,
- measurement-gap request,
- sparse-runtime support summary,
- client-ready redesign memo.
