# TASK-0136 BRIEF REPORT — acquire Simple English Wikipedia dump (external-only) + pin provenance (MANIFEST.json)

Branch/HEAD (pre-commit): `test` @ `245bd34507b169fc13bb176129641382f86a1245`

## Result

- **Acquisition:** SUCCESS (external-only; dump not in git)
- **Pinned provenance:** `datasets/simplified_wiki_v0/MANIFEST.json`

## VERIFIED (L0) Dump Provenance

- dump_id: `20260201`
- dump_date_utc: `2026-02-01` (from official dump_id naming)
- filename: `simplewiki-20260201-pages-articles.xml.bz2`
- dump_url: `https://dumps.wikimedia.org/simplewiki/20260201/simplewiki-20260201-pages-articles.xml.bz2`
- local_path (external; not in repo): `D:\datasets\wikimedia\simplewiki\20260201\simplewiki-20260201-pages-articles.xml.bz2`
- size_bytes: `342917678`
- sha256: `a2af6ce4c421c400f498740be8aefe77f71d52cc97fe50ed35ba28c27a3c9da6`
- acquired_at_utc: `2026-02-08T19:25:29Z`

## Commands (Repro)

Monitoring/runbook: `reports/analysis/TASK_0136_MONITORING_COMMANDS.md`

Download (resume-safe) + log:
```powershell
$dump_id = "20260201"
$filename = "simplewiki-20260201-pages-articles.xml.bz2"
$url = "https://dumps.wikimedia.org/simplewiki/$dump_id/$filename"

$dir = "D:\datasets\wikimedia\simplewiki\$dump_id"
New-Item -ItemType Directory -Force $dir | Out-Null
$out = Join-Path $dir $filename
$log = Join-Path $dir "download.log"

curl.exe -L -C - --retry 10 --retry-delay 5 --output $out $url 2>&1 | Tee-Object -FilePath $log
```

Hash + size (L0 truth):
```powershell
Get-FileHash -Algorithm SHA256 $out
(Get-Item $out).Length
```

## What’s Next

- TASK-0137: implement `build_dataset.py` to produce deterministic JSONL + splits from the pinned dump (refusing to run unless input hash/size match `MANIFEST.json`).

