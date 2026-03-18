# BDC Client Packet Workflow

## Purpose
Run a client evidence folder end-to-end without bespoke analyst assembly.

## One-command flow
```powershell
python tools/bdc_designer_v2.py --pretty client-bundle --folder_path <client-folder> --out_root <bundle-out>
```

## Bundle contents
- `intake_manifest.json`
- `normalized_packet.json`
- `validation.json`
- `recommendation.json`
- `explanation.json`
- `redesign.json`
- `measurement_gaps.json`
- `sparse_runtime_support.json`
- `redesign_memo.md`
- `client_request_template.md`
- `bundle_summary.json`

## Operator rules
- Do not edit the normalized packet by hand before the first run.
- If validation fails, repair the client packet upstream instead of inventing fields locally.
- Deliver recommendation and redesign memo together.
- Use `measurement_gaps.json` as the only approved request list for follow-up data.
