# TASK-1603 Addendum Spec

Date: 2026-02-27
Status: Draft-ready addendum for execution
Task: `TASK-1603` (Phase 2 continuation)

## Scope of this addendum

This addendum extends TASK-1603 with an explicit architecture update centered on:
- Backbone integration and health monitoring,
- acid-level discrimination tracking,
- apoptosis-triggered regeneration as first operational H3 self-repair mechanism.

## 1) Architecture Update

### Backbone

- Role:
  - Integration + Health Monitor + Apoptosis Controller
  - Quaternary relation: `conflict_flag` + H3 self-repair signal
- Parameters: `0` (controller logic only)
- Functions:
  1. Sum acid scores (integration)
  2. Compute `conflict_flag = variance(acid_contributions) > threshold`
  3. Compute `acid_discrimination` per acid and genome (health monitor)
  4. Trigger apoptosis: if acid is dead for `K` generations -> reinitialize that acid
- Constants:
  - `APOPTOSIS_THRESHOLD = 0.01`
  - `APOPTOSIS_PATIENCE = 5` generations
  - `APOPTOSIS_SCOPE = non-elite individuals only`
- DNA analog:
  - Apoptosis signaling pathway (`p53`, caspases) for programmed death/regeneration under detected damage

## 2) New Step 2b

Add `fibonacci.py` utility with acid-discrimination function:

```python
def acid_discrimination(genome_v1, samples, candidate_ids) -> dict[str, float]:
    ...
```

Definition:
- For each context acid (`T`, `G`):
  - discrimination = mean(`max_score - min_score`) across samples
- Output:
  - `{"T": float, "G": float}`
  - `0` means dead, `>0` means alive

Also add:
- `acid_a_discrimination`: check if all `token_biases ~ 0`

## 3) New Step 4b (mutate.py)

Extend mutation with apoptosis path:

```python
def mutate_genome_v1(parent, rng, sigma_base, acid_health=None):
    ...
```

Rules:
- If `acid_health` provided and acid is dead:
  - apoptosis regeneration for that acid via `rng.uniform(-1, 1)`
- If multiple acids are dead:
  - regenerate only the weakest one per mutation
- If no dead acid:
  - normal phi-scaled Gaussian mutation
- Return:
  - `(new_genome, apoptosis_event: bool)`

## 4) New Step 5b (select.py)

- `next_population_v1` must receive:
  - `acid_health_map: dict[int, dict[str, float]]`
- For each offspring:
  - pass parent acid-health into mutation
- Efficiency contract:
  - acid health computed in evaluation phase, not in mutate phase

## 5) New Step 6b (run_generations.py)

Per-generation acid-health tracking:
- Compute `acid_discrimination` for all individuals after evaluation
- Log:
  - `mean_acid_T_discrimination`
  - `mean_acid_G_discrimination`
- Track dead streaks:
  - `acid_T_dead_streak`
  - `acid_G_dead_streak`
- When streak >= `APOPTOSIS_PATIENCE`:
  - set acid-health mutation flags
- Log per generation:
  - `apoptosis_events_count`
- Persist acid discrimination in `metrics.csv`

## 6) Updated metrics.csv columns

Required columns:
- `generation`
- `complexity_regime`
- `mean_accuracy`, `max_accuracy`
- `mean_soft_accuracy`, `max_soft_accuracy`
- `mean_complexity`, `max_complexity`
- `mean_penalty`, `max_penalty`
- `mean_fitness`, `max_fitness`
- `functional_diversity`
- `conflict_flag_rate`
- `acid_T_discrimination`, `acid_G_discrimination`
- `apoptosis_events`

## 7) Additional verification

1. Apoptosis smoke:
   - Construct genome with dead `Acid_T` (e.g. all `prev_context_table=0.0`)
   - Run ~10 generations
   - Verify apoptosis triggers and `Acid_T` gets reinitialized
2. Preserve healthy acids:
   - After `Acid_T` apoptosis, `Acid_A` and `Acid_G` params remain unchanged
3. Activation evidence:
   - `apoptosis_events > 0` in at least one sweep generation

## 8) Additional success criteria

1. `apoptosis_events > 0` in sweep (mechanism activates when needed)
2. Post-apoptosis discrimination increases for regenerated acid

## 9) H3 connection (explicit)

Acid apoptosis is treated as first operational H3 implementation:
- system detects damaged components,
- regenerates only damaged parts,
- preserves accumulated information in healthy acids.

Biological analog:
- DNA repair pathways (`base excision repair`, `mismatch repair`) + programmed damage handling.

