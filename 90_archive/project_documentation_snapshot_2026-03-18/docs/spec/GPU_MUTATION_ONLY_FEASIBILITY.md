# GPU Mutation-Only Feasibility (Determinism + Artifact Parity)

Scope: feasibility spike for a GPU backend for the mutation-only runner semantics used by:
- `experiments/exp_0015_kc1_ttt_vnext_validation/src/runner.py` (CPU authoritative reference)

Canon constraints:
- CPU remains authoritative.
- GPU results are replicate-only until equivalence is proven (L2 contract).
- No retro changes to existing experiment semantics.

## Current CPU Semantics (What Must Not Change)

The CPU runner (exp_0015) is pure Python and uses:
- Genome representation: `List[List[int]]` with per-locus base-4 digits (0..3).
- RNG: per-seed PiStream slicing -> SHA256 -> `random.Random(stream_seed)` for each named stream.
  - For exp_0015: `INIT_PISTREAM` and `MUT_MAGNITUDE_PISTREAM` are used.
- Mutations:
  - `per_locus_flip(p)`: independent Bernoulli decisions using `rng.random() < p` per locus.
  - `k_point_mutation(k)`: positions via `rng.sample(range(L), k_eff)` and per-position new allele via `rng.randrange(4)`.
- Metrics per generation:
  - `E_genotype_bits`: Shannon entropy of genotype counts (base-2).
  - `D`: mean pairwise Hamming distance normalized by `L`.
- Gates:
  - KC1_TTT: fails if `max(D[g<=H]) < T` using the **full-precision `D`**, not the rounded CSV value.
  - KC2 thresholds (final generation only): `E < 2.5` or `D < 0.30`, using the **rounded** values written into `metrics_rows`.

Implication: even small numeric drift in `D` for the first `H` generations can flip KC1 outcomes and therefore flip `summary.csv` rates.

## What Dominates Runtime (Likely Hotspots)

Given defaults (pop=30, gen=50, L up to 256), the computational hotspot is:
- `mean_pairwise_hamming(genomes)`:
  - complexity: `O(pop^2 * L)` per generation
  - for pop=30: 435 pairs; for L=256: 111,360 locus comparisons per generation

Mutation operators are `O(pop * L)` (per-locus) or `O(pop * k)` (k-point) and are typically cheaper than pairwise Hamming.

## GPU Viability: What Can Move Without Semantic Drift

### Feasible (Low semantic risk)

1. **Accelerate D computation only (hybrid CPU+GPU)**
   - Keep all RNG + mutation + genome state updates on CPU (exactly as today).
   - Move only the pairwise Hamming aggregate to GPU.
   - Key trick for parity: compute an **integer** `sum_diff = sum_{pairs} diff_count` on GPU, then compute:
     - `D = sum_diff / (L * pairs)` on CPU
   - Because `sum_diff` is an integer and addition is exact, this avoids floating reduction-order drift and can be bitwise-stable.
   - This is a “GPU accelerator”, not a full GPU runner.

2. **Leave entropy on CPU**
   - Entropy is not the hotspot at pop=30.
   - It uses floating logs and counter iteration order; keeping it on CPU avoids additional parity risk.

### Risky / Likely Not Equivalent (High semantic risk)

1. **Port RNG and mutation decisions to GPU**
   - Current RNG is Python `random.Random` seeded from PiStream slices.
   - Torch CUDA RNG streams will not match Python’s Mersenne Twister sequences.
   - Even if both are deterministic, different RNG streams mean different mutations => non-equivalent trajectories and summary rates.

2. **Compute `D` as float reductions on GPU**
   - Even deterministic algorithms can change float rounding via parallel reduction order.
   - This is especially risky because KC1 checks `max(D)<=T` in early generations.

3. **Full “GPU-native” runner with identical artifacts**
   - Requires a GPU-side implementation of:
     - PiStream slicing, SHA256-based seeding, and Python-compatible RNG behavior, or
     - a canonical spec change allowing different RNG streams (not allowed).
   - Also requires strict artifact parity (`metrics.csv` row-by-row), which is brittle under any numeric drift.

## Determinism Plan (If Attempting Any GPU Work)

Environment (local observation):
- Torch is installed: `torch 2.5.1+cu121` and CUDA is available.

For any torch-based GPU acceleration, enforce:
- `torch.use_deterministic_algorithms(True)`
- `torch.backends.cudnn.deterministic = True`
- `torch.backends.cudnn.benchmark = False`

But: deterministic settings do not solve “different RNG stream” parity, and do not guarantee float equality to CPU.

Recommended parity strategy:
- If GPU is used, prefer integer accumulations + CPU-side final float conversion.

## Artifact Parity Targets (Minimal First)

The minimal equivalence contract from TASK-0128 compares `summary.csv` keyed by `(config_id,set)` with:
- `seeds_total`
- `kc1_fail_rate`
- `threshold_fail_rate`
- `overall_pass_rate`

For a mutation-only GPU backend to be considered equivalent under that contract:
- It must reproduce **per-seed** KC1/KC2 pass/fail classifications exactly, because rates are discrete with seeds_total=30.

This implies:
- Either the full trajectory must match (strong), or
- the gate-relevant metrics must match exactly for each seed (still hard).

## Feasibility Conclusion

Status:
- **NOT READY** for a GPU-equivalent mutation-only runner that reproduces CPU artifacts under the L2 contract.

Reasons:
- CPU semantics depend on Python `random.Random` streams derived from PiStream; GPU RNG parity is not available.
- KC1 uses full-precision `D` in early generations; even tiny numeric drift can flip outcomes.

What *is* feasible next (separately scoped):
- A **hybrid accelerator** that keeps RNG+mutation on CPU and offloads only the integer pairwise Hamming accumulation to GPU, then computes `D` on CPU.
- This can preserve semantics, but speedups are uncertain due to CPU↔GPU transfer overhead at current (small) population sizes.

## Minimal GPU Backend v0 Plan (Hybrid Accelerator)

Goal: keep CPU semantics identical, accelerate only the hotspot.

1. Add an optional code path (new runner or new module, not retrofitting old runs):
   - Represent genomes as a small `torch.int16` tensor on GPU each generation: shape `[pop, L]`.
   - Compute `sum_diff`:
     - Option A (torch ops): `(G.unsqueeze(1) != G.unsqueeze(0)).sum(dim=-1, dtype=torch.int32)` to get pairwise diff counts, then sum upper triangle.
     - Option B (custom CUDA): only if torch ops prove nondeterministic or too slow.
   - Return `sum_diff` to CPU and compute `D = sum_diff / (L * pairs)` as Python float.

2. Keep:
   - RNG streams (`seed_streams.py`) unchanged on CPU
   - mutation application unchanged on CPU
   - entropy computation unchanged on CPU

3. Measure (do not promise speedup):
   - wall time per seed/config for CPU vs hybrid
   - GPU transfer overhead share

Kill-criteria for v0:
- If any seed’s KC1/KC2 classification differs from CPU for the same input seeds/configs: stop (non-equivalent).
- If speedup < 1.2x at realistic sizes or transfer dominates: stop (not worth complexity).

