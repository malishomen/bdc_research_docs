# TASK-0158 BRIEF REPORT — graceful stop `task0157b_live_unbounded` + L0 harvest bundle (ZIP)

Branch: `main`

## Identity (L0)

- repo_root: `D:\projects\Bio_Digital_Core\Bio_digital_core`
- run_tag: `task0157b_live_unbounded`
- manifest (launcher): `logs/exp_0017_comprehension_v0_cloze/_launchers/RUN_LAUNCH_MANIFEST_2026_02_10T00_39_25Z_task0157b_live_unbounded.json`
- run_dir: `logs/exp_0017_comprehension_v0_cloze/run_20260210T003928Z_9216ceb_task0157b_live_unbounded`
- snapshot_root: `ui/pacman_viz/_snapshots/task0157b_live_unbounded`
- dataset_root: `D:\datasets\bdc\simplified_wiki_v0\20260201\full_build`

## Stop (Graceful) Evidence (L0)

From `logs/exp_0017_comprehension_v0_cloze/run_20260210T003928Z_9216ceb_task0157b_live_unbounded/STOP_REQUEST.json`:
- mode: `graceful`
- requested_by: `viewer`
- ts_utc: `2026-02-10T06:47:36Z`

Terminal state:
- `RUN_STATUS.json.state=COMPLETED`, `step=287000`, `ts_utc=2026-02-10T06:48:30Z`
- `metrics_by_step.jsonl` ends with `event=RUN_END` (`state=COMPLETED`, `reason=MAX_STEPS_REACHED`, `step=287000`, `ts_utc=2026-02-10T06:48:30Z`)

## Terminal Metrics (L0)

From `metrics.json`:
- final_step: `287000`
- val.masked_accuracy: `0.5729703295869413` (k=`67956`, n=`118603`), val.masked_loss=`2.7413528035963797`
- test.masked_accuracy: `0.5514775977121068` (k=`68263`, n=`123782`), test.masked_loss=`2.8949505100748567`
- baseline_shuffled_val.masked_accuracy: `0.027646855475831133`
- verdict_kc_sanity: `PASS`

## Post-Stop Gates (L0)

Policy sidecar finalized (post-stop):
- tool: `python tools/analysis/exp0017_write_policy_sidecar.py --run_dir <RUN_DIR> --dataset_root <DATASET_ROOT> --require_integrity --require_sanity`
- result: `exit_code=0`, `quaternary_state=YES`, `verdict=PASS`, `ts_utc=2026-02-10T06:50:40Z`

Artifact integrity:
- tool: `python tools/analysis/exp0017_artifact_integrity_check.py --run_dir <RUN_DIR> --hash`
- result: `INTEGRITY_EXIT_CODE=0` (`ok=true`)

Progress policy eval:
- tool: `python tools/analysis/exp0017_progress_policy_eval.py --runs_root logs/exp_0017_comprehension_v0_cloze --run_tags task0157b_live_unbounded --require_integrity --dataset_root <DATASET_ROOT> --require_sanity`
- result: `POLICY_EVAL_EXIT_CODE=0` (`verdict=PASS`)

## Snapshot Evidence (Viz) (L0)

From `ui/pacman_viz/_snapshots/task0157b_live_unbounded/` at harvest time:
- snapshot_count (strict timestamped `snapshot_YYYYmmddTHHMMSSZ.json`): `370`
- `LATEST.json`: `ts_utc=2026-02-10T06:47:29Z`, `step=287000`, `data_status=complete`
- Note (L0): `LATEST.json.quat_state` at that moment was `MAYBE_NO` while `policy_eval.json` post-stop is `YES` (sidecar updated after the last snapshot tick). Bundle includes an additional `normalized_snapshot_post_stop.json` derived read-only from run_dir artifacts.

## L0 Bundle ZIP (External-Only)

ZIP (not committed; external-only):
- path: `D:\datasets\bdc\bundles\TASK_0158_TASK0157B_ARCHIVE.zip`
- size_bytes: `113086`
- sha256: `5cf9cbbf5b051ca433c9fa1a5bf6ab62bfb54c8759be527fd5440475187047ab`

Bundle contents (high level):
- `run_dir/`: crash-safe artifacts + `STOP_REQUEST.json` + `policy_eval.json`
- `launcher/`: manifest + port selection + launcher logs + generated policy loop script
- `snapshots/`: `LATEST.json` + `SNAPSHOT_DAEMON_STATUS.json` + last 60 timestamped snapshots + `normalized_snapshot_post_stop.json`
- `README_L0.md` inside ZIP: sha256 list for every staged file.

## Explicitly Not Committed

- No files under `logs/**` committed.
- No files under `ui/pacman_viz/_snapshots/**` committed.
- No external dataset files committed.
- ZIP bundle kept external-only (path+sha256 pinned above).

