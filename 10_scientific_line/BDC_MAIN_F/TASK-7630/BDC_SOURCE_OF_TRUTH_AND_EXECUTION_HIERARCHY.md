# BDC Source Of Truth And Execution Hierarchy

**Date:** 2026-03-19  
**Status:** CANONICAL GOVERNANCE NOTE

## Purpose

This document defines how BDC prevents hierarchy drift, scope drift, and execution amnesia across sessions.

The goal is simple:

**The project must always know which documents define validity, which document defines the real current state, and which exact next action is actually authorized.**

## Source-Of-Truth Hierarchy

### Level 1 — Validity Law
- `CANON.md`

This level decides:
- what counts as a valid claim,
- what counts as a valid artifact,
- what kind of evidence is required,
- what is forbidden regardless of enthusiasm or convenience.

Nothing below this level may override it.

### Level 2 — Actual Current State
- `bdc_real_statemant.md`

This file decides:
- what the real current active line is,
- what has already been closed,
- what the current authorized next executable action is,
- what current scope limits are in force.

This is the primary operational source for the actual project state.

### Level 3 — Canonical Strategic Frame
- `docs/project/project_main_doc.md`
- `docs/project/project_roadmap.md`

These documents define:
- the strategic shape of the project,
- the active bounded roadmap,
- the relation between the scientific reboot line and `BDC Designer`.

They must remain consistent with the current live state.

### Level 4 — Operational Continuity
- `memory.md`

This file is the continuity and session handoff layer.

It does not replace the live-state file.
It operationalizes it.

### Level 5 — Historical / Architectural Context
- continuity memos
- architecture maps
- historical reboot notes
- document maps

These documents are valid context but not live operational priority when they conflict with fresher higher-priority state documents.

## Conflict Resolution Rule

If two documents appear to disagree:

1. `CANON.md` wins on validity.
2. `bdc_real_statemant.md` wins on actual current state.
3. `project_main_doc.md` and `project_roadmap.md` win on strategic framing over historical context docs.
4. `memory.md` must be corrected if it drifts from the live-state file.
5. Historical/continuity docs must be interpreted as context, not live priority, when they conflict with fresher higher-priority documents.

## Execution Discipline Rule

At any moment the project may do only one of the following:

1. execute the currently authorized next action,
2. close the currently authorized action with measured results,
3. open the next bounded gate only after the current action is closed.

The project may not:
- reopen broad strategy while a narrower authorized action is pending,
- widen scope ahead of the current bounded gate,
- treat readiness as success,
- treat product-layer guidance as scientific truth,
- or skip from strategic discussion directly to a broader execution layer.

## `BDC Designer` Rule

`BDC Designer` is mandatory for:
- narrowing,
- evidence discipline,
- packet completeness,
- secondary confirmation.

`BDC Designer` is not allowed to:
- replace measured scientific gate truth,
- reopen a closed scope by recommendation surface alone,
- overrule a canonical measured gate.

## Forgetting Prevention Rule

To prevent forgetting or drift:

1. update `bdc_real_statemant.md` after every state-changing task,
2. update `memory.md` after every state-changing task,
3. keep the current next executable action explicit,
4. run the hierarchy verifier before major executions and phase transitions,
5. refuse any broader action not explicitly authorized by the current live state.

## Current Applied Interpretation

As of `2026-03-19`:
- the live scientific line is `R5 - single-mechanism transfer long-run`,
- the next authorized executable action is the canonical `R5` long-run,
- no post-`R5` widening is authorized before measured `R5` evidence exists.

That means:
- no new strategic redirection,
- no multi-mechanism opening,
- no organism/cell/SuperCell claims,
- no broader reboot reinterpretation,
- until the `R5` long-run is executed and measured.
