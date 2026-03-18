# BDC Designer Confidence And Evidence Import Plan

**Version:** 1.0  
**Date:** 2026-03-18  
**Status:** PLANNED  
**Branch:** test  
**Depends On:** `docs/project/BDC_DESIGNER_FREEZE_STATE.md`, `D:\projects\Bio_Digital_Core\Temp\research\BDC_EXTERNAL_RESEARCH_APPLICABILITY_REPORT.md`

---

## 1. Purpose

This document defines the next strict execution block for `BDC Designer` after freeze:

1. calibration
2. selective prediction
3. generalized risk
4. evidence-state semantics

The goal is to import the strongest validated ideas from the external research packet into the existing `BDC Designer` core without reopening unrelated product scope.

This is a bounded product-hardening and theory-alignment package, not a new product line.

---

## 2. Why This Package Exists

`BDC Designer` is operational, but four deficits remain visible:

1. confidence is heuristic and not calibration-audited;
2. abstention exists in practice but is not a formal selective-prediction contract;
3. multi-threshold risk evaluation is underdeveloped;
4. packet evidence states are informative but not yet formalized as a compact semantics layer.

External sources now provide enough support to address these deficits honestly:

- Guo et al. -> calibration discipline
- Brier -> proper scoring baseline
- Geifman & El-Yaniv -> reject option / risk-coverage framing
- Traub et al. -> generalized risk and multi-threshold evaluation
- Belnap + many-valued logic references -> evidence-state semantics

---

## 3. Strategic Boundaries

This package is allowed to change:

- confidence metrics and outputs
- diagnostics and abstention contract
- benchmark and evaluation reporting
- evidence-state representation and inference support
- CLI and client-bundle output surface as needed to expose the new fields

This package is not allowed to change:

- role ontology content
- variant scoring logic for architecture search, except where new evidence semantics are explicitly required
- TextAI customer verdicts retroactively
- reboot-line research code
- any protected canon document except `project_main_doc.md` and `project_roadmap.md` references for planning continuity

---

## 4. Execution Rule

Execution order is strict:

`TASK-7579 -> TASK-7580 -> TASK-7581 -> TASK-7582`

No parallel delivery is allowed between these four tasks.

Reason:

- calibration provides the confidence discipline baseline;
- selective prediction must consume calibrated confidence;
- generalized risk evaluation must consume the selective contract;
- evidence-state semantics should align to the final confidence and abstention contract, not precede it blindly.

---

## 5. Package Goals

At package completion, `BDC Designer` must be able to:

1. report calibrated confidence quality on benchmarked cases;
2. produce explicit selective-decision outcomes, including abstention;
3. evaluate recommendation quality beyond fixed working points;
4. reason over evidence states using a formal compact semantics layer rather than ad hoc labels alone.

---

## 6. Phase Breakdown

## Phase A — Calibration Layer

### Objective

Upgrade confidence from a heuristic banding layer into a calibration-aware operator surface.

### Required additions

- Brier score support
- Expected Calibration Error (ECE)
- reliability-table output suitable for reports and client bundles
- calibration summary in benchmark and/or audit outputs
- explicit distinction between raw confidence and calibrated confidence where needed

### Required deliverables

- calibration module or extension
- benchmark-facing calibration outputs
- operator documentation for interpretation
- regression tests on benchmark fixtures

### Definition of Done

- calibration metrics computed reproducibly on canonical fixtures
- outputs are written to JSON artifacts, not only console text
- tests prove metric presence and expected field stability
- brief report written

---

## Phase B — Selective Prediction Contract

### Objective

Convert current caution/warm-start behavior into an explicit selective-decision contract.

### Required additions

Canonical recommendation outcome classes:

- `recommend`
- `recommend_with_caution`
- `warm_start_only`
- `abstain_need_more_evidence`

### Required behavior

- diagnostics and explanation layers must agree on the outcome class
- client bundle must expose the outcome class
- abstention must be triggered by explicit criteria, not vague text only

### Definition of Done

- outcome class emitted in machine-readable outputs
- abstention path tested on low-evidence fixture(s)
- explanation layer reflects the same decision class
- brief report written

---

## Phase C — Generalized Risk Evaluation

### Objective

Add multi-threshold evaluation so that confidence systems are not judged only at fixed working points.

### Required additions

- generalized-risk metric support
- coverage-risk summary
- benchmark output that can compare confidence systems across thresholds
- explicit note of why this is different from single-threshold pass/fail

### Minimum expectation

The implementation does not need a publication-grade visualization layer in the first pass, but it must provide stable numeric outputs that can be consumed by reports and later plots.

### Definition of Done

- generalized-risk output exists for benchmark fixtures
- threshold-scan or equivalent aggregation is reproducible
- tests verify output presence and monotonic sanity where applicable
- brief report written

---

## Phase D — Evidence-State Semantics

### Objective

Formalize packet evidence states as a compact semantics layer aligned with many-valued reasoning.

### Required additions

- canonical evidence-state vocabulary
- formal mapping between packet evidence labels and action semantics
- machine-readable evidence-state summary
- explicit handling of contradiction vs absence vs inferred support

### Expected scope

This phase is not a full `qcore` rewrite.

It is a bounded semantics layer for `BDC Designer` packet reasoning that should later align with a broader Belnap-style note.

### Definition of Done

- evidence-state semantics documented
- validator/evidence pipeline expose the new state summary cleanly
- diagnostics and explanation consume the new summary
- tests prove contradiction and missingness are not conflated
- brief report written

---

## 7. Package-Level Tests

Minimum package verification before declaring completion:

1. unit tests for each phase
2. regression tests on at least one existing TextAI fixture
3. CLI-level smoke test for exposed outputs
4. client-bundle regression ensuring no breakage of existing bundle generation
5. benchmark-oriented test proving the new confidence outputs exist and remain parseable

---

## 8. Package-Level Definition of Done

The package is complete only if all of the following are true:

1. calibrated confidence outputs exist
2. selective-decision outcome class exists
3. generalized-risk outputs exist
4. evidence-state semantics summary exists
5. CLI and client-bundle surfaces expose the new fields
6. canonical fixtures still pass
7. docs, brief reports, append-only logs are updated

---

## 9. Failure Conditions

The package must stop and escalate if any of the following occurs:

1. confidence changes break existing recommendation identity on canonical fixtures without explicit evidence-based reason;
2. selective prediction becomes a text-only layer without machine-readable contract;
3. generalized-risk implementation cannot be made reproducible on current fixtures;
4. evidence-state semantics collapses contradiction and missingness into one state;
5. client-bundle compatibility with current TextAI fixtures is broken.

---

## 10. Immediate Task Chain

- `tasks/TASK-7579-BDC-DESIGNER-CALIBRATION-LAYER.json`
- `tasks/TASK-7580-BDC-DESIGNER-SELECTIVE-PREDICTION-CONTRACT.json`
- `tasks/TASK-7581-BDC-DESIGNER-GENERALIZED-RISK-EVALUATION.json`
- `tasks/TASK-7582-BDC-DESIGNER-EVIDENCE-STATE-SEMANTICS.json`

---

## 11. Practical Meaning

This package is the shortest honest bridge between:

- the external research packet we have now studied,
- the current frozen `BDC Designer`,
- and the next round of implementation work.

It does not reopen strategy.
It sharpens the current product line.
