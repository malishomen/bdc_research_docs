# BDC CLI v2 Install and Run

## Install
```powershell
pip install .
```

## Installed entrypoint
```powershell
bdc-designer-v2 recommend --input_json bdc_real_use_packets/text_ai_auto/TEXTAI_AUTO_BDC_INPUT_PACKET_V1.json --pretty
```

## Packet-first run
```powershell
python tools/bdc_designer_v2.py recommend --input_json bdc_real_use_packets/text_ai_auto/TEXTAI_AUTO_BDC_INPUT_PACKET_V1.json --pretty
```

## Raw-case run
```powershell
python tools/bdc_designer_v2.py recommend --raw_text_file examples/bdc_cli_v2_raw_case.txt --pretty
```
