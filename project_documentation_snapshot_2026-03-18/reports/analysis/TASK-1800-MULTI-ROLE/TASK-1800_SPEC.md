# TASK-1800: Phase 4 Multi-Role Evolution — Experiment Specification

**Date:** 2026-03-01  
**Status:** SPEC (pre-implementation)  
**Prerequisite:** Phase 2 PASS (ADR-0008), Phase 3 closure (ADR-0009), Phase 2 penalty regime (ADR-0005 Regime B)

---

## Scope

Implement Phase 4 (Specialization & Cooperation) per `docs/project/project_roadmap.md`:
- Multi-role evolution with collective fitness
- Minimum 3 micro-tasks derived from simplified_wiki
- Roles emerge from evolution, not assignment
- **Energy model:** NOT used (per ADR-0009). Phase 2 penalty regime (`lambda=0.01`, Regime B) is canonical.

---

## Micro-Task Suite

### 1. Cloze Prediction (existing)

- **Source:** Phase 2 infrastructure (`evolution/cloze_symbolic/`)
- **Input:** Context (prev, next tokens, position)
- **Output:** Predicted token_id from candidate set
- **Metric:** Hard accuracy (% correct token predictions)
- **No changes** to existing task or genome evaluation.

### 2. Entity Detection (binary, derived)

- **Definition:** Predict whether the masked token is a *named entity* (binary: entity=1, non-entity=0).
- **Derivation:** `target_is_entity = raw_token[0].isupper() and len(raw_token)>1` at sample build time. Heuristic proxy for NER (no wiki markup in simplified_wiki).
- **Shared samples:** Same `ClozeSample` set as cloze; add `target_is_entity: bool` (and optional `candidate_is_entity: List[bool]` for candidate set).
- **Evaluation:** Genome predicts token_id → map to `candidate_is_entity[argmax]`. Correct if `predicted_entity == target_is_entity`.
- **Data requirement:** Tokenization pass must preserve case for entity labels. Hash remains on lowercased token for compatibility with cloze vocabulary.
- **Implementation:** Extend `build_cloze_task` to optionally produce `EntityTaskData` overlay, or extend `ClozeTaskData` with `target_is_entity` per sample and `candidate_is_entity` per candidate.

### 3. Category Classification (document-level proxy)

- **Constraint:** simplified_wiki has no categories. Use synthetic proxy.
- **Option A (minimal):** Document-level binary: "long" vs "short" — `doc_is_long = (token_count(doc) >= median)`.
  - Sample: one representative (e.g. first masked sample) per doc.
  - Organism prediction: aggregate over doc (e.g. predict from first sample's context).
  - Weak specialization signal.
- **Option B (recommended):** Synthetic category from `hash(doc_id) % num_categories`.
  - `num_categories = 4` or `8`.
  - Deterministic, creates document diversity.
  - Sample: (doc_id, list of masked positions, category_id). Organism sees context of one sample per doc; prediction = category. Genome must produce category logits — **requires extended evaluation** (not just argmax token).
- **Option C (defer):** Implement cloze + entity first; add category in TASK-1800-B if needed for 3-task gate.

**Decision:** Start with **Option C** — 2 micro-tasks (cloze + entity) for MVP. If success criteria allow 2-task collective, proceed. Otherwise add category in follow-up.

**Fallback to 3 tasks:** If governance requires 3 tasks before gate, implement Option A (doc long/short) with minimal genome extension: use `position_norm` and `doc_length_norm` as extra features; add a binary "doc head" to genome output (small R0 change).

---

## Collective Fitness

```
collective_fitness(population) = weighted_mean(
  best_cloze_accuracy(population),
  best_entity_accuracy(population)  [, best_category_accuracy if 3 tasks]
)
```

**Individual fitness (contribution_to_collective):**

- **Scheme S1 (specialist-friendly):** `individual_fitness = max(cloze_acc, entity_acc)` — organism gets credit for excelling at any single task.
- **Scheme S2 (Shapley-like):** marginal contribution when added to a "committee" of best-per-task. More expensive to compute.
- **Scheme S3 (weighted sum):** `individual_fitness = 0.5*cloze_acc + 0.5*entity_acc` — favors generalists.

**Recommendation:** S1 for Phase 4 — simple, encourages specialization (organism can thrive by being best at entity even if weak at cloze). ADR-0007 will formalize.

---

## Protocol (per roadmap)

| Parameter | Value |
|-----------|-------|
| N seeds | 30 |
| G generations | 100 |
| P population | 200 |
| Subset size | 100 docs |
| Dataset | simplified_wiki_v0 (same as Phase 2) |
| Genome | ClozeGenome v2 (`--use_skip_bigram`) |
| Complexity | Regime B, `lambda=0.01` |
| Energy model | **Off** (ADR-0009) |
| Speciation | Active |

---

## Success Criteria (from roadmap)

1. `collective_performance > best_single_role_individual_performance` with 95% CI.
2. Stable role diversity: ≥ 2 distinct functional groups in ≥ 24/30 seeds at gen 100.
3. Role necessity: removing any functional group degrades collective performance by ≥ 5%.

## Kill Criteria

- `collective_performance <= best_individual_performance` → cooperation not emerging
- Mono-role dominance (one role > 90% of population) in > 20/30 seeds → specialization not occurring
- Roles interchangeable (removing one doesn't degrade > 2%) → division superficial
- Mass extinction of minority roles → ecosystem not stable

---

## Implementation Order

1. **TASK-1800-PREP:** Extend `ClozeTaskData` / build with `target_is_entity` and `candidate_is_entity`; add entity evaluation path.
2. **TASK-1800-PREP:** Implement `evolution/collective_fitness.py` (collective + individual fitness, Scheme S1).
3. **TASK-1800-RUN:** Implement `evolution/cloze_symbolic/run_generations_multirole.py` or extend `run_generations.py` with `--collective` flag.
4. **TASK-1800-RUN:** Create `scripts/edp1/run_phase4_multirole.py` for N=30 sweep.
5. **TASK-1800-REPORT:** Analyze role clusters, cooperation metrics, BRIEF_REPORT.

---

## Deliverables (from roadmap)

- `evolution/collective_fitness.py` — collective evaluation module
- `evolution/micro_tasks/` — entity evaluation (and optional category) modules
- `results/edp1_exp0600_multirole/` — run artifacts
- `reports/analysis/TASK-1800-MULTI-ROLE/TASK-1800_BRIEF_REPORT.md`
- `decisions/ADR-0007-collective-fitness.md` (at gate)

---

## Rollback

- Collective fitness behind `--collective` flag; flag-off restores individual (cloze-only) fitness.
- Entity overlay is additive; no change to default cloze path.

---

## Links

- Roadmap: `docs/project/project_roadmap.md` (Phase 4)
- ADR-0009: `decisions/ADR-0009-energy-model-results.md`
- ADR-0005: `decisions/ADR-0005-complexity-regime.md`
- Phase 2 gate: TASK-1607, ADR-0008
