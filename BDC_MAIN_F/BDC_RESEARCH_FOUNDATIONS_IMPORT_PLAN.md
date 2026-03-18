# BDC Research Foundations Import Plan

**Version:** 1.0  
**Date:** 2026-03-18  
**Status:** PLANNED  
**Branch:** test  
**Depends On:** `docs/project/BDC_RESEARCH_REBOOT_PLAN.md`, `docs/project/BDC_RESEARCH_REBOOT_CHARTER.md`, `D:\projects\Bio_Digital_Core\Temp\research\BDC_EXTERNAL_RESEARCH_APPLICABILITY_REPORT.md`

---

## 1. Purpose

This document defines the next documentation-first import package for the scientific BDC line.

Bounded import targets:

1. Belnap-alignment
2. diversity taxonomy
3. error/erasure model
4. channel-aware memory

The package exists to turn the strongest external research findings into an ordered internal work program for the rebooted BDC research line.

This is not implementation yet.
This is the contract that implementation must obey.

---

## 2. Why This Package Exists

The reboot line now has:

- a historical map,
- a reboot plan,
- a reboot charter,
- a first `Selection Physics Rebuild` package.

What it still lacks is a disciplined import of the strongest scientific foundations we just extracted from the external research packet.

The four most valuable imports are:

1. a formal four-valued semantics layer instead of informal quaternary intuition;
2. a diversity policy grounded in evolutionary-optimization literature instead of hand-waving around mutation and speciation;
3. a memory error model that distinguishes corruption from loss;
4. a channel-aware memory architecture rather than a DNA metaphor without physical constraints.

---

## 3. Strategic Boundaries

This package is allowed to define:

- foundational notes,
- reboot-facing task packets,
- phase ordering,
- definitions of done,
- acceptance standards,
- explicit constraints for later implementation.

This package is not allowed to:

- reopen the old `hidden_rule` product path,
- claim that any of the imported theories are already implemented,
- rewrite protected canon documents,
- conflate `BDC Designer` product work with reboot-line scientific work.

---

## 4. Execution Rule

Execution order is strict:

`TASK-7584 -> TASK-7585 -> TASK-7586 -> TASK-7587`

Reason for order:

1. `Belnap-alignment` comes first because evidence, uncertainty, contradiction, and designated action states need formal semantics before downstream mechanism notes are written.
2. `Diversity taxonomy` comes second because selection physics and speciation policy need to be rebuilt before memory architecture is overinterpreted.
3. `Error/erasure model` comes third because memory cannot be specified honestly without a noise and loss model.
4. `Channel-aware memory` comes last because it should consume the semantics and error model instead of inventing them ad hoc.

No parallel implementation is allowed between these four tasks.

---

## 5. Package Goals

At completion, the BDC research line must have:

1. a formal semantic alignment note between BDC quaternary states and a Belnap-style frame;
2. a diversity-policy note for rebooted selection physics;
3. a bounded memory error model note;
4. a channel-aware memory note that turns DNA inspiration into explicit architectural constraints.

---

## 6. Phase Breakdown

## Phase A — Belnap Alignment

### Objective

Define a formal semantics note that aligns BDC quaternary logic with a Belnap-style four-valued frame.

### Required outputs

- canonical mapping note
- action-state interpretation
- contradiction vs gap distinction
- explicit limits of the mapping

### Definition of Done

- note written
- evidence-state consequences stated
- designated states for action/reasoning defined
- relationship to current BDC terms documented

---

## Phase B — Diversity Taxonomy

### Objective

Replace vague diversity intuition with an explicit taxonomy for reboot-line evolutionary design.

### Required outputs

- lineage / genotype / phenotype distinction
- relation to speciation and premature convergence
- practical policy implications for `Selection Physics Rebuild`
- what not to import blindly

### Definition of Done

- note written
- taxonomy stated clearly
- direct reboot implications listed
- future experiment hooks identified

---

## Phase C — Error/Erasure Model

### Objective

Define a memory and transmission defect model for the scientific BDC line.

### Required outputs

- corruption vs erasure distinction
- burst defect concept
- address corruption concept
- state bundle and genome implications

### Definition of Done

- note written
- error classes defined
- implications for serialization and recovery listed
- explicit anti-metaphor constraints written

---

## Phase D — Channel-Aware Memory

### Objective

Define a memory-architecture note that treats BDC memory as an addressable noisy channel rather than an ideal storage metaphor.

### Required outputs

- address/header/payload/control model
- selective retrieval concept
- active/locked/retired states
- channel-aware retrieval and replication assumptions

### Definition of Done

- note written
- addressable memory unit defined
- relation to DNA-inspired line stated honestly
- dependency on error/erasure model made explicit

---

## 7. Package-Level Tests

Minimum package verification:

1. all plan and task docs exist;
2. all task JSON files parse;
3. project docs reference the new package;
4. phase ordering is explicit in the master plan;
5. every task packet has DoD, tests, evaluation criteria, and out-of-scope boundaries.

---

## 8. Package-Level Definition of Done

The package is complete only if:

1. the master import plan exists;
2. the strict scientific task chain exists;
3. project docs reference the new package;
4. a brief report exists;
5. append-only logs are updated.

---

## 9. Failure Conditions

Stop and escalate if any of the following happens:

1. Belnap-alignment is written as marketing metaphor instead of formal semantics;
2. diversity taxonomy is collapsed into “more mutation” or “more randomness”;
3. error/erasure model does not distinguish loss from corruption;
4. channel-aware memory is specified without dependency on the error model;
5. product-line `BDC Designer` concerns bleed into the reboot-line package without explicit reason.

---

## 10. Immediate Task Chain

- `tasks/TASK-7583-BDC-RESEARCH-FOUNDATIONS-IMPORT-PLAN.json`
- `tasks/TASK-7584-BDC-BELNAP-ALIGNMENT-NOTE.json`
- `tasks/TASK-7585-BDC-DIVERSITY-TAXONOMY-NOTE.json`
- `tasks/TASK-7586-BDC-ERROR-ERASURE-MODEL-NOTE.json`
- `tasks/TASK-7587-BDC-CHANNEL-AWARE-MEMORY-NOTE.json`

---

## 11. Practical Meaning

This package does not yet build the new scientific BDC.

It prepares the four foundation notes that the new scientific BDC should stand on, so that later implementation work does not repeat:

- informal quaternary semantics,
- weak diversity reasoning,
- idealized memory assumptions,
- and DNA language without channel discipline.
