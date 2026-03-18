# COGNITIVE PROTOCOL - TRL-8 Canonical Knowledge Exchange

**Version:** 0.8.1  
**Status:** CANONICAL  
**Last Updated:** 2026-01-24

---

## Overview

The Cognitive Protocol defines the canonical format and semantics for knowledge exchange between cognitive agents in the TRL-8 Cognitive Co-Evolution Framework.

---

## Knowledge Package Specification

### Structure

```json
{
  "source_agent": 42,
  "topic": "strategy",
  "confidence": 0.8,
  "semantic_knowledge": {
    "pattern_0": 0.75,
    "pattern_1": 0.62
  },
  "beliefs": [
    {
      "content": "fitness is improving",
      "confidence": 0.85,
      "evidence_count": 15
    }
  ],
  "episode": 125,
  "timestamp": "2026-01-24T00:30:00Z"
}
```

### Fields

| Field | Type | Description |
|-------|------|-------------|
| source_agent | int | ID of teaching agent |
| topic | str | Knowledge topic (strategy/fitness/environment) |
| confidence | float | Source confidence (0-1) |
| semantic_knowledge | dict | Key-value pairs of learned patterns |
| beliefs | list | Believed propositions with confidence |
| episode | int | Episode number when knowledge created |
| timestamp | ISO8601 | Moment of knowledge creation |

---

## Transfer Protocol

### Teaching Initiation

1. Agent enters `TEACHING` cognitive state
2. Selects best learned knowledge
3. Packages with confidence metric
4. Broadcasts to social cluster

### Learning Reception

1. Recipient agent enters `LEARNING` state
2. Receives knowledge package
3. Evaluates source reputation
4. Integrates weighted by confidence
5. Updates internal beliefs

### Integration Formula

```
New Knowledge = α × Source Knowledge + (1-α) × Existing Knowledge

where α = Source Confidence × Recipient Learning Rate
```

### Effectiveness Metric

```
Effectiveness = Fitness Gain × Source Reputation / Recipient Fitness

Tracked per (source, recipient) pair over time
```

---

## Belief Updating Protocol

### Evidence Processing

```
Belief Update:
  confidence(new) = confidence(old) + evidence_strength × direction
  
  where:
    direction = +1 (supporting evidence)
                -1 (contradicting evidence)
                
    evidence_strength = |observation - prediction|
```

### Belief Consolidation

Every 10 episodes:
- High-confidence beliefs (>0.8) → semantic knowledge
- Contradicted beliefs (<0.2) → removed
- Moderate beliefs → kept for reasoning

---

## Social Learning Network

### Cluster Formation

```
Similarity Metric = 1 - Fitness Distance / Max Possible Distance

Agents join cluster if similarity > threshold (0.5)
```

### Within-Cluster Exchange

- Probability: 0.7 per agent per episode
- Type: Mostly within-cluster (high cohesion benefit)
- Effectiveness: Cluster cohesion × base effectiveness

### Between-Cluster Exchange

- Probability: 0.1 per agent per episode
- Type: Rare cross-cluster bridging
- Effectiveness: 0.5 × base effectiveness (diversity cost)

---

## Role-Based Knowledge Sharing

### Teacher Role

- Shares frequently (probability 0.6 per episode)
- High confidence threshold (>0.7)
- Reputation gains when learners improve
- Penalty if shared knowledge leads to failures

### Learner Role

- Receives frequently (probability 0.8 per episode)
- Integrates weighted by source reputation
- Updates beliefs from received knowledge
- Reputation gains when integrated knowledge helps

### Specialist Roles

- Narrow knowledge domains
- High confidence in specialty
- Limited cross-domain teaching
- Effective for within-cluster depth

### Generalist Roles

- Broad shallow knowledge
- Bridge between clusters
- Enable diversity through connections
- Moderate confidence across domains

---

## Collective Memory Format

### Successful Strategy Record

```json
{
  "episode": 125,
  "population_fitness": 0.62,
  "strategy_characteristics": [
    "high_teaching",
    "cooperative",
    "cluster_formation"
  ],
  "timestamp": "2026-01-24T00:30:00Z"
}
```

### Failed Strategy Record

```json
{
  "episode": 80,
  "population_fitness": 0.48,
  "failure_reasons": [
    "excessive_competition",
    "low_diversity",
    "cluster_isolation"
  ],
  "timestamp": "2026-01-24T00:25:00Z"
}
```

### Population Norm

```json
{
  "norm": "cooperative_teaching",
  "value": 0.75,
  "confidence": 0.82,
  "last_reinforced_episode": 150,
  "violation_count": 3
}
```

---

## Interaction Protocol

### Teach → Learn Sequence

```
1. Teacher prepares knowledge package
2. Teacher broadcasts availability
3. Learner evaluates package
4. Learner accepts/rejects
5. If accepted:
   - Integrate knowledge
   - Update beliefs
   - Record source reputation
   - Send feedback
6. Teacher updates teaching_instances
7. Both record interaction
```

### Synchronization

- All interactions logged with episode number
- Timestamped for replay capability
- Reversible for experimental variation

---

## Privacy & Reputation

### Source Anonymity

Knowledge packages preserve agent ID but:
- No personal history shared
- Only aggregated patterns transmitted
- Reputation tracked separately

### Reputation Mechanics

```
Initial Reputation = 0.5

Teaching Reputation:
  +0.05 when learner shows improvement
  -0.03 when learner fails after learning
  
Learning Reputation:
  +0.02 for successful knowledge integration
  -0.02 for poor learning outcomes
  
Decay: 0.99 × reputation per episode (slow)
```

---

## Compatibility & Versioning

### Protocol Version

- Current: 0.8.1
- Backward compatible with: 0.8.0
- Breaking changes trigger error

### Validation

All knowledge packages validated against schema:
- Required fields present
- Type checking on all fields
- Confidence values in [0,1]
- Episode numbers monotonic

---

## Usage Examples

### Teaching Example

```python
# Agent 42 teaches Agent 15
knowledge = agent42.teach_others(
    topic="strategy",
    confidence=0.8
)

# Agent 15 receives and learns
agent15.learn_from_others(knowledge)

# Outcome: Agent 15's performance may improve
# Interaction recorded for network analysis
```

### Belief Updating Example

```python
# Observation contradicts belief
observation_strength = 0.7  # High contradiction
agent.memory.beliefs["hypothesis"].update_confidence(
    evidence=observation_strength,
    is_supporting=False
)
# Result: belief confidence drops by 0.105 (0.7 × 0.15)
```

---

## Network Analysis

### Degree Centrality

Number of teaching/learning connections per agent

### Clustering Coefficient

Tendency of connected agents to form triangles (teaching triangles)

### Information Diffusion

How quickly successful strategies propagate through network

### Community Detection

Identification of stable clusters over time

---

## Experimental Variations

### Pressure Type Effects

**STABLE:**
- High within-cluster sharing
- Few cross-cluster transfers
- Roles stabilize

**VARYING:**
- Increased cross-cluster sharing
- Frequent role reassignment
- Knowledge diversity critical

**ADVERSARIAL:**
- Teaching discouraged
- Individual learning emphasized
- Cluster fragmentation likely

**COOPERATIVE:**
- Teaching promoted
- Knowledge widely shared
- Dense networks form

---

## Compliance Checking

### Valid Knowledge Package

```python
def validate_knowledge_package(pkg):
    required = ["source_agent", "topic", "confidence", "episode"]
    return all(k in pkg for k in required) and \
           0 <= pkg["confidence"] <= 1 and \
           isinstance(pkg["episode"], int)
```

---

**PROTOCOL STATUS:** CANONICAL & OPERATIONAL

For questions or extensions, refer to `docs/TRL8_SPECIFICATION.md`
