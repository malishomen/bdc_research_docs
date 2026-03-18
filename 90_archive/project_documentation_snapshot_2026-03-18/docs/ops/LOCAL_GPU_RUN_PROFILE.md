# Local GPU Run Profile (GTX 1080 Ti)

Date: 2026-03-04  
Status: ACTIVE (operations note)

## Purpose
- Define a safe default compute profile for Torch-based workloads on local PC GPU.
- Keep symbolic engines (`evolution/cloze_symbolic/*`, energy model, Phase 2/3/4 symbolic loops) CPU-only.

## Hardware/Runtime baseline
- GPU: `NVIDIA GeForce GTX 1080 Ti` (11 GB VRAM)
- CUDA runtime: `12.x`
- Torch baseline: `2.5.1+cu121`
- Safe memory headroom target: use up to ~9 GB VRAM (leave margin for OS/driver/runtime variance).

## Default device policy
- Torch scripts with GPU profile should use:
  - `--device auto` (default): picks `cuda:0` when available, otherwise CPU.
  - Optional explicit override: `--device cuda` or `--device cpu`.
- Queen/orchestrator should not execute long Torch training jobs.
  - Long Torch runs are routed to local PC GPU.

## Precision policy
- Baseline on GPU: `float32` is acceptable and default-safe.
- Mixed precision is optional via explicit flag (`--use_amp`) where supported.

### Calibration update (TASK-2103, 2026-03-04)
- Mini-calibration (`N=5`, seeds `1337..1341`) evaluated:
  - `opt_amp_bs12` (`--use_amp --batch_size 12`)
  - `opt_fp32_bs12` (`--batch_size 12`, AMP off)
  - `opt_amp_bs8` (`--use_amp --batch_size 8`)
- Fixed selection rule:
  1. Keep profiles with `stability_fail_rate <= 0.10`
  2. Select max `mean_delta` (`baseline_val_loss - optimized_val_loss`)
- Selected profile for applied rerun path: `opt_amp_bs8`
  - `--use_amp`
  - `--batch_size 8`
  - `--steps 80`
  - Keep `--strict_numeric_asserts` OFF for AMP path (debug-only flag).
- Fallback profile if instability reappears: `opt_fp32_bs12`.

## Memory policy
- For long runs, keep VRAM under soft cap:
  - `--gpu_mem_soft_limit_gb 9.0`
- This is warning/throttling guidance, not a hard crash condition.

## Eligibility matrix

GPU-eligible (Torch-based):
- `cognitive/run_trl10_gpu_optimized.py`
- `cognitive/gpu_training_engine.py` (when launched with CUDA device)
- `experiments/exp_0017_comprehension_v0_cloze/src/train.py`
- `scripts/wiki_pilot/run_once.py`

CPU-only (pure symbolic / non-Torch evolution path):
- `evolution/cloze_symbolic/*`
- `evolution/energy_model.py`
- Phase 2/3/4 symbolic engines and orchestration around them

## Backward compatibility rule
- Existing CLI behavior must stay valid.
- Only optional flags are introduced (`--device`, `--use_amp`, `--gpu_mem_soft_limit_gb`).
- No forced migration of existing run commands.
