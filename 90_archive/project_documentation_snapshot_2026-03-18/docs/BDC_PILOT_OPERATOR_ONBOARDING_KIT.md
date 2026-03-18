# BDC Pilot Operator Onboarding Kit

## 1. What This Kit Is
This kit enables a new technical operator to install, run, validate, and interpret BDC Designer with minimal supervision.

## 2. Install Guide
Primary install path:
- See `docs/BDC_INSTALL_AND_RUN.md`
- Use: `python -m pip install -e .`

## 3. Windows One-Click Guide
- See `docs/BDC_WINDOWS_QUICKSTART.md`
- Batch launcher: `launchers/bdc_designer_launcher.bat`
- PowerShell launcher: `launchers/bdc_designer_launcher.ps1`

## 4. First Valid Run Path
1. Run:
   - `python tools/bdc_designer_cli.py --input_json examples/release_examples.json --pretty`
2. Confirm output schema includes:
   - `schema_version`
   - `count`
   - `results`
3. Save output for traceability:
   - `python tools/bdc_designer_cli.py --input_json examples/release_examples.json --out_json results/tmp_operator_first_run.json --pretty`

## 5. Example Walkthrough
- Start with `examples/release_examples.json`.
- Review one recommendation object:
  - `effective_role_count`
  - `role_weights`
  - `strategy_mode`
  - `confidence`
  - `caution_flags`

## 6. Interpretation Cheat Sheet
- `effective_role_count`: target role complexity for initial design pass.
- `role_weights`: equilibrium-style prior, not a universal optimum.
- `strategy_mode`:
  - `standalone_bdc_prior`: quick prior only
  - `bdc_warm_start`: prior then local refinement
  - `bdc_pruning`: constrained search
  - `full_hybrid_search`: robust mode for high-impact workflows
- `caution_flags`: mandatory review signals, not optional metadata.

## 7. Common Error Guide
- Missing Python in PATH:
  - install Python 3.10+ and reopen terminal.
- Missing file paths:
  - run from repository root.
- PowerShell execution policy:
  - run with `-ExecutionPolicy Bypass`.
- Unknown task family:
  - treat recommendation as lower confidence and validate with pilot loop.

## 8. Pilot Checklist
- Baseline frozen before BDC run.
- Descriptor snapshot captured.
- CLI output saved.
- Caution flags reviewed.
- Hybrid refinement trace recorded.
- Baseline vs BDC vs hybrid compared.
- Operator notes stored.

## 9. Scope and Non-Claims
Restricted BDC is an architecture-prior and hybrid guidance system.
It does not claim universal optimization.
