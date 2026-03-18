# Comprehension Metric v0 — Cloze Reconstruction (simplified_wiki_v0)

## Purpose

Define a minimal, reproducible, measurable "comprehension" proxy on real data: masked-token reconstruction (cloze).

This is **not** a claim of semantic understanding. It is a deterministic metric suitable for:
- regression tracking,
- sanity baselines,
- reproducibility gates,
- CPU-authoritative PASS/FAIL decisions.

## Data Source (Pinned)

Dataset: `simplified_wiki_v0` (Simple English Wikipedia)
- Input pinned by `datasets/simplified_wiki_v0/MANIFEST.json`
- Outputs pinned by `datasets/simplified_wiki_v0/DERIVED_MANIFEST.json` (`full_build.outputs.*`)

The training harness MUST refuse to run if `docs.jsonl` sha256 does not match the derived manifest.

## Task Definition (Cloze)

Given a tokenized sequence `x[0..L-1]`, create a masked input `x'` and labels `y`:
- A subset of positions is deterministically chosen to mask (see Masking).
- `x'[i] = [MASK]` for masked positions; otherwise `x'[i] = x[i]`.
- `y[i] = x[i]` for masked positions; otherwise `y[i] = IGNORE` (`-100`).

Metric: masked-token accuracy on val/test.

## Tokenization (v0)

Allowed v0 tokenizers (must be deterministic):
- `whitespace_hash` (default): regex tokenization + stable hash to buckets.
- `byte`: UTF-8 bytes (0..255) with `[PAD]` and `[MASK]` special tokens.

Tokenizer parameters MUST be recorded in RUN_METADATA (vocab size, tokenizer name).

## Deterministic Masking (Canonical)

Mask selection is deterministic and depends only on:
- `doc_id` (string),
- `token_index` (absolute token index within the document),
- `mask_salt` (versioned constant),
- `mask_rate` and `mask_span_max`.

Rule (per-token):
- compute `h = sha256(f"{doc_id}:{token_index}:{mask_salt}")`
- map first 32 bits to `r in [0,1)`
- if `r < mask_rate` then start a mask-span of length:
  - `span = 1 + (sha256(f"{doc_id}:{token_index}:{mask_salt}:span")[0:32] mod mask_span_max)`
- spans must not overlap; masked tokens are replaced by `[MASK]`.

Pinned defaults:
- `mask_rate = 0.15`
- `mask_span_max = 3`
- `mask_token = "[MASK]"`
- `mask_salt = "comprehension_v0_cloze_mask_v1"`

## Splits

Training/val/test splits come from the dataset build:
- `split_train.txt`, `split_val.txt`, `split_test.txt` (doc_id per line)

The cloze harness must honor these splits; it must not generate its own split logic.

## Baselines / Sanity

Baselines (no learning):
- `random`: for masked positions, predict a random token (deterministic RNG seed).
- `shuffled`: for masked positions, predict a token from a deterministic per-doc permutation of the same sequence.

Sanity kill-criterion:
- If `baseline_shuffled_val_accuracy >= model_val_accuracy` => FAIL.

## Reproducibility Gates

With identical:
- git HEAD,
- seed,
- tokenizer/masking parameters,
- dataset sha256,

Two runs must match `val_accuracy` within `0.5%` absolute (or be declared FAIL).

## CPU Authoritativeness

GPU is compute-only. The PASS/FAIL decision is based on the recorded metrics and gates, not on GPU-only evidence.

