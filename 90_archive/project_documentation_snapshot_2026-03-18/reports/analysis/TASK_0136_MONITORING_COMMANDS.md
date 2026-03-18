# TASK-0136 MONITORING COMMANDS — simplewiki dump acquisition (external-only)

Constraints:
- Downloaded dump MUST be stored outside the repo and must never be committed.
- Use resume-safe download.

## Terminal A (Download + Pin)

```powershell
cd d:\projects\Bio_Digital_Core\Bio_digital_core

# Official dump pointer (verify in browser if needed):
$dump_id = "20260201"
$filename = "simplewiki-20260201-pages-articles.xml.bz2"
$url = "https://dumps.wikimedia.org/simplewiki/$dump_id/$filename"

# External storage (outside repo):
$dir = "D:\\datasets\\wikimedia\\simplewiki\\$dump_id"
New-Item -ItemType Directory -Force $dir | Out-Null
$out = Join-Path $dir $filename
$log = Join-Path $dir "download.log"

# Resume-safe download:
curl.exe -L -C - --retry 10 --retry-delay 5 --output $out $url 2>&1 | Tee-Object -FilePath $log

# Hash + size (L0 truth):
Get-FileHash -Algorithm SHA256 $out
(Get-Item $out).Length
```

## Terminal B (Progress / Evidence)

File growth:
```powershell
$out = "D:\\datasets\\wikimedia\\simplewiki\\20260201\\simplewiki-20260201-pages-articles.xml.bz2"
while ($true) {
  $i = Get-Item $out -ErrorAction SilentlyContinue
  if ($i) { "{0} bytes @ {1:o}" -f $i.Length, $i.LastWriteTimeUtc } else { "not found" }
  Start-Sleep -Seconds 10
}
```

Tail download log:
```powershell
Get-Content "D:\\datasets\\wikimedia\\simplewiki\\20260201\\download.log" -Tail 50
```

