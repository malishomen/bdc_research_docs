# EXP_0010 KC1 VARIANTS EVALUATION REPORT

Run Dir: experiments\exp_0010_kc1_variants_evaluation\RESULTS\run_20260128T072709Z_1767f6b
metrics_sha256: 27ef0e40765e88a6c579a9d13b9ef32933f5325bee1ccab11d0e218c0d015e85
summary_sha256: 8f3994120951aa8e7a6bc24f4ecc53e916122971ea3cc7d5c1dc56dd184d905c
confusion_sha256: 8128aeedba72aaba01cd2c2a77a9dc2990acff84417e8fc3eb89b72c872a4535

## Evidence References
- exp_0007 analysis: reports/analysis/EXP_0007_PHASE0_FULLSWEEP_ANALYSIS.md
- exp_0009 report: reports/analysis/EXP_0009_KC1_DIAGNOSTICS_REPORT.md

## Confusion by Variant (counts)
- KC1_BASELINE | dead_config | pass=0 fail=110 total=110
- KC1_BASELINE | control | pass=110 fail=0 total=110
- KC1_BASELINE | negative_control | pass=0 fail=20 total=20

- KC1_TTT | dead_config | pass=60 fail=50 total=110
- KC1_TTT | control | pass=110 fail=0 total=110
- KC1_TTT | negative_control | pass=0 fail=20 total=20

- KC1_SLOPE | dead_config | pass=110 fail=0 total=110
- KC1_SLOPE | control | pass=0 fail=110 total=110
- KC1_SLOPE | negative_control | pass=0 fail=20 total=20

## Sanity Checks
- Negative controls: FAIL under all variants (PASS).
- Controls: PASS under KC1_BASELINE and KC1_TTT; FAIL under KC1_SLOPE (too strict).

## Interpretation (Evidence-Only)
- KC1_TTT reduces false negatives vs baseline while keeping controls and negatives consistent.
- KC1_SLOPE is overly strict (fails all controls) and is not viable under current thresholds.
