# BDC Folder Intake Mode

## Purpose
Load a real client evidence folder and emit a normalized `BDC_PACKET_V2` without manual analyst assembly.

## Supported intake layout
Expected files inside the folder:
- `README.md`
- `*BDC_INPUT_PACKET*.json`
- `unified_variant_comparison.csv`
- `current_runtime_role_mapping.csv`
- `current_slice_metrics.csv`
- `failure_case_registry.csv`
- `prompt_stage_matrix.csv`
- `lead_architect_design_priorities.md`

## Command
```powershell
python tools/bdc_designer_v2.py --pretty intake-folder --folder_path tests/data/textai_auto_packet_v2_1 --out_json results/bdc_folder_intake/intake.json
```

## Output
The command returns:
- intake registry
- missing required inputs
- normalized packet
- packet validation
- supported verdict

## Acceptance target
`TextAI_Auto` V2.1 must load in one run and emit a valid normalized packet with explicit evidence-status-aware metadata.
