# TASK-LOCAL-GPU-PREP BRIEF REPORT

## Scope
- Prepare a GPU-aware run profile for Torch-based workloads on local PC (GTX 1080 Ti, CUDA 12.x).
- Preserve CPU-only behavior for symbolic EDP1 evolution path.

## Changes
- Updated GPU-capable runners with optional device/profile flags:
  - `scripts/wiki_pilot/run_once.py`
    - added optional flags: `--device`, `--use_amp`, `--gpu_mem_soft_limit_gb`
    - added startup device print: `MODEL_DEVICE ...`
    - added VRAM soft-limit telemetry warning.
  - `cognitive/run_trl10_gpu_optimized.py`
    - added optional flags: `--device`, `--use_amp`, `--gpu-mem-soft-limit-gb`
    - added device resolution (`auto|cpu|cuda`) with explicit error on invalid CUDA request
    - added GPUController soft memory cap logic (~9 GB default)
    - added startup device print via logger (`MODEL_DEVICE ...`).
- Added ops documentation:
  - `docs/ops/LOCAL_GPU_RUN_PROFILE.md`
    - GPU-eligible vs CPU-only matrix
    - Queen routing rule (no long Torch training jobs on Queen)
    - compatibility constraints.

## Verification (L0)
- Command: `python -c "import torch; print(torch.__version__, torch.cuda.is_available(), torch.cuda.get_device_name(0) if torch.cuda.is_available() else 'N/A')"`
- Result: PASS (`2.5.1+cu121 True NVIDIA GeForce GTX 1080 Ti`)

- Command: `python scripts/wiki_pilot/run_once.py --dry_run --steps 5 --batch_size 8 --seq_len 128 --d_model 128 --nhead 4 --num_layers 2 --dim_ff 256 --device cuda --out_dir results/.tmp_task_local_gpu_prep/wiki_pilot_gpu_smoke`
- Result: PASS
- Output summary: startup line contains `MODEL_DEVICE cuda:0 amp_enabled=False`.

- Command: GPU utilization smoke with polling:
  - run `scripts/wiki_pilot/run_once.py` (`--dry_run --steps 30 --device cuda`) while sampling `nvidia-smi`.
- Result: PASS
- Output summary:
  - `GPU_POLL_MAX util=66 mem_mb=3143`
  - no CUDA OOM; memory well below ~9 GB soft cap.

- Command: `python cognitive/run_trl10_gpu_optimized.py --hours 0.002 --agents 8 --batch-size 8 --device cuda --dataset datasets/wiki_prepared.jsonl --results-dir results/.tmp_task_local_gpu_prep/trl10_gpu_profile_smoke --log-file results/.tmp_task_local_gpu_prep/trl10_gpu_profile_smoke/train.log`
- Result: PASS
- Output summary: logger prints `MODEL_DEVICE cuda:0 amp_enabled=False`, short run completed with final checkpoint.

- Command: `python -m evolution.cloze_symbolic.run_generations --dry_run --genome_version v2 --use_skip_bigram --seed 1337 --out_dir results/.tmp_task_local_gpu_prep/edp1_cpu_check`
- Result: PASS
- Output summary: run completed; `summary.json` has no GPU device field; symbolic path unchanged.

- Command: `python -m py_compile scripts/wiki_pilot/run_once.py cognitive/run_trl10_gpu_optimized.py`
- Result: PASS

## Artifacts
- `docs/ops/LOCAL_GPU_RUN_PROFILE.md` — operations policy for local GPU profile and routing.
- `scripts/wiki_pilot/run_once.py` — optional GPU profile flags + telemetry.
- `cognitive/run_trl10_gpu_optimized.py` — optional GPU profile flags + VRAM soft-limit control.
- `reports/analysis/TASK-LOCAL-GPU-PREP/TASK-LOCAL-GPU-PREP_BRIEF_REPORT.md` — this report.

## Risks / Limitations
- `--gpu_mem_soft_limit_gb` is soft control/telemetry, not a hard allocation guard.
- Mixed precision is optional; default remains safe float32 path for compatibility.
- No changes were made to symbolic EDP1 engines; they remain CPU-only.

## Rollback
- `git revert <commit-hash-containing-task-local-gpu-prep>`
