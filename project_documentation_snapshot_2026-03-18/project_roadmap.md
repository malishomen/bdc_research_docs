# BDC MASTER ROADMAP 2026-02-27

**Branch:** `test`
**Date:** 2026-02-27
**Status:** Critical Phase — Physics-of-Selection must be fixed before complexity can evolve.

This document is the single source of truth for the project's continuation, consolidating all recent findings and strategic realignments. Each phase is gated with explicit goals, deliverables, and kill criteria.

---

## 0. Non-Negotiables (Canon Alignment)

*   **No claims without artifacts.** All metrics must be backed by reproducible run artifacts.
*   **Reproducibility anchor.** Canonical PASS/FAIL is determined by `runtime_summary.json.kill_status`.
*   **Append-only logs.** `AGENTS_LOG.md` and `WEEKLY_STATUS.md` are append-only.
*   **`main` is protected.** All work occurs in the `test` branch.
*   **No scope creep.** New ideas must become new, separate experiments.
*   **FAIL is valuable.** A met kill criterion stops the current direction and is recorded as a key finding.

---

## 1. Executive Summary: Where We Are (L0 Facts)

1.  **Two Working Systems:** The **Evolution Engine (EDP1)** and the **Wiki Pipeline** are both functional and deterministic but have not yet been connected.
2.  **Physics Failure (TASK-1400B):** It is mathematically proven that under the current complexity penalty (`fitness = accuracy − λ * Σ|w|`), more complex architectures like `v2` can **never** outperform simpler ones like `v1`.
3.  **Conclusion:** The project's "world physics" structurally forbid evolutionary growth. This must be fixed before any other progress can be made. The `hidden_rule` task is exhausted and will be used only as a controlled lab environment.

---

## 2. Strategic North Star: Digital Biology

BDC is a digital-biology research program. The goal is to create a "seed organism" (SuperCell) that can be placed in a new environment ("broth"), adapt, and be extracted back stronger ("digital panspermia"), demonstrating real-world utility.

---

## 3. Gated Roadmap

### Phase 0 — Closure & Freeze of Exhausted Line (1–2 days)

*   **Goal:** Formally close the `hidden_rule` line of inquiry and preserve it as a benchmark.
*   **Tasks:**
    *   **TASK-1500:** Create `ADR-0004` to document that the `hidden_rule` direction is exhausted due to the complexity barrier. Update `KILL_CRITERIA.yaml` to mark this line as closed.
*   **DoD:** `ADR-0004` is merged; `KILL_CRITERIA.yaml` is updated.

### Phase 1 — R2 Physics Fix as a Controlled Sweep (3–5 days)

*   **Goal:** Replace the non-biological "linear size tax" with a complexity regime that allows for architectural growth.
*   **Tasks:**
    *   **TASK-1501 (exp_0300):** Run a controlled sweep of new complexity penalty formulas (e.g., `mean(|w|)`, `Σ|w| / sqrt(K)`) using the `hidden_rule` environment and `v1, v1.5, v2` genomes.
*   **Success Criteria:** At least one new formula makes `v2` mathematically feasible (`required_accuracy <= 1.0`) and empirically competitive.
*   **Kill Criteria:** If no formula enables `v2` to become competitive, the problem is not just the physics but a deeper architectural mismatch.
*   **Deliverables:** `exp_0300` artifacts, `ADR-0005` selecting the new canonical complexity formula.

### Phase 2 — New Task: Wiki-Derived Evolution (5–7 days)

*   **Goal:** Bridge the Evolution Engine and the Wiki Pipeline. Stop optimizing a toy task.
*   **Tasks:**
    *   **TASK-1600 (exp_0400):** Create a "Cloze Evolution Task". The evolving genome will define a strategy for predicting masked tokens in text from `simplified_wiki_v0`. Fitness will be `cloze accuracy`.
*   **Success Criteria:** Evolved strategies significantly outperform random and frequency-based baselines.
*   **Kill Criteria:** If evolved strategies do not beat baselines, the current genome representation is unsuitable for language tasks. Stop and redesign the genome.
*   **Deliverables:** `exp_0400` results, `genome_v3` (cloze-adapted).

### Phase 3 — Energy / Resource-Bounded Evolution (5–7 days)

*   **Prerequisite:** Phase 1 and 2 PASS.
*   **Goal:** Make complexity tradeoffs biological: complexity consumes a finite "energy" resource rather than directly penalizing fitness.
*   **Tasks:**
    *   **TASK-1700 (exp_0500):** Implement a minimal energy model where each agent has an energy budget, and architectural complexity consumes energy. Individuals exceeding their budget fail to reproduce.
*   **Success Criteria:** A stable, non-trivial distribution of complexity levels emerges in the population.
*   **Kill Criteria:** If the system collapses to either trivial strategies or unbounded complexity, the energy model is invalid.
*   **Deliverables:** `exp_0500` results.

### Phase 4 — Specialization & Cooperation (7–10 days)

*   **Prerequisite:** Phase 3 PASS.
*   **Goal:** Demonstrate the emergence of a division of labor and collective advantage.
*   **Tasks:**
    *   **TASK-1800 (exp_0600):** Evolve multiple roles/genome types simultaneously. Fitness will depend on the **collective performance** on a suite of wiki-derived micro-tasks.
*   **Success Criteria:** Collective performance is measurably greater than the performance of the best single-role individual.
*   **Kill Criteria:** If cooperation does not emerge (collective <= individual), this direction is stopped.
*   **Deliverables:** `exp_0600` results, role diversity metrics.

### Phase 5 — Evaluation Gate / Roadmap Revision

*   **Prerequisite:** All previous phases PASS.
*   **Goal:** Make a go/no-go decision on more advanced concepts like "SuperCell v0".
*   **Tasks:**
    *   Operationally define "functional competence" based on metrics from Phases 2-4.
    *   Propose the next set of ADRs based on the accumulated evidence.

---

## 4. Immediate Next Actions (Strict Order)

1.  **Phase 0 / TASK-1500:** Formal closure of the `hidden_rule` line via `ADR-0004`.
2.  **Phase 1 / TASK-1501:** Complexity regime sweep (`exp_0300`) and selection via `ADR-0005`.
3.  **Phase 2 / TASK-1600:** Cloze Evolution Task on Wikipedia data.

No work on a "SuperCell v0" or other major new architectural concepts is to begin until these foundational phases are successfully completed.
