# EXPERIMENT: PiStream v3 — Diversity-First Evolution Architecture

**Version:** 1.0  
**Status:** SPECIFICATION  
**Last Updated:** 2026-01-27  
**Type:** Architecture Specification  
**Related:** PiStream v2.x (CLOSED), ARCHITECTURE.md, EVOLUTION_ENGINE.md

---

## Executive Summary

PiStream v3 introduces a **Diversity-First Evolution** architecture designed to overcome the fundamental limitations of PiStream v2.x, which demonstrated architectural inability to achieve positive `avg_fitness_delta` across all parameter configurations (2916 tested, 0 PASS).

**Core Innovation:** Three-phase evolution with explicit diversity accumulation before selection pressure, formal thresholds for phase transitions, and kill-criteria tied to diversity maintenance rather than fitness alone.

---

## Context: PiStream v2.x Closure

### Parametric Sweep Results

**Total Configurations Tested:** 2916  
**PASS:** 0  
**FAIL:** 2916  
**INVALID:** 0

**Parameter Grid:**
- `mutation_sigma_initial`: [0.03, 0.05, 0.07]
- `mutation_sigma_min`: [0.01, 0.02]
- `mutation_sigma_max`: [0.1, 0.15]
- `adaptive_gain`: [1.1, 1.3, 1.5]
- `tournament_k`: [2, 3, 4]
- `elitism_ratio`: [0.0, 0.05, 0.1]
- `diversity_penalty`: [0.0, 0.1, 0.2]
- `entropy_floor`: [0.0, 0.1, 0.2]

### Root Cause Analysis

**Architectural Limitations Identified:**

1. **Premature Selection Pressure:** Selection applied before sufficient diversity accumulation, leading to premature convergence.
2. **Diversity-Fitness Tradeoff:** No mechanism to prioritize diversity over fitness in early phases.
3. **Single-Phase Evolution:** All generations treated identically, regardless of population state.
4. **Entropy Collapse:** Entropy floor mechanisms insufficient to prevent diversity loss under selection pressure.

**Conclusion:** Parameter tuning insufficient. Architectural change required.

---

## PiStream v3 Architecture

### Core Principle: Diversity-First Evolution

**Philosophy:** Population must accumulate sufficient diversity **before** selection pressure is applied. Selection without diversity leads to premature convergence and fitness stagnation.

### Three-Phase Evolution Model

#### Phase 0: Diversity Accumulation (No Selection)

**Purpose:** Build population diversity without fitness-based selection pressure.

**Duration:** Until formal diversity threshold `D_MIN` is reached.

**Mechanisms:**
- **Pure Mutation:** All agents mutate every generation (no selection).
- **Diversity Maximization:** Mutations designed to maximize genotypic diversity.
- **No Fitness Pressure:** Fitness computed but not used for selection.
- **Entropy Tracking:** Monitor population entropy continuously.

**Transition Criteria:**
```
IF diversity >= D_MIN AND entropy >= E_MIN AND generation >= G_MIN:
    TRANSITION TO PHASE 1
```

**Formal Thresholds:**
- `D_MIN`: Minimum diversity index (default: 0.30)
- `E_MIN`: Minimum entropy (default: 2.5 bits)
- `G_MIN`: Minimum generations (default: 10)

**Metrics Tracked:**
- Population diversity index (genotypic distance)
- Shannon entropy of fitness distribution
- Genotypic variance
- Mutation rate (adaptive)

#### Phase 1: Evolution with Selection

**Purpose:** Apply selection pressure while maintaining diversity above threshold.

**Duration:** Until fitness convergence or diversity collapse detected.

**Mechanisms:**
- **Selection Enabled:** Tournament selection with diversity bonus.
- **Diversity Enforcement:** Agents below diversity threshold penalized.
- **Adaptive Mutation:** Mutation rate adjusted based on diversity trend.
- **Elitism with Diversity:** Elite selection includes diversity constraint.

**Selection Formula:**
```
fitness_selection = tournament_selection(fitness)
diversity_bonus = diversity_index * diversity_weight
combined_score = fitness_selection + diversity_bonus
```

**Diversity Maintenance:**
- If diversity < D_MIN: Increase mutation rate, reduce selection pressure.
- If diversity > D_MAX: Reduce mutation rate, increase selection pressure.

**Transition Criteria:**
```
IF avg_fitness_delta < threshold AND diversity >= D_MIN:
    TRANSITION TO PHASE 2 (Stabilization)
ELSE IF diversity < D_MIN:
    REVERT TO PHASE 0 (Diversity Recovery)
```

#### Phase 2: Stabilization

**Purpose:** Maintain evolved population without further exploration.

**Duration:** Fixed number of generations or until stability confirmed.

**Mechanisms:**
- **Reduced Mutation:** Lower mutation rate to preserve solutions.
- **Selection Only:** No new diversity injection.
- **Convergence Monitoring:** Track fitness stability.

**Exit Criteria:**
- Fitness variance < threshold for N consecutive generations.
- Maximum generations reached.

---

## Formal Thresholds and Parameters

### Diversity Thresholds

| Threshold | Symbol | Default Value | Purpose |
|-----------|--------|---------------|---------|
| Minimum Diversity | `D_MIN` | 0.30 | Phase 0 → Phase 1 transition |
| Maximum Diversity | `D_MAX` | 0.70 | Phase 1 diversity ceiling |
| Diversity Collapse | `D_COLLAPSE` | 0.15 | Trigger Phase 0 recovery |

### Entropy Thresholds

| Threshold | Symbol | Default Value | Purpose |
|-----------|--------|---------------|---------|
| Minimum Entropy | `E_MIN` | 2.5 bits | Phase 0 → Phase 1 transition |
| Entropy Floor | `E_FLOOR` | 1.5 bits | Kill-criterion trigger |

### Generation Thresholds

| Threshold | Symbol | Default Value | Purpose |
|-----------|--------|---------------|---------|
| Minimum Generations | `G_MIN` | 10 | Phase 0 minimum duration |
| Stabilization Generations | `G_STAB` | 20 | Phase 2 duration |

### Selection Parameters

| Parameter | Symbol | Default Value | Purpose |
|-----------|--------|---------------|---------|
| Tournament Size | `tournament_k` | 3 | Selection pressure |
| Diversity Weight | `diversity_weight` | 0.3 | Diversity bonus coefficient |
| Elitism Ratio | `elitism_ratio` | 0.05 | Elite preservation |

### Mutation Parameters

| Parameter | Symbol | Default Value | Purpose |
|-----------|--------|---------------|---------|
| Initial Mutation Rate | `mutation_rate_initial` | 0.1 | Phase 0 mutation rate |
| Selection Mutation Rate | `mutation_rate_selection` | 0.05 | Phase 1 mutation rate |
| Stabilization Mutation Rate | `mutation_rate_stabilization` | 0.01 | Phase 2 mutation rate |
| Adaptive Gain | `adaptive_gain` | 1.2 | Mutation rate adjustment factor |

---

## Kill-Criteria for PiStream v3

### Primary Kill-Criteria

**1. Diversity Collapse:**
```
IF diversity < D_COLLAPSE (0.15) AND entropy < E_FLOOR (1.5 bits):
    KILL: Architecture fails to maintain diversity
```

**2. Fitness Regression:**
```
IF avg_fitness_delta < -0.05 for 5 consecutive generations:
    KILL: Population fitness declining despite selection
```

**3. Phase 0 Failure:**
```
IF Phase 0 duration > 50 generations AND diversity < D_MIN:
    KILL: Cannot accumulate sufficient diversity
```

**4. Entropy Collapse:**
```
IF entropy < E_FLOOR (1.5 bits) for 3 consecutive generations:
    KILL: Population entropy collapsed
```

### Success Criteria

**Minimum Requirements:**
- Phase 0 completes within 50 generations.
- Phase 1 achieves `avg_fitness_delta > 0.01` for at least 10 consecutive generations.
- Diversity maintained above `D_MIN` throughout Phase 1.
- Phase 2 stabilizes fitness variance < 0.01.

**Target Metrics:**
- Final `avg_fitness` > 0.60 (baseline from PiStream v2.x: ~0.50).
- Final diversity > 0.25 (baseline from PiStream v2.x: ~0.15).
- `avg_fitness_delta` > 0.02 per generation (Phase 1 average).

---

## Relationship to PiStream v2.x Results

### Lessons Learned

1. **Diversity Must Precede Selection:** PiStream v2.x applied selection immediately, causing premature convergence.
2. **Parameter Tuning Insufficient:** 2916 configurations tested, none achieved positive fitness delta.
3. **Architectural Change Required:** Phase-based evolution necessary, not parameter adjustment.

### Architectural Differences

| Aspect | PiStream v2.x | PiStream v3 |
|--------|---------------|-------------|
| **Selection Timing** | Immediate (generation 1) | Delayed (after Phase 0) |
| **Diversity Priority** | Secondary (penalty only) | Primary (Phase 0 focus) |
| **Evolution Phases** | Single phase | Three phases |
| **Diversity Enforcement** | Penalty-based | Threshold-based |
| **Mutation Strategy** | Uniform | Phase-adaptive |

### Expected Improvements

- **Diversity:** +67% (0.15 → 0.25 target).
- **Fitness Delta:** Positive (vs. negative/zero in v2.x).
- **Convergence:** Controlled (vs. premature in v2.x).

---

## Implementation Requirements

### Phase Detection Logic

```python
def detect_phase(diversity, entropy, generation, fitness_delta):
    if diversity < D_MIN or entropy < E_MIN or generation < G_MIN:
        return PHASE_0  # Diversity accumulation
    elif diversity < D_COLLAPSE:
        return PHASE_0  # Recovery
    elif fitness_delta < STABILIZATION_THRESHOLD and diversity >= D_MIN:
        return PHASE_2  # Stabilization
    else:
        return PHASE_1  # Evolution with selection
```

### Diversity Computation

```python
def compute_diversity(population):
    # Genotypic distance matrix
    distances = pairwise_genotypic_distance(population)
    # Diversity index: mean pairwise distance normalized
    diversity_index = np.mean(distances) / max_possible_distance
    return diversity_index
```

### Selection with Diversity Bonus

```python
def select_with_diversity(population, tournament_k, diversity_weight):
    # Tournament selection on fitness
    fitness_winners = tournament_selection(population, k=tournament_k)
    # Diversity bonus
    diversity_scores = [compute_diversity([agent]) for agent in population]
    combined_scores = fitness_scores + diversity_weight * diversity_scores
    # Select based on combined score
    return select_by_score(population, combined_scores)
```

---

## Experimental Protocol

### Initial Configuration

- **Population Size:** 30 agents (TRL-3 requirement).
- **Generations:** 100 (Phase 0: 10-50, Phase 1: 30-80, Phase 2: 20).
- **PiStream Seeds:** Deterministic (ENV_PISTREAM, MUT_DECISION_PISTREAM, MUT_MAGNITUDE_PISTREAM).

### Metrics Collection

**Per Generation:**
- Population diversity index.
- Shannon entropy.
- Average fitness.
- Fitness delta (vs. previous generation).
- Phase identifier.
- Mutation rate.

**Per Phase:**
- Phase duration (generations).
- Phase transition triggers.
- Diversity trend (slope).
- Fitness trend (slope).

**Final:**
- Total generations.
- Final diversity.
- Final entropy.
- Final fitness.
- Fitness improvement (delta from initial).
- Phase distribution (0/1/2).

### Validation Requirements

1. **Reproducibility:** Same seeds → same results (within tolerance).
2. **Determinism:** PiStream-based randomness only.
3. **Kill-Criteria Compliance:** No kill-criteria violations.
4. **Phase Transitions:** Documented and justified.

---

## Relationship to BDC Architecture

### Task Class Alignment

**PiStream v3 belongs to Class 1 (Core Validation):**
- Validates foundational hypotheses (H1, H2, H3).
- CPU/simulation only (no GPU until TRL5 closed).
- PiStream tests, exact recall, recovery rate.

### Integration Points

- **ARCHITECTURE.md:** Implements Class 1 requirements.
- **EVOLUTION_ENGINE.md:** Extends evolutionary mechanisms.
- **RESEARCH_METHODOLOGY.md:** Follows kill-criteria validation.
- **SEED_POLICY.md:** Uses PiStream streams (ENV, MUT_DECISION, MUT_MAGNITUDE).

### Scaling Limits

- **Max Agents:** 30 (TRL-3 requirement).
- **Stop-Scaling Criteria:** Signal-to-noise ratio < 0.1.

---

## Future Work

### Phase 3 Extensions (Post-v3)

- **Multi-Objective Evolution:** Fitness + diversity Pareto optimization.
- **Adaptive Thresholds:** D_MIN, E_MIN learned from population dynamics.
- **Hybrid Selection:** Combine tournament + diversity-based selection.
- **Migration:** Island-model diversity injection (BDC HIVE integration).

### Research Questions

1. **Optimal D_MIN:** What diversity threshold maximizes fitness improvement?
2. **Phase Duration:** How long should Phase 0 last for best results?
3. **Diversity Metrics:** Which diversity measure best predicts fitness improvement?
4. **Recovery Mechanisms:** How to recover from diversity collapse in Phase 1?

---

## References

- **ARCHITECTURE.md:** Core BDC architecture and task classes.
- **EVOLUTION_ENGINE.md:** Evolutionary mechanisms and PiStream v1 stagnation analysis.
- **RESEARCH_METHODOLOGY.md:** Kill-criteria and validation standards.
- **analysis/PISTREAM_PARAMETRIC_SWEEP_SUMMARY.json:** PiStream v2.x parametric sweep results.
- **PISTREAM_PARAMETRIC_SWEEP_REPORT.md:** Detailed v2.x analysis.

---

**EXPERIMENT_PISTREAM_V3.md Status:** SPECIFICATION  
**Next Review:** After implementation begins or major design changes  
**Implementation Priority:** HIGH (mandatory after v2.x closure)
