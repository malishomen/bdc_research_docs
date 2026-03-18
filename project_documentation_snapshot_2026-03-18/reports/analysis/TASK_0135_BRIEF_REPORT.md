# TASK-0135 BRIEF REPORT — lock simplified_wiki_v0 as Simple English Wikipedia (Variant B) (provenance-first; no download)

Branch/HEAD: `test` @ `147745806104fbeadd3db92bf7e737617267631e`

## Decision

- **simplified_wiki_v0 = Simple English Wikipedia dump** (Variant B).
- All dump identifiers/URLs/filenames remain **UNVERIFIED** until TASK-0136 acquisition + sha256 pinning.

## Artifacts Added

- `datasets/simplified_wiki_v0/SPEC.md`
- `datasets/simplified_wiki_v0/INGESTION_POLICY.md`
- `datasets/simplified_wiki_v0/RUN_COMMANDS.md`

## Provenance Standard (What “Good” Looks Like)

- A local dump file exists (external, not in git).
- `datasets/simplified_wiki_v0/MANIFEST.json` pins:
  - `sha256`, `size_bytes`, `dump_id`, `dump_date_utc`, `filename`, and a `dump_url` pointer.
- Builder refuses to run if input hash/size do not match manifest.

## Next Step

- TASK-0136: acquire dump locally and create `MANIFEST.json` with verified hash/size.
- TASK-0137: implement `build_dataset.py` and produce deterministic JSONL + splits.

