# EXP_0011 VNEXT SMOKE REPORT

Run Dir: experiments\exp_0011_pistream_v3_phase0_vnext_kc1_ttt\RESULTS\smoke_20260128T075827Z_a05c1ec
metrics_sha256: 59932b92d06c363af63ed48424fac439d34bc8ef3df0709d2573ce6c5ddb18ab
summary_sha256: bd3fb9e6bad2c921a73b027412b39b088fcbf19344ffa1cad0ea6a726a9dfa41

## Config Set
- dead: si64_clonal_init_per_locus_flip_p0p01, si128_clonal_init_k_point_mutation_k1p0
- controls: si64_random_init_per_locus_flip_p0p01, si128_random_init_k_point_mutation_k1p0
- negative: si64_clonal_init_per_locus_flip_p0p0

## Summary (pass_rate over 5 seeds)
- dead: 0/2 configs pass (both fail overall KC stack)
- controls: 2/2 configs pass
- negative: 0/1 config pass

## Notes (Evidence-Only)
- KC1_TTT does not automatically convert these two dead configs into PASS; overall failure may still occur via KC2.
- Controls remain PASS and negative control remains FAIL, consistent with expectations.
