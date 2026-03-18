# BDC CLI v2 Usage

## Commands
- `recommend --input_json <path>`
- `validate --input_json <path>`
- `explain --input_json <path>`
- `build-packet --input_json <path>`
- `compare --input_json <path> [--v1_output_json <path>] [--memo_summary_json <path>]`
- `benchmark --examples_json <path>`

## Input behavior
- If input already has `schema_version=BDC_PACKET_V2`, it is used directly.
- If input is a v1 descriptor object, CLI adapts it via `descriptor_v1_to_packet_v2`.
- If input is a legacy case packet, CLI adapts it via `legacy_packet_to_v2`.

## Example
```powershell
python tools/bdc_designer_v2.py recommend --input_json bdc_real_use_packets/text_ai_auto/TEXTAI_AUTO_BDC_INPUT_PACKET_V1.json --pretty
```
