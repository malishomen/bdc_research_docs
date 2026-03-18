# TASK-1000 WIKI PIPELINE STATUS (L0)

## Wiki dataset source
- `datasets/simplified_wiki_v0/MANIFEST.json`
- Source: `simplewiki (Simple English Wikipedia)`
- Dump URL: `https://dumps.wikimedia.org/simplewiki/20260201/simplewiki-20260201-pages-articles.xml.bz2`
- Input SHA256 (manifest): `a2af6ce4c421c400f498740be8aefe77f71d52cc97fe50ed35ba28c27a3c9da6`

## Dataset size
- Source dump size (`MANIFEST.json`): `342,917,678 bytes`
- Derived full build `docs.jsonl` (`DERIVED_MANIFEST.json`): `1,009,721,195 bytes`
- Full build docs count (`DERIVED_MANIFEST.json`): `278,985`

## Shard format
- For `exp_0017`: no explicit pre-sharded binary format in repo contract.
- Current format is file-based:
  - `docs.jsonl`
  - `split_train.txt`
  - `split_val.txt`
  - `split_test.txt`
- HIVE task-type shards for real distributed training:
  - UNVERIFIED / not active in current production snapshot (`HELLO_MVP` observed previously).

## Tokenization method
- From `experiments/exp_0017_comprehension_v0_cloze/src/train.py` and `docs/spec/COMPREHENSION_V0_CLOZE.md`:
  - `whitespace_hash` (default)
  - `byte` (alternative)

## Vocabulary size
- `whitespace_hash` default: `8192`
- `byte` tokenizer effective vocab: `258`

## Preprocessing script path
- `datasets/simplified_wiki_v0/build_dataset.py`
- Legacy TRL-7 fetch helper:
  - `experiments/exp_0006_wiki_adaptation/fetch_wikitext.py`

## Validation split logic
- In `DERIVED_MANIFEST.json`:
  - split ratios: `train=0.90`, `val=0.05`, `test=0.05`
  - split salt: `simplified_wiki_v0_split_v1`
  - disjoint union check: `true`

## Baseline metric (if exists)
- Spec baseline modes exist:
  - `random`
  - `shuffled`
- Current numeric baseline in active runtime:
  - UNVERIFIED in this intake (no fresh exp_0017 run metrics collected in this task).

## Current training status
- Canonical snapshot evidence from recent reports indicates production HIVE queue currently uses `HELLO_MVP` task flow.
- Real distributed Wiki training (`train/eval shard` task types) is not evidenced as active in this intake.
- Status: `PARTIAL / NOT ACTIVE AS VERIFIED TRAIN SHARDS`.

## Evidence files
- `datasets/simplified_wiki_v0/MANIFEST.json`
- `datasets/simplified_wiki_v0/DERIVED_MANIFEST.json`
- `experiments/exp_0017_comprehension_v0_cloze/SPEC.md`
- `experiments/exp_0017_comprehension_v0_cloze/RUN_COMMANDS.md`
- `experiments/exp_0017_comprehension_v0_cloze/src/train.py`
