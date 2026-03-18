# TASK-0137 MONITORING COMMANDS — simplified_wiki_v0 deterministic builder (smoke + repro)

Constraints:
- No network calls.
- Outputs must be written outside the repo (do not commit JSONL/split files).
- Builder must refuse to run if input dump hash/size mismatch `datasets/simplified_wiki_v0/MANIFEST.json`.

## Terminal A (Two Smoke Runs + Repro Check)

```powershell
cd d:\projects\Bio_Digital_Core\Bio_digital_core

$m = "datasets/simplified_wiki_v0/MANIFEST.json"
$base = "D:\datasets\bdc\simplified_wiki_v0\20260201"

$r1 = Join-Path $base "smoke_run1"
$r2 = Join-Path $base "smoke_run2"

python datasets/simplified_wiki_v0/build_dataset.py --manifest $m --out_root $r1 --max_docs 1000 --progress_every_pages 2000
python datasets/simplified_wiki_v0/build_dataset.py --manifest $m --out_root $r2 --max_docs 1000 --progress_every_pages 2000

# Compare output hashes (should match run1 vs run2):
Get-Content (Join-Path $r1 "BUILD_REPORT.json") | Out-File -Encoding utf8 (Join-Path $r1 "_build_report_print.txt")
Get-Content (Join-Path $r2 "BUILD_REPORT.json") | Out-File -Encoding utf8 (Join-Path $r2 "_build_report_print.txt")

python -c @'
import json,sys,hashlib
from pathlib import Path
r1 = json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))
r2 = json.loads(Path(sys.argv[2]).read_text(encoding="utf-8"))
o1 = r1["outputs"]; o2 = r2["outputs"]
ok = (o1 == o2)
print("REPRO_OK" if ok else "REPRO_FAIL")
if not ok:
    k = sorted(set(o1) | set(o2))
    for kk in k:
        if o1.get(kk) != o2.get(kk):
            print("DIFF", kk, o1.get(kk), o2.get(kk))
sys.exit(0 if ok else 2)
'@ (Join-Path $r1 "BUILD_REPORT.json") (Join-Path $r2 "BUILD_REPORT.json")
```

## Terminal B (Progress / Artifact Monitoring)

File sizes (watch growth):
```powershell
$base = "D:\datasets\bdc\simplified_wiki_v0\20260201"
$files = @(
  "smoke_run1\docs.jsonl",
  "smoke_run1\split_train.txt",
  "smoke_run1\split_val.txt",
  "smoke_run1\split_test.txt",
  "smoke_run1\BUILD_REPORT.json"
)
while ($true) {
  foreach ($f in $files) {
    $p = Join-Path $base $f
    $i = Get-Item $p -ErrorAction SilentlyContinue
    if ($i) { "{0} {1} bytes {2:o}" -f $f, $i.Length, $i.LastWriteTimeUtc } else { "{0} (missing)" -f $f }
  }
  Start-Sleep -Seconds 10
}
```

