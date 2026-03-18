# BDC Designer Windows Quickstart

This guide provides one-click and low-friction launch paths for Windows users.

## Launcher Assets

- Batch launcher: `launchers/bdc_designer_launcher.bat`
- PowerShell launcher: `launchers/bdc_designer_launcher.ps1`

Both use the same validated CLI logic and output schema as `tools/bdc_designer_cli.py`.

## Option A: Double-click Batch Launcher

1. Open the repository folder in File Explorer.
2. Double-click `launchers/bdc_designer_launcher.bat`.
3. The launcher runs the default bundled input: `examples/release_examples.json`.

## Option B: PowerShell Launcher

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File launchers/bdc_designer_launcher.ps1 -Pretty
```

Custom input:

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File launchers/bdc_designer_launcher.ps1 -InputJson examples/release_examples.json -Pretty
```

Persist output:

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File launchers/bdc_designer_launcher.ps1 -InputJson examples/release_examples.json -OutJson results/tmp_windows_launcher_output.json -Pretty
```

## Verify Schema Consistency

Compare launcher output to direct CLI:

```powershell
python tools/bdc_designer_cli.py --input_json examples/release_examples.json --pretty
```

Expected top-level keys for batch mode:
- `schema_version`
- `count`
- `results`

## Troubleshooting

- If `python` is not found, install Python 3.10+ and ensure it is available in `PATH`.
- If PowerShell blocks script execution, use `-ExecutionPolicy Bypass` as shown above.

## Scope Safety

BDC Designer is a restricted architecture-prior and hybrid guidance tool.
It does not claim universal optimization.
