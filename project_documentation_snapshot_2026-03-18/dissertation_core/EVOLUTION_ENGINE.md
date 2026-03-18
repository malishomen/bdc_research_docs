# BDC Evolution Engine

**Version:** 1.0  
**Status:** CANONICAL  
**Last Updated:** 2026-01-27  
**Implements:** ARCHITECTURE.md Class 1 and Class 2 requirements

---

## Overview

This document explicitly describes the evolutionary mechanisms used in BDC, including mutation strength, selection pressure, diversity enforcement, and the root causes of PiStream v1 stagnation.

---

## Evolutionary Pressure

### Definition

**Evolutionary pressure** is the force that drives population change through:
1. **Selection:** Favoring higher-fitness agents
2. **Mutation:** Introducing variation
3. **Diversity enforcement:** Preventing premature convergence

### Selection Pressure

**Formula:**
```
selection_pressure = (fitness_variance / mean_fitness) × selection_fraction
```

Where:
- `fitness_variance`: Variance of fitness across population
- `mean_fitness`: Average fitness of population
- `selection_fraction`: Proportion of population selected for reproduction (typically 0.3-0.5)

**Target Range:** 0.1 - 0.3

**Too Low (< 0.1):** Population stagnates, no improvement
**Too High (> 0.3):** Premature convergence, loss of diversity

### Mutation Strength

**Definition:** Magnitude of parameter changes introduced by mutations.

**Formula (for genome parameters):**
```
mutation_strength = base_mutation_rate × mutation_magnitude_multiplier
```

Where:
- `base_mutation_rate`: Default mutation probability (0.03 - 0.07)
- `mutation_magnitude_multiplier`: Amplitude of change (1.0 - 3.0)

**PiStream v1 Values (INSUFFICIENT):**
- `base_mutation_rate`: 0.01 - 0.03 (too low)
- `mutation_magnitude_multiplier`: 0.5 - 1.0 (too conservative)
- **Result:** Mutations too small to escape local optima

**PiStream v2 Values (CORRECTED):**
- `base_mutation_rate`: 0.03 - 0.07 (increased)
- `mutation_magnitude_multiplier`: 1.5 - 3.0 (increased)
- **Result:** Sufficient variation to explore fitness landscape

### Diversity Enforcement

**Mechanism:** Explicit diversity maintenance to prevent premature convergence.

**Metrics:**
- **Population diversity:** Pairwise distance between agent states
- **Target diversity:** ≥ 0.15 (for Class 1), ≥ 0.20 (for Class 2)
- **Convergence threshold:** Diversity < 0.10 triggers diversity injection

**Diversity Injection:**
When diversity drops below threshold:
1. **Immigration:** Introduce random new agents (10-20% of population)
2. **Mutation boost:** Increase mutation rate by 2x for 5-10 generations
3. **Niche protection:** Preserve top agents from each fitness cluster

---

## PiStream v1 Stagnation: Root Cause Analysis

### Symptoms Observed

1. **Fitness plateau:** Average fitness stopped improving after ~100 generations
2. **Diversity collapse:** Population diversity dropped from 0.25 to < 0.10
3. **Premature convergence:** All agents converged to similar strategies
4. **No escape:** Mutations failed to generate better solutions

### Root Causes

#### 1. Insufficient Mutation Strength

**Problem:**
- Mutation rate: 0.01 - 0.03 (too low)
- Mutation magnitude: 0.5 - 1.0 (too small)
- Result: Mutations too weak to escape local optima

**Evidence:**
- Fitness variance decreased over time (sign of convergence)
- No exploration of distant regions of parameter space
- Stuck in local fitness peaks

#### 2. Weak Selection Pressure

**Problem:**
- Selection fraction: 0.1 - 0.2 (too low)
- Fitness variance: Decreased over time (reduced pressure)
- Result: Insufficient force to drive improvement

**Evidence:**
- Top 10% agents similar to bottom 10% (low pressure)
- Slow fitness improvement rate
- No clear fitness gradient

#### 3. Lack of Diversity Enforcement

**Problem:**
- No explicit diversity maintenance mechanism
- No immigration of new agents
- No niche protection
- Result: Population converged to single strategy

**Evidence:**
- Diversity dropped from 0.25 to < 0.10
- All agents had similar parameters
- No exploration-exploitation balance

#### 4. Signal-to-Noise Degradation

**Problem:**
- Fitness improvements became indistinguishable from noise
- No mechanism to detect genuine improvement vs. random fluctuation
- Result: Evolution stopped "believing" in improvements

**Evidence:**
- Fitness variance < 0.01 (below noise floor)
- No statistical significance in fitness changes
- Population Governor would have stopped scaling (but didn't exist)

### Resolution (PiStream v2)

**Changes:**
1. **Increased mutation strength:** 0.03 - 0.07 rate, 1.5 - 3.0 magnitude
2. **Stronger selection pressure:** 0.3 - 0.5 selection fraction, maintain fitness variance
3. **Diversity enforcement:** Explicit mechanisms, immigration, niche protection
4. **Population Governor:** Automatic stop-scaling when signal-to-noise < 0.1

**Expected Outcome:**
- Sustained fitness improvement over 500+ generations
- Diversity maintained ≥ 0.15
- Escape from local optima
- Statistical significance in improvements

---

## Mutation Mechanisms

### Deterministic Mutation via PiStream

**Rule:** All mutations MUST be deterministic and reproducible via PiStream.

**Streams:**
- `MUT_DECISION_PISTREAM`: Which parameters to mutate
- `MUT_MAGNITUDE_PISTREAM`: How much to mutate

**Violation:** Using non-PiStream randomness invalidates reproducibility.

### Mutation Types

#### 1. Point Mutations

**Definition:** Single parameter change within allowed range.

**Formula:**
```
new_value = old_value + (MUT_MAGNITUDE_PISTREAM.next() - 1.5) × mutation_strength × range
```

Where:
- `range`: Parameter's allowed range (e.g., [0, 1])
- `mutation_strength`: Current mutation strength (0.03 - 0.07)

#### 2. Segment Mutations

**Definition:** Multiple consecutive parameters changed together.

**Use Case:** Preserving parameter correlations (e.g., sensor weights)

**Formula:**
```
segment_length = MUT_DECISION_PISTREAM.next() % max_segment_length
segment_start = MUT_DECISION_PISTREAM.next() % (genome_length - segment_length)
for i in range(segment_start, segment_start + segment_length):
    genome[i] = mutate(genome[i])
```

#### 3. Adaptive Mutations

**Definition:** Mutation strength adjusted based on fitness improvement rate.

**Formula:**
```
if fitness_improvement_rate < threshold:
    mutation_strength *= 1.5  # Increase exploration
else:
    mutation_strength *= 0.9  # Decrease (fine-tuning)
```

**Bounds:** mutation_strength must stay within [0.03, 0.07]

---

## Selection Mechanisms

### Fitness-Based Selection

**Method:** Rank agents by fitness, select top fraction.

**Formula:**
```
selected_count = floor(population_size × selection_fraction)
selected_agents = sorted(agents, key=fitness, reverse=True)[:selected_count]
```

**Selection Fraction:**
- **Class 1 (Core):** 0.3 - 0.4 (moderate pressure)
- **Class 2 (Cognitive):** 0.4 - 0.5 (higher pressure for competition)

### Tournament Selection

**Alternative Method:** Random tournaments, winner advances.

**Formula:**
```
tournament_size = 3 - 5
for each slot in next_generation:
    tournament = random.sample(population, tournament_size)
    winner = max(tournament, key=fitness)
    next_generation.append(winner)
```

**Use Case:** Maintains diversity better than pure fitness ranking.

### Elitism

**Rule:** Always preserve top N agents (typically 10-20% of population).

**Rationale:** Prevents loss of best solutions due to bad luck.

**Formula:**
```
elite_count = floor(population_size × elitism_fraction)
elite = sorted(agents, key=fitness, reverse=True)[:elite_count]
next_generation.extend(elite)
```

---

## Diversity Maintenance

### Diversity Metrics

**Pairwise Distance:**
```
diversity = mean(pairwise_distance(agent_i.state, agent_j.state) 
                 for all i, j where i < j)
```

**Target Values:**
- **Class 1:** ≥ 0.15
- **Class 2:** ≥ 0.20

### Diversity Injection Mechanisms

#### 1. Immigration

**Definition:** Introduce random new agents when diversity drops.

**Formula:**
```
if diversity < threshold:
    immigration_count = floor(population_size × 0.1)
    new_agents = [create_random_agent() for _ in range(immigration_count)]
    population.extend(new_agents)
    population = select(population, target_size)  # Trim back
```

#### 2. Mutation Boost

**Definition:** Temporarily increase mutation rate to escape convergence.

**Formula:**
```
if diversity < threshold:
    mutation_strength *= 2.0
    boost_duration = 5 - 10 generations
```

#### 3. Niche Protection

**Definition:** Preserve best agent from each fitness cluster.

**Formula:**
```
clusters = cluster_agents_by_fitness(population, num_clusters=5)
protected_agents = [max(cluster, key=fitness) for cluster in clusters]
next_generation.extend(protected_agents)
```

---

## Fitness Functions

### Class 1 (Paramecium MVP)

**Formula:**
```
fitness = reward_food 
        - penalty_collisions 
        - penalty_toxin 
        - penalty_energy 
        - penalty_genome_size
```

Where:
- `reward_food`: Positive reward for finding food
- `penalty_collisions`: Negative for collisions
- `penalty_toxin`: Negative for toxin exposure
- `penalty_energy`: Negative for energy consumption (actions/turns/time)
- `penalty_genome_size`: Negative for oversized genomes (anti-cheat)

**Anti-Cheat:** Prevents agents from "cheating" via infinite scanning or genome bloat.

### Class 2 (Cognitive Co-Evolution)

**Formula:**
```
fitness = task_performance 
        + 0.1 × alignment 
        + 0.05 × diversity 
        - 0.02 × energy_cost
```

Where:
- `task_performance`: Primary task success (0-1)
- `alignment`: Belief alignment with population (0-1)
- `diversity`: Individual contribution to population diversity (0-1)
- `energy_cost`: Computational/resource cost (normalized)

---

## Evolutionary Loop

### Standard Loop (Class 1)

```
1. Initialize population (N agents, PiStream-seeded)
2. For each generation:
   a. Evaluate fitness for all agents
   b. Check diversity (if < threshold, inject diversity)
   c. Select top fraction (selection_pressure)
   d. Mutate selected agents (MUT_DECISION, MUT_MAGNITUDE streams)
   e. Create next generation (selected + mutated + elite)
   f. Check stop-scaling criteria (signal-to-noise, convergence)
3. Return best agent(s) and metrics
```

### Co-Evolutionary Loop (Class 2)

```
1. Initialize population (N cognitive agents)
2. For each episode:
   a. Agents interact in environment
   b. Compute fitness (task + social metrics)
   c. Update beliefs and knowledge
   d. Form social clusters
   e. Knowledge transfer between agents
   f. Select and mutate (with diversity enforcement)
   g. Check convergence (diversity, alignment)
3. Return population state and emergence metrics
```

---

## Stop-Scaling Criteria

**Population Governor** automatically stops scaling when:

1. **Signal-to-noise ratio < 0.1:**
   ```
   signal_to_noise = fitness_improvement_rate / fitness_variance
   if signal_to_noise < 0.1: STOP
   ```

2. **Diversity < 0.10:**
   ```
   if diversity < 0.10: STOP (convergence detected)
   ```

3. **Convergence > 95%:**
   ```
   convergence = agents_with_similar_fitness / total_agents
   if convergence > 0.95: STOP
   ```

4. **Resource exhaustion:**
   ```
   if GPU_utilization < 50% or OOM_errors: STOP
   ```

**Override:** Requires explicit ADR and justification.

---

## Validation Requirements

All evolutionary mechanisms must be validated with:

1. **Reproducibility:** Same seeds → same mutations
2. **Diversity maintenance:** Diversity ≥ target over 100+ generations
3. **Fitness improvement:** Sustained improvement (not just noise)
4. **Statistical significance:** t-test, confidence intervals

**Evidence Standard:** See RESEARCH_METHODOLOGY.md

---

**EVOLUTION_ENGINE.md Status:** CANONICAL & OPERATIONAL  
**Next Review:** After PiStream v2 validation or major mechanism changes
