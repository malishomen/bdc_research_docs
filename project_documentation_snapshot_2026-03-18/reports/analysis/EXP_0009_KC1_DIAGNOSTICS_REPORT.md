# EXP_0009 KC1 DIAGNOSTICS REPORT

Run Dir: experiments\exp_0009_kc1_diagnostics\RESULTS\run_20260128T070924Z_96cc185
metrics_sha256: aed93ed4999944109cf2e60cefc53d2199689c600da578205c329b3911d974c4
summary_sha256: 643c7dbc5124bbc2efd701437cab94f02ccbef122d3d8c726043517f9f062abe

## Evidence References
- exp_0007 analysis: reports/analysis/EXP_0007_PHASE0_FULLSWEEP_ANALYSIS.md
- exp_0008 routing: reports/analysis/EXP_0008_ROUTING_APPLICATION_EXP0007.md

## Headline Counts
- dead_config seeds: 110
- control seeds: 110
- negative_control seeds: 20

## KC1 Trigger Rates
- dead_config kc1_rate: 1.0
- control kc1_rate: 0.0
- negative_control kc1_rate: 1.0

## Early Dynamics (Medians)
- dead_config median_time_to_D>=0.10: 3.0
- control median_time_to_D>=0.10: 1.0
- dead_config median_time_to_E>=1.0: 1.0
- control median_time_to_E>=1.0: 1.0
- dead_config median_slope_D_0_10: 0.029835
- control median_slope_D_0_10: -5.2e-05

## KC1 Trigger Generation Histogram (dead_config)
- gen_1: 110

## Reachability Gaps (dead_config)
- never_reach_D>=0.10 by gen 15: 0
- never_reach_E>=1.0 by gen 15: 0

## Conclusion (Evidence-Only)
Dead configs show slow-start behavior (thresholds reached late but within gen 15).
