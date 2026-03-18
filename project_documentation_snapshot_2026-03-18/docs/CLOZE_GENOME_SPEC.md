# CLOZE GENOME SPEC (v0)

**Date:** 2026-02-27  
**Experiment:** exp_0400 (Phase 2)  
**Module:** `evolution/cloze_symbolic/`

## 1. Purpose

Define a minimal, interpretable genome for wiki-derived cloze evolution, separate from hidden_rule EDP1.

This spec is additive and does not modify:
- `evolution/edp1_symbolic/*`
- wiki LM training stack (`scripts/wiki_pilot/*`).

## 2. Data Contract

Source dataset:
- `D:/datasets/bdc/simplified_wiki_v0/20260201/full_build/docs.jsonl`

Subset protocol:
- Deterministic subset of `subset_size=100` docs.
- Subset seed is derived from master seed via named stream:
  - `ENV_PISTREAM = sha256("<master_seed>:ENV_PISTREAM")[:8]`
- Selection method: `random.Random(subset_seed).sample(range(N_docs), k=subset_size)`.

Cloze sample generation:
- Tokenization: deterministic regex `[A-Za-z0-9']+`, lowercased.
- Token IDs: stable FNV-like hash mod `vocab_size` (default 512).
- Masking: deterministic per token index:
  - `r = sha256(f"{doc_id}:{token_index}:{mask_salt}")`
  - masked if `r < mask_rate` (`mask_rate=0.15`, `mask_salt="comprehension_v0_cloze_mask_v1"`).
- Valid samples require both neighbors (`pos in [1..len-2]`).
- Each sample stores:
  - `prev_token_id`
  - `next_token_id`
  - `position_norm`
  - `target_token_id`

## 3. Genome Structure

`ClozeGenome` parameters:
- `w_prev_match` (float)
- `w_next_match` (float)
- `w_position` (float)
- `w_frequency_prior` (float)
- `token_biases` (tuple[float], length = `top_k_tokens`)

Configurable dimensionality:
- `top_k_tokens` is runtime-configurable (CLI) and controls genome size:
  - `top_k=4` -> `K=8` parameters (`4 + 4`)
  - `top_k=16` -> `K=20` parameters (`4 + 16`)
- Backward-compatible default: `top_k_tokens=16`.

Interpretation:
- Prediction is argmax over top-K frequent candidate tokens in the subset.
- Candidate score:
  - `token_bias[k]`
  - `+ w_prev_match * I(prev_token == candidate_k)`
  - `+ w_next_match * I(next_token == candidate_k)`
  - `+ w_position * position_norm`
  - `+ w_frequency_prior * candidate_freq_norm[k]`

## 4. Parameter Ranges

Initialization:
- Scalars in `[-1.0, 1.0]`
- Token biases in `[-1.0, 1.0]`

Mutation:
- Gaussian perturbation `N(0, sigma)` (`sigma=0.20` default)
- Clipped to `[-5.0, 5.0]`

## 5. Complexity & Fitness

Canonical regime from ADR-0005:
- **Regime B** (fixed for exp_0400)

Complexity:
- `complexity = mean(abs(parameters))`
- `K = 4 + top_k_tokens`

Penalty and fitness:
- `penalty = lambda * complexity` (default `lambda=0.01`)
- `fitness_mode=hard` (default, backward compatible): `fitness = accuracy - penalty`
- `fitness_mode=soft`: 
  - compute candidate scores for each sample,
  - compute stable softmax probabilities (`exp(score - max_score)`),
  - `soft_accuracy = mean(P(target_token))`,
  - `fitness = soft_accuracy - penalty`.

Recorded decomposition per generation:
- `max/mean_accuracy`
- `max/mean_soft_accuracy`
- `max/mean_complexity`
- `max/mean_penalty`
- `max/mean_fitness`

## 6. Baselines

Required baselines on same subset and masking:
1. `random` predictor (deterministic `QUERY_PISTREAM` seed)
2. `frequency` predictor (most frequent candidate token)
3. `constant` predictor (fixed token id = 0)
4. `bigram` predictor (argmax target count for given previous token, fallback to frequency)

Representational capacity control:
- `ClozeGenome.frequency_oracle(top_k_tokens, strength=10.0)` must reproduce the frequency baseline by construction:
  - all context weights = `0`,
  - `w_frequency_prior` >> `0`,
  - all token biases = `0`.
- This oracle is evaluated directly (without evolution) in TASK-1601 diagnostics.

## 7. Reproducibility Fields

Every `summary.json` must include:
- `seed`, `population`, `generations`
- `subset_size`, `subset_doc_count`, `subset_doc_ids_preview`
- `stream_seeds` (`ENV/QUERY/MUT_DECISION/MUT_MAGNITUDE`)
- `complexity_regime="B"`, `complexity_lambda`
- baseline accuracies and final metrics.

## 8. ClozeGenome v1 Nucleotide Architecture (R1)

Biological and mathematical basis:
- DNA 4-nucleotide framing (`A/T/G/C`) with backbone integration.
- Quaternary mapping: `A -> T (Truth)`, `T -> MY`, `G -> MN`, `Backbone -> conflict_flag`.
- Golden ratio engineering:
  - `phi = 1.618...`
  - `phi^-1 = 0.618...`
  - DNA geometry analogy: `34/21 ~ phi`.

### 8.1 Genome components

`ClozeGenomeV1`:
- `Acid_A` (frequency channel):
  - `w_frequency_prior`
  - `token_biases[top_k]`
- `Acid_T` (forward context channel):
  - `prev_context_table[8]` (Fibonacci-sized hash table)
- `Acid_G` (reverse context channel):
  - `next_context_table[5]` (Fibonacci-sized hash table)
- `Backbone`:
  - no learnable params, additive integration of acid channels.

Removed from v0:
- `w_position` (dead parameter)
- `w_prev_match`, `w_next_match` (replaced by hashed context interactions)

### 8.2 Scoring

For candidate `i`:

```text
acid_A = token_biases[i] + w_frequency_prior * freq_norm[i]
acid_T = prev_context_table[fib_hash(prev_token_id, candidate_id_i, 8)]
acid_G = next_context_table[fib_hash(next_token_id, candidate_id_i, 5)]
score_i = acid_A + acid_T + acid_G
```

Hash function:
- default: Fibonacci hash (Knuth constant)
- optional diagnostic mode: simple XOR hash

### 8.3 Parameter budget

- `top_k=5`: `1 + 5 + 8 + 5 = 19`
- `top_k=8`: `1 + 8 + 8 + 5 = 22`

### 8.4 Complexity / fitness / conflict

- Complexity stays Regime B:
  - `complexity = mean(abs(all_params))`
- Fitness modes:
  - `hard`: `fitness = binary_accuracy - penalty`
  - `soft`: `fitness = soft_accuracy - penalty`
- Conflict flag:
  - computed from variance of acid contributions across candidates
  - `conflict_flag=1` if variance exceeds threshold

### 8.5 Selection and mutation

Golden section selection defaults for v1:
- `elite_frac = 1 - phi^-1 ~= 0.382`
- `survivor_frac = phi^-1 ~= 0.618`

phi-scaled mutation sigmas (`sigma_base`):
- `Acid_A`: `sigma_base * phi^-2 ~= 0.382 * sigma_base` (most conserved)
- `Acid_T`: `sigma_base * phi^-1 ~= 0.618 * sigma_base`
- `Acid_G`: `sigma_base * 1.0` (most exploratory)

### 8.6 Apoptosis self-repair (H3 operational hook)

Backbone health monitor uses acid discrimination:
- `acid_discrimination(acid) = mean(max_score - min_score)` across samples
- dead acid if discrimination `< APOPTOSIS_THRESHOLD`
- if dead for `APOPTOSIS_PATIENCE` consecutive generations:
  - regenerate that acid in non-elite offspring only

Defaults:
- `APOPTOSIS_THRESHOLD = 0.01`
- `APOPTOSIS_PATIENCE = 5`

### 8.7 Bigram oracle method

`ClozeGenomeV1.bigram_oracle(...)`:
- construct `prev_context_table` from empirical `bigram_counter` via bucketed averages
- normalize to `[-5, 5]`
- used for representational check:
  - PASS target `abs(oracle_acc - bigram_baseline) < 0.02`
- fallback escalation: `prev_hash_size=13` if delta remains large

## 9. ClozeGenome v2 Sensor Architecture (R1)

Design goal:
- remove hash bottleneck from v1 by switching from bucketed context tables to pre-computed context sensors.

### 9.1 Sensor formulation

Candidate score for token `i`:

```text
score[i] =
  token_biases[i]
  + w_frequency_prior * freq_norm[i]
  + w_bigram * bigram_score[i]
  + w_reverse_bigram * reverse_bigram_score[i]
```

Where:
- `bigram_score[i] = count(prev_token, candidate_i) / (sum_j count(prev_token, candidate_j) + 1)`
- `reverse_bigram_score[i] = count(candidate_i, next_token) / (sum_j count(candidate_j, next_token) + 1)`

Feature sensors are derived from:
- `ClozeTaskData.bigram_counter`
- `ClozeTaskData.reverse_bigram_counter`

### 9.2 Genome parameters

`ClozeGenomeV2`:
- `w_frequency_prior`
- `token_biases[top_k]`
- `w_bigram`
- `w_reverse_bigram`

Parameter budget:
- `top_k=5`: `5 + 3 = 8`
- `top_k=8`: `8 + 3 = 11`

Complexity:
- same canonical Regime B: `mean(abs(all_params))`

### 9.3 Oracles

Bigram oracle:
- `w_bigram=10.0`, all other params `0.0`
- must reproduce bigram baseline exactly (delta `0.0` by construction).

Frequency oracle:
- `w_frequency_prior=10.0`, all other params `0.0`
- must reproduce frequency baseline exactly (delta `0.0` by construction).

### 9.4 Acid mapping and mutation

Acid mapping:
- `Acid_A` -> frequency sensor (`token_biases + w_frequency_prior`)
- `Acid_T` -> bigram sensor (`w_bigram`)
- `Acid_G` -> reverse-bigram sensor (`w_reverse_bigram`)

phi-scaled mutation (`sigma_base`):
- `Acid_A`: `sigma_base * phi^-2`
- `Acid_T`: `sigma_base * phi^-1`
- `Acid_G`: `sigma_base * 1.0`

Backbone conflict flag:
- variance across acid contributions per candidate, thresholded to get `conflict_flag`.

## 10. ClozeGenome v2 Extended Sensors (TASK-1606)

Purpose:
- diagnose whether second-order context sensors raise the v2 ceiling after TASK-1605 gate failure.

Added optional sensors (enabled only with `--use_skip_bigram`):
- `skip_bigram`: `P(candidate | token_{t-2})` proxy
- `rev_skip_bigram`: `P(token_{t+2} | candidate)` proxy

Scoring extension in 5-sensor mode:

```text
score[i] =
  bias[i]
  + w_freq * freq_norm[i]
  + w_bigram * bigram_score[i]
  + w_reverse * reverse_bigram_score[i]
  + w_skip_bigram * skip_bigram_score[i]
  + w_rev_skip_bigram * rev_skip_bigram_score[i]
```

Acid mapping:
- `Acid_A`: frequency channel
- `Acid_T`: bigram + skip_bigram channels
- `Acid_G`: reverse_bigram + rev_skip_bigram channels

Mutation rates:
- `w_skip_bigram` uses `sigma_t` (same as `w_bigram`)
- `w_rev_skip_bigram` uses `sigma_g` (same as `w_reverse_bigram`)

Backward compatibility invariant:
- default mode (`--use_skip_bigram` not set) must be bit-identical to 3-sensor v2:
  - skip weights remain exactly `0.0`
  - skip features are not precomputed/passed
  - complexity denominator and parameter count are unchanged

Sparsity note:
- skip-bigram counts can be sparse on `subset_size=100`; a negative diagnostic outcome only proves non-informativeness at current scale.

## 11. Phase 3 Energy Model (TASK-1700)

Objective:
- switch from fitness-penalty selection to resource-bounded selection.

Enabled by run flag:
- `--energy_model` (default: off; backward-compatible behavior when omitted).

Mechanics:
- each individual gets energy budget `E_0` per generation.
- complexity induces computation cost:
  - linear: `alpha * complexity`
  - sublinear: `alpha * sqrt(complexity)`
  - step: `alpha * ceil(complexity / threshold)`
- reproduction pool is restricted to lineages with positive remaining energy.
- fitness under energy mode:
  - `fitness = task_accuracy` (hard) or `soft_accuracy` (soft),
  - complexity no longer subtracted from fitness.

Diagnostics added for Phase 3:
- `energy_alive_ratio`
- `final_complexity_variance`
- `high_complexity_alive_ratio`
- FFT post-processing (`spectral_entropy`, `dominant_frequency`, `stagnation_flag`) via `spectral_diagnostics.py`.

phi instrumentation:
- P1 metric logged (diagnostic only):
  - `phi_balance = |w_bigram| / (|w_freq| + |w_bigram| + eps)`
  - `phi_deviation = |phi_balance - phi^-1|`
- P7 prepared behind `--phi_rebalance` flag (default off).
