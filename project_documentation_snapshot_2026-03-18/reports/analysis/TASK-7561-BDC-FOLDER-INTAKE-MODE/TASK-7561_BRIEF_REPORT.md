# TASK-7561 BRIEF REPORT

## Scope
- Implement Phase A of the post-TextAI roadmap: Folder Intake Mode.
- Allow BDC Designer to ingest a client evidence folder and emit a normalized `BDC_PACKET_V2` without manual analyst assembly.

## Changes
- Added folder intake package:
  - `src/bdc_designer_v2/intake/__init__.py`
  - `src/bdc_designer_v2/intake/file_registry.py`
  - `src/bdc_designer_v2/intake/normalization_profile.py`
  - `src/bdc_designer_v2/intake/folder_loader.py`
- Extended CLI with `intake-folder` command.
- Added operator docs:
  - `docs/BDC_FOLDER_INTAKE_MODE.md`
- Added regression fixture:
  - `tests/data/textai_auto_packet_v2_1/*`
- Added phase runner and tests:
  - `scripts/analysis/run_phase47_bdc_folder_intake_mode.py`
  - `tests/test_phase47_bdc_folder_intake_mode.py`

## Verification (L0)
- Command: `python -m py_compile src/bdc_designer_v2/cli.py src/bdc_designer_v2/intake/file_registry.py src/bdc_designer_v2/intake/normalization_profile.py src/bdc_designer_v2/intake/folder_loader.py scripts/analysis/run_phase47_bdc_folder_intake_mode.py`
- Result: PASS
- Output summary: intake modules and CLI compiled cleanly.
- Command: `pytest -q tests/test_phase47_bdc_folder_intake_mode.py`
- Result: PASS
- Output summary: `3 passed`.
- Command: `python scripts/analysis/run_phase47_bdc_folder_intake_mode.py --folder_path tests/data/textai_auto_packet_v2_1 --out_root results/bdc_folder_intake`
- Result: PASS
- Output summary: `supported=true`, `validated_packet_quality_level=Q4`, `tested_variant_count=12`.

## Artifacts
- `src/bdc_designer_v2/intake/file_registry.py` — folder file discovery.
- `src/bdc_designer_v2/intake/normalization_profile.py` — folder-to-packet normalization.
- `src/bdc_designer_v2/intake/folder_loader.py` — intake orchestrator and support verdict.
- `docs/BDC_FOLDER_INTAKE_MODE.md` — intake usage contract.
- `tests/data/textai_auto_packet_v2_1/*` — self-contained first-client regression fixture.

## Risks / Limitations
- Phase A normalization is currently optimized for the `TextAI_Auto`-style packet layout.
- It is robust to extra files, but not yet generalized to arbitrary folder taxonomies.
- Evidence weighting, redesign mode, measurement-gap output, and sparse-runtime tuning remain for later phases.

## Rollback
- `git revert <TASK-7561 final commit>`
