# Release Notes — Main Merge 2026-03-17 — BDC Designer Freeze

**Date:** 2026-03-17  
**Merge Commit:** `3159a5b`  
**Branch Flow:** `test -> main`  
**Status:** COMPLETED

---

## Summary

`BDC Designer` has been frozen as the current mainline-ready productized subsystem and merged to `main`.

This merge promotes the validated `BDC Designer` line from `test` into the repository's protected branch after:
- CLI v2 productization,
- benchmark validation,
- post-TextAI product hardening,
- client packet workflow integration,
- freeze-state documentation,
- and corrective normalization of the repository instruction filename on Windows.

---

## What Is Now In Main

### Core `BDC Designer` line
- `src/bdc_designer_v2/`
- `tools/bdc_designer_v2.py`
- `schemas/BDC_CLI_SCHEMA_V2.json`
- packet validation, recommendation, explanation, redesign, and client-bundle workflows

### Product/operator documentation
- `docs/BDC_CLI_V2_USER_GUIDE.md`
- `docs/BDC_CLIENT_PACKET_WORKFLOW.md`
- `docs/BDC_CLIENT_PRESENTATION_BRIEF.md`
- `docs/project/BDC_DESIGNER_FREEZE_STATE.md`
- `docs/project/BDC_DESIGNER_POST_TEXTAI_ROADMAP.md`

### TextAI-driven hardening line
- folder-intake mode
- evidence-status-aware weighting
- logical redesign mode
- measurement gap detector
- sparse runtime evidence support
- client bundle workflow
- 4-role redesign consistency fix

---

## Merge Basis

Primary freeze documentation:
- `docs/project/BDC_DESIGNER_FREEZE_STATE.md`

Main preparation task:
- `reports/analysis/TASK-7571-BDC-DESIGNER-FREEZE-AND-MAIN-MERGE/TASK-7571_BRIEF_REPORT.md`

Corrective filename normalization task:
- `reports/analysis/TASK-7572-AGENTS-FILENAME-NORMALIZATION/TASK-7572_BRIEF_REPORT.md`

---

## Important Operational Notes

1. `BDC Designer` is frozen as a claim-safe architecture-design and redesign-guidance system.
2. The deterministic decision core remains primary.
3. LLM integration remains interpreter-only, not final decision-maker.
4. Client delivery now supports folder-based intake and one-command bundle generation.
5. The repository instruction file is now normalized to:
   - `AGENTS.md`

---

## Non-Claims

This merge does **not** claim:
- universal architecture optimization,
- guaranteed client performance lift,
- autonomous replacement of experimentation,
- closure of future `BDC Designer` evolution.

It establishes a stable mainline base for the current validated system.

---

## Post-Merge State

- `main` and `test` were synchronized to the same head after merge.
- Active working branch returned to:
  - `test`

