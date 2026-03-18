# TASK-0138 MONITORING COMMANDS — simplified_wiki_v0 full build (external outputs)

Constraints:
- No network calls.
- Inputs must pass refuse-to-run verification against `datasets/simplified_wiki_v0/MANIFEST.json`.
- Outputs must be written outside the repo (do not commit JSONL/split files).

## Terminal A (Full Build + Log)

```powershell
cd d:\projects\Bio_Digital_Core\Bio_digital_core

$m = "datasets/simplified_wiki_v0/MANIFEST.json"
$out = "D:\datasets\bdc\simplified_wiki_v0\20260201\full_build"
New-Item -ItemType Directory -Force $out | Out-Null

# Full build (no --max_docs). Capture stdout/stderr to an external log for monitoring.
python datasets/simplified_wiki_v0/build_dataset.py --manifest $m --out_root $out --progress_every_pages 20000 2>&1 | Tee-Object -FilePath (Join-Path $out "build_full.log")
```

## Terminal B (Progress / Sizes)

Tail the build log:
```powershell
$out = "D:\datasets\bdc\simplified_wiki_v0\20260201\full_build"
Get-Content (Join-Path $out "build_full.log") -Tail 80 -Wait
```

Watch output file growth:
```powershell
$out = "D:\datasets\bdc\simplified_wiki_v0\20260201\full_build"
$files = @("docs.jsonl","split_train.txt","split_val.txt","split_test.txt","BUILD_REPORT.json")
while ($true) {
  foreach ($f in $files) {
    $p = Join-Path $out $f
    $i = Get-Item $p -ErrorAction SilentlyContinue
    if ($i) { "{0} bytes {1:o} {2}" -f $i.Length, $i.LastWriteTimeUtc, $f } else { "missing {0}" -f $f }
  }
  Start-Sleep -Seconds 15
}
```

## Post-Build Integrity Checks

Split coverage/disjointness:
```powershell
$out = "D:\datasets\bdc\simplified_wiki_v0\20260201\full_build"
python -c @'
from pathlib import Path
import json,sys
root = Path(sys.argv[1])
j = json.loads((root/"BUILD_REPORT.json").read_text(encoding="utf-8"))
n = j["stats"]["docs_written"]
tr = set((root/"split_train.txt").read_text(encoding="utf-8").splitlines())
va = set((root/"split_val.txt").read_text(encoding="utf-8").splitlines())
te = set((root/"split_test.txt").read_text(encoding="utf-8").splitlines())
assert not (tr & va), "train∩val non-empty"
assert not (tr & te), "train∩test non-empty"
assert not (va & te), "val∩test non-empty"
u = tr | va | te
assert len(u) == n, f"split union {len(u)} != docs_written {n}"
print("SPLITS_OK", "docs_written", n, "train", len(tr), "val", len(va), "test", len(te))
'@ $out
```

Output sha256 (already recorded inside `BUILD_REPORT.json.outputs`, but can be recomputed):
```powershell
$out = "D:\datasets\bdc\simplified_wiki_v0\20260201\full_build"
Get-FileHash -Algorithm SHA256 (Join-Path $out "docs.jsonl")
Get-FileHash -Algorithm SHA256 (Join-Path $out "split_train.txt")
Get-FileHash -Algorithm SHA256 (Join-Path $out "split_val.txt")
Get-FileHash -Algorithm SHA256 (Join-Path $out "split_test.txt")
```

