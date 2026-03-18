# TASK-0134 SIMPLIFIED WIKI SOURCE REPORT (L0) — local discovery

Goal: record **facts only** about where a “simplified wiki” dataset/source lives (local path/archival/script/source pointer), without making new data acquisition decisions.

## Result

- **Simplified wiki:** **NOT FOUND LOCALLY (VERIFIED)**
  - Targeted search across `datasets/`, `backup/`, `results/`, `experiments/`, `tools/`, `docs/` for filenames containing `simplified`, `simplewiki`, `simple wiki`, `enwiki`, `dump`, `corpus`, `wikipedia`, `wikidata` returned **0 file hits** specifically indicating “simplified wiki”.

## Related Local Wiki Artifacts (VERIFIED)

These are present locally but are **not** “simplified wiki”:

1. `datasets/wiki_prepared.jsonl`
   - size_bytes: `13609807`
   - sha256: `b994f01862daf06af5f348eb84e9141fdbe461ba2eeee168720b75d778abf8ed`
   - notes: referenced by TRL-10 wikidata/WikiText-2 pipelines; content appears to be a prepared wiki-style dataset (not specifically “simplified wiki”).

2. Code references (not data sources by themselves):
   - `cognitive/run_trl10_wikidata.py` (wikidata/wikipedia processing logic)
   - `experiments/exp_0006_wiki_adaptation/` (wiki adaptation experiment scaffold)

## Mentions Of “Full Wikipedia Corpus” (UNVERIFIED AS LOCAL FILES)

Repository documents mention “full Wikipedia corpus training / dump”, but **no local dump file** or explicit simplified-wiki corpus path was found during this L0 discovery step.

Examples of mentions:
- `EXECUTION_SUMMARY_TRL10_1.md` (describes full Wikipedia corpus run)
- `scripts/trl10_1_post_completion.sh` (references tagging for “full Wikipedia corpus”)
- `WEEKLY_STATUS.md` (mentions extended Wikipedia corpus training)

Status: **UNVERIFIED** because these are text mentions without a verified local corpus file path in the repo tree.

## Next Steps (Decision Required)

If “simplified wiki” is required for the next phase, one of:

1. Provide a **local path** to the dataset/archive (preferred for provenance).
2. Choose a **public source** and define ingestion policy (separate decision; not part of this report).

