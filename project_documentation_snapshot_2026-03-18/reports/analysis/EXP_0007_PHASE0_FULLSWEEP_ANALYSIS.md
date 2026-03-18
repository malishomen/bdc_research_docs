# EXP_0007 PHASE-0 FULL SWEEP ANALYSIS

Run Dir: experiments/exp_0007_pistream_v3_phase0_sweep/RESULTS/full_20260128T022709Z_2525f37
metrics_sha256: ba375c427d9452fcb36b7cc941cff4a2661190f1dd37e51b357fe8ac36e08b4d
summary_sha256: ffc728d283762cfb06c74f74d18de68fa6f19dea602317047eaa5436759eabb1

## Headline
- configs_total: 32
- pass_rate=1.0: 21
- pass_rate=0.0: 11
- pass_rate>0: 21
- pass_rate>=0.5: 21

## Breakdown
init_mode:
- clonal_init: total 16, pass_rate>0: 5, pass_rate=0: 11
- random_init: total 16, pass_rate>0: 16, pass_rate=0: 0

mutation_operator:
- k_point_mutation: total 16, pass_rate>0: 11, pass_rate=0: 5
- per_locus_flip: total 16, pass_rate>0: 10, pass_rate=0: 6

genome_length L:
- L=64: total 16, pass_rate>0: 11, pass_rate=0: 5
- L=128: total 16, pass_rate>0: 10, pass_rate=0: 6

## Dominant Failure Mode
- KC1_EARLY_COLLAPSE dominates metrics rows (KC1=16500 rows, no-KC=31500 rows).
- Early collapse correlates with clonal_init + low mutation intensity:
  - per_locus_flip with p in {0.01, 0.02, 0.05}
  - k_point_mutation with k in {1, 2, 4}

## Dead Configs (pass_rate=0.0)
- si128_clonal_init_k_point_mutation_k1p0
- si128_clonal_init_k_point_mutation_k2p0
- si128_clonal_init_k_point_mutation_k4p0
- si128_clonal_init_per_locus_flip_p0p01
- si128_clonal_init_per_locus_flip_p0p02
- si128_clonal_init_per_locus_flip_p0p05
- si64_clonal_init_k_point_mutation_k1p0
- si64_clonal_init_k_point_mutation_k2p0
- si64_clonal_init_per_locus_flip_p0p01
- si64_clonal_init_per_locus_flip_p0p02
- si64_clonal_init_per_locus_flip_p0p05

## Top 10 Configs (sorted by pass_rate desc, then median_D_at_50 desc)
- si64_clonal_init_k_point_mutation_k4p0 | pass_rate=1.0 | median_E_at_50=4.906891 | median_D_at_50=0.754741
- si128_random_init_per_locus_flip_p0p01 | pass_rate=1.0 | median_E_at_50=4.906891 | median_D_at_50=0.754687
- si64_random_init_k_point_mutation_k4p0 | pass_rate=1.0 | median_E_at_50=4.906891 | median_D_at_50=0.753772
- si64_random_init_k_point_mutation_k1p0 | pass_rate=1.0 | median_E_at_50=4.906891 | median_D_at_50=0.752586
- si128_random_init_per_locus_flip_p0p1 | pass_rate=1.0 | median_E_at_50=4.906891 | median_D_at_50=0.751904
- si64_random_init_k_point_mutation_k2p0 | pass_rate=1.0 | median_E_at_50=4.906891 | median_D_at_50=0.750718
- si128_clonal_init_k_point_mutation_k8p0 | pass_rate=1.0 | median_E_at_50=4.906891 | median_D_at_50=0.750359
- si128_random_init_k_point_mutation_k8p0 | pass_rate=1.0 | median_E_at_50=4.906891 | median_D_at_50=0.750251
- si128_clonal_init_per_locus_flip_p0p1 | pass_rate=1.0 | median_E_at_50=4.906891 | median_D_at_50=0.750180
- si64_random_init_per_locus_flip_p0p05 | pass_rate=1.0 | median_E_at_50=4.906891 | median_D_at_50=0.749641

## Notes
- Analysis uses summary CSV from full sweep; raw CSVs remain local and are not committed.
- This analysis is evidence for Quaternary Router routing gates only (infra vs cognitive separation preserved).