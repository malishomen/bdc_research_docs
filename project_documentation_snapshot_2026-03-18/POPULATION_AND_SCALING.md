# BDC Population and Scaling

**Version:** 1.0  
**Status:** CANONICAL  
**Last Updated:** 2026-01-27  
**Implements:** ARCHITECTURE.md scaling limits and Population Governor

---

## Overview

This document defines formal limits on agent counts by task class, noise vs signal rules, stop-scaling criteria, and the Population Governor concept.

**Core Principle:** More agents ≠ better results. Scaling must stop when signal-to-noise ratio degrades or resources are exhausted.

---

## Agent Count Limits by Task Class

### Class 1: Core Validation (TRL 1-5)

**Maximum Agents:** 30

**Rationale:**
- Statistical validity requires N≥30 for significance testing
- Deterministic PiStream limits practical population size
- Signal-to-noise ratio degrades beyond 30 agents
- Computational cost grows quadratically with agent interactions

**Validation Requirements:**
- N≥30 fixed seeds for each experiment
- At least 2 baselines for comparison
- Exact recall, recovery rate, calibration metrics

**Stop-Scaling Criteria:**
- Signal-to-noise ratio < 0.1
- Diversity < 0.15
- Convergence > 95%

### Class 2: Cognitive Co-Evolution (TRL 6-9)

**Maximum Agents:** 50

**Rationale:**
- Co-evolution complexity requires larger populations for cluster formation
- Social organization emerges with 20-50 agents
- Diversity maintenance becomes difficult beyond 50
- Computational cost (attention mechanisms) scales with N²

**Validation Requirements:**
- Fitness, diversity, alignment metrics
- Cluster formation and role differentiation
- Knowledge transfer effectiveness

**Stop-Scaling Criteria:**
- Diversity < 0.15
- Convergence > 95%
- GPU utilization < 50% (if GPU-accelerated)
- OOM (Out of Memory) errors

### Class 3: Knowledge Integration (TRL 10+)

**Maximum Agents:** 50

**Rationale:**
- GPU memory constraints (11GB VRAM typical)
- Population dynamics network scales with N²
- Batch processing efficiency degrades beyond 50
- Knowledge extraction overhead grows linearly

**Validation Requirements:**
- Comprehension scores
- Entity discovery rates
- Knowledge diversity metrics

**Stop-Scaling Criteria:**
- GPU utilization < 50%
- OOM errors
- Batch size must drop below 32
- Training time per episode > 2x baseline

---

## Noise vs Signal Rules

### Signal Definition

**Signal** is measurable improvement in target metrics:

- **Fitness improvement:** Sustained increase over 10+ episodes
- **Recall improvement:** Exact recall increases (for H2 validation)
- **Recovery improvement:** Recovery rate increases (for H3 validation)
- **Diversity maintenance:** Diversity stays ≥ target threshold

### Noise Definition

**Noise** is variance, drift, or random fluctuations:

- **Fitness variance:** Random fluctuations around mean
- **Measurement error:** Instrumentation or sampling error
- **Environmental drift:** Non-deterministic environment changes
- **Numerical precision:** Floating-point rounding errors

### Signal-to-Noise Ratio

**Formula:**
```
signal_to_noise = improvement_rate / fitness_variance
```

Where:
- `improvement_rate`: Rate of fitness improvement (per episode)
- `fitness_variance`: Variance of fitness across population

**Target:** signal_to_noise ≥ 0.1

**Below 0.1:** Improvements indistinguishable from noise → STOP SCALING

### Measurement Protocol

1. **Baseline measurement:**
   - Run 100 episodes with current population size
   - Measure fitness_mean, fitness_variance
   - Compute improvement_rate = (fitness_final - fitness_initial) / 100

2. **Signal-to-noise calculation:**
   ```
   signal_to_noise = improvement_rate / fitness_variance
   ```

3. **Decision:**
   - If signal_to_noise ≥ 0.1: Continue scaling (if under max limit)
   - If signal_to_noise < 0.1: STOP SCALING (Population Governor triggers)

---

## Stop-Scaling Criteria

### Automatic Stop Triggers

The **Population Governor** automatically stops scaling when any of these criteria are met:

#### 1. Signal-to-Noise Ratio < 0.1

**Condition:**
```
signal_to_noise = improvement_rate / fitness_variance < 0.1
```

**Action:**
- Stop increasing agent count
- Log warning: "Signal-to-noise ratio below threshold"
- Continue training with current population size

**Override:** Requires explicit ADR and justification

#### 2. Diversity < Threshold

**Condition:**
```
diversity < threshold
```

Where:
- Class 1: threshold = 0.15
- Class 2: threshold = 0.15
- Class 3: threshold = 0.20

**Action:**
- Stop scaling
- Trigger diversity injection (see EVOLUTION_ENGINE.md)
- Log warning: "Diversity below threshold, injection triggered"

**Override:** Not recommended (diversity is critical for evolution)

#### 3. Convergence > 95%

**Condition:**
```
convergence = agents_with_similar_fitness / total_agents > 0.95
```

Where "similar" means fitness within 0.01 of each other.

**Action:**
- Stop scaling
- Trigger mutation boost (see EVOLUTION_ENGINE.md)
- Log warning: "Premature convergence detected"

**Override:** Requires explicit ADR and justification

#### 4. Resource Exhaustion

**Conditions:**
- GPU utilization < 50% (inefficient resource use)
- OOM (Out of Memory) errors
- Training time per episode > 2x baseline
- Batch size must drop below 32

**Action:**
- Stop scaling immediately
- Log error: "Resource exhaustion, scaling stopped"
- Reduce population if necessary to restore stability

**Override:** Not allowed (hardware limits are absolute)

---

## Population Governor

### Concept

The **Population Governor** is a mandatory component that enforces agent count limits and stop-scaling criteria.

**Purpose:**
- Prevent wasteful scaling beyond useful limits
- Maintain signal-to-noise ratio
- Preserve computational resources
- Ensure diversity and prevent convergence

### Implementation

**Location:** `evolution/population_governor.py`

**Interface:**
```python
class PopulationGovernor:
    def __init__(
        self,
        task_class: TaskClass,
        max_agents: int,
        signal_to_noise_threshold: float = 0.1,
        diversity_threshold: float = 0.15,
    ):
        ...
    
    def should_scale(
        self,
        current_agents: int,
        fitness_history: List[float],
        diversity: float,
        convergence: float,
        resource_metrics: Dict,
    ) -> Tuple[bool, str]:
        """
        Returns (should_scale, reason)
        """
        ...
    
    def get_max_agents(self) -> int:
        """Returns maximum allowed agents for task class"""
        ...
```

### Decision Logic

```python
def should_scale(...) -> Tuple[bool, str]:
    # Check hard limit
    if current_agents >= self.max_agents:
        return False, "Maximum agent count reached"
    
    # Check signal-to-noise
    signal_to_noise = compute_signal_to_noise(fitness_history)
    if signal_to_noise < self.signal_to_noise_threshold:
        return False, f"Signal-to-noise ratio {signal_to_noise:.3f} < {self.signal_to_noise_threshold}"
    
    # Check diversity
    if diversity < self.diversity_threshold:
        return False, f"Diversity {diversity:.3f} < {self.diversity_threshold}"
    
    # Check convergence
    if convergence > 0.95:
        return False, f"Convergence {convergence:.3f} > 0.95"
    
    # Check resources
    if resource_metrics['gpu_util'] < 0.50:
        return False, f"GPU utilization {resource_metrics['gpu_util']:.1%} < 50%"
    
    if resource_metrics.get('oom_errors', 0) > 0:
        return False, "OOM errors detected"
    
    # All checks passed
    return True, "Scaling allowed"
```

### Override Mechanism

**Requirement:** Explicit ADR documenting:
- Why override is necessary
- What alternative validation will be used
- How signal-to-noise will be maintained
- Resource impact assessment

**Process:**
1. Create ADR with override justification
2. Update Population Governor configuration
3. Document override in experiment metadata
4. Monitor closely for degradation

---

## Scaling Strategies

### Linear Scaling

**Definition:** Add agents one at a time until limit or stop criteria.

**Formula:**
```
next_population_size = min(current_agents + 1, max_agents)
```

**Use Case:** Initial exploration, unknown optimal size

**Stop Condition:** Any stop-scaling criterion triggers

### Exponential Scaling

**Definition:** Double population size at each step until limit.

**Formula:**
```
next_population_size = min(current_agents * 2, max_agents)
```

**Use Case:** Rapid exploration of population size space

**Stop Condition:** Any stop-scaling criterion triggers

**Warning:** May overshoot optimal size quickly

### Adaptive Scaling

**Definition:** Adjust scaling rate based on signal-to-noise ratio.

**Formula:**
```
if signal_to_noise > 0.2:
    scale_rate = 1.5  # Aggressive scaling
elif signal_to_noise > 0.1:
    scale_rate = 1.2  # Moderate scaling
else:
    scale_rate = 1.0  # Stop scaling

next_population_size = min(int(current_agents * scale_rate), max_agents)
```

**Use Case:** Optimal balance between exploration and efficiency

**Stop Condition:** signal_to_noise < 0.1 or other stop criteria

---

## Validation Requirements

All scaling decisions must be validated with:

1. **Signal-to-noise measurement:** Before and after scaling
2. **Diversity monitoring:** Ensure diversity maintained
3. **Resource monitoring:** GPU/utilization, memory, time
4. **Statistical significance:** t-test for fitness improvements

**Evidence Standard:** See RESEARCH_METHODOLOGY.md

---

## Examples

### Example 1: Class 1 Scaling

**Initial:** 10 agents  
**Target:** 30 agents (max for Class 1)  
**Strategy:** Linear scaling, +1 agent per 50 episodes

**Result:**
- Reached 30 agents after 1000 episodes
- Signal-to-noise maintained ≥ 0.15 throughout
- Diversity maintained ≥ 0.20
- **Conclusion:** Scaling successful, limit reached

### Example 2: Class 2 Premature Stop

**Initial:** 20 agents  
**Target:** 50 agents (max for Class 2)  
**Strategy:** Exponential scaling, double every 100 episodes

**Result:**
- Reached 40 agents after 200 episodes
- Signal-to-noise dropped to 0.08 at 40 agents
- **Population Governor triggered:** Stop scaling
- **Conclusion:** Optimal size is 35-40 agents for this task

### Example 3: Class 3 Resource Limit

**Initial:** 30 agents  
**Target:** 50 agents (max for Class 3)  
**Strategy:** Linear scaling, +5 agents per checkpoint

**Result:**
- Reached 45 agents
- OOM error at 45 agents (GPU memory exhausted)
- **Population Governor triggered:** Stop scaling, reduce to 40
- **Conclusion:** Hardware limit reached, optimal size is 40 agents

---

## Relationship to Other Documents

- **ARCHITECTURE.md:** Defines task classes and max limits (referenced)
- **EVOLUTION_ENGINE.md:** Defines diversity enforcement (implements)
- **RESEARCH_METHODOLOGY.md:** Defines validation requirements (implements)
- **CHECKPOINT_SYSTEM_V2.md:** Checkpoints include population size (references)

---

**POPULATION_AND_SCALING.md Status:** CANONICAL & OPERATIONAL  
**Next Review:** After Population Governor implementation or limit changes
