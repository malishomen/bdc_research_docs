# TASK-0147 BRIEF REPORT — L0 one-pager fix + Pac-Man visualization (L0-first) plan+scaffold

Branch: `test`

## Part A — L0 One-Pager Minimal Fix

File:
- Updated: `reports/analysis/TASK_0145_TASK0144_L0_ONE_PAGER.md`

Change (minimal; L0-only):
- Added an explicit proof snippet pinning two artifact-derived values:
  - `RUN_METADATA.json.git_head = 9708fecb84eccc9b2418a1e26820945bbc2a0cc5`
  - `metrics.json.final_step = 91001`

Commit:
- `TASK-0147(A): L0 one-pager fix (git_head_run + final_step)` @ `6a812da22c00e88002599e8976308e4101dd393e`

## Part B — Pac-Man Visualization Plan + Scaffold (Read-Only)

Authoritative UX spec:
- `docs/EXPERIMENT_VISUALIZATION_PACMAN.md`

Plan (implementation-ready; canon-safe; no training coupling):
- Updated: `docs/spec/PACMAN_VISUALIZATION_IMPLEMENTATION_PLAN.md`

Scaffold (new; file-based; offline by default):
- `ui/pacman_viz/README.md`
- `ui/pacman_viz/schema/run_snapshot.schema.json`
- `ui/pacman_viz/src/normalize_run_snapshot.py`
- `ui/pacman_viz/src/viewer.html`

Key guarantees (canon):
- Visualization is **read-only** and **file-based**; runs as a separate process.
- No synthetic/faked visuals: if a required artifact is missing/stale, the UI must show explicit `NO DATA / INCOMPLETE` (no interpolation).
- Quaternary mapping is viewer-only metadata and must not influence experiment PASS/FAIL.

## Demo (Real Run Artifacts; No Network)

Example run_dir (TASK-0144; gitignored logs):
- `logs/exp_0017_comprehension_v0_cloze/run_20260209T075959Z_9708fec_task0144_quality_2h_io`

Normalize a snapshot (command):
```powershell
cd D:\projects\Bio_Digital_Core\Bio_digital_core
$run = "logs/exp_0017_comprehension_v0_cloze/run_20260209T075959Z_9708fec_task0144_quality_2h_io"
$out = "ui/pacman_viz/_task0147_demo_snapshot.json"
python ui/pacman_viz/src/normalize_run_snapshot.py --run_dir $run --out $out
Get-FileHash -Algorithm SHA256 $out
python -c "import json;from pathlib import Path; j=json.loads(Path(r'ui/pacman_viz/_task0147_demo_snapshot.json').read_text('utf-8')); print('git_head_run', j['git_head_run']); print('step', j['step']); print('quat_state', j['quat_state']); print('data_status', j['data_status'])"
```

Observed (L0):
- Snapshot sha256: `b8402e79f9e9254ed8050b49b41eeeebc7912bdf75de2284eb306a50b8e2b3f2`
- `git_head_run=9708fecb84eccc9b2418a1e26820945bbc2a0cc5`
- `step=91001`
- `data_status=complete`
- `quat_state=MAYBE_YES` (policy not provided; labeled `unknown_policy` by default)

Viewer (offline):
- Open `ui/pacman_viz/src/viewer.html`
- Click "Load snapshot JSON" and select `ui/pacman_viz/_task0147_demo_snapshot.json`

## Verification

- `pytest -q` PASS (includes deterministic snapshot test on a synthetic fixture under `tests/data/pacman_viz/`).

## Explicitly Not Committed

- No files under `logs/**` were committed.
- No external dataset files were committed.
- Demo snapshot JSON is generated locally and should remain untracked (delete after inspection).

