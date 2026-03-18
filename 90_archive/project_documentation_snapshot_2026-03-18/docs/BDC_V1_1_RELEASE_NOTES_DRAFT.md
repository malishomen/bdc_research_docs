# BDC v1.1 Release Notes (Draft)

## Release Intent
Focused usability and pilot-readiness patch built from field evidence (telemetry, operator friction, pilot feedback).

## Implemented Improvements
1. Operator interpretation quick report in CLI output.
2. Guided input validation mode (`--validate_only`) and strict validation gate (`--strict_validation`).
3. Diagnostics output option (`--diagnostics_out`) for launcher/operator support.
4. Refined caution-flag taxonomy for clearer risk interpretation.
5. Confidence calibration adjustments under descriptor complexity and budget constraints.

## Regression Posture
- Core schema keys preserved: `schema_version`, `input`, `recommendation`, `caution_flags`.
- Existing recommendation flow retained; patch focuses on operator quality and safety.

## Scope Safety
No expansion of restricted BDC scientific claim scope. This patch improves usability, reliability, and operational clarity only.
