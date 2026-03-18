# EDP1 Scientific Snapshot 1208

## Scope
- Analysis-only snapshot across existing runtime artifacts.
- No experiment reruns; aggregation re-run only when missing.

## Variant Summary
- `edp1_exp0200_speciation`: runtime pass_rate=1.0, final_max_accuracy_mean=nan, final_mean_accuracy_mean=nan, final_max_fitness_mean=0.7881661019442968, final_mean_fitness_mean=nan, final_max_penalty_mean=nan, final_mean_penalty_mean=nan
- `edp1_exp0200_shock`: runtime pass_rate=0.9333333333333333, final_max_accuracy_mean=nan, final_mean_accuracy_mean=nan, final_max_fitness_mean=0.8037433403659048, final_mean_fitness_mean=nan, final_max_penalty_mean=nan, final_mean_penalty_mean=nan
- `edp1_exp0200_v2`: runtime pass_rate=1.0, final_max_accuracy_mean=nan, final_mean_accuracy_mean=nan, final_max_fitness_mean=0.5356865515715755, final_mean_fitness_mean=nan, final_max_penalty_mean=nan, final_mean_penalty_mean=nan
- `edp1_exp0200_v2_prior`: runtime pass_rate=1.0, final_max_accuracy_mean=0.790234375, final_mean_accuracy_mean=0.5844720052083333, final_max_fitness_mean=0.5531664379938884, final_mean_fitness_mean=0.31733006528305713, final_max_penalty_mean=nan, final_mean_penalty_mean=nan
- `edp1_exp0200_v2_staged`: runtime pass_rate=1.0, final_max_accuracy_mean=0.7884765625, final_mean_accuracy_mean=0.5883697916666667, final_max_fitness_mean=0.5524726487966959, final_mean_fitness_mean=0.3211291017413905, final_max_penalty_mean=nan, final_mean_penalty_mean=nan
- `edp1_exp0200_v2_noshock`: runtime pass_rate=0.0, final_max_accuracy_mean=nan, final_mean_accuracy_mean=nan, final_max_fitness_mean=0.5344320536004283, final_mean_fitness_mean=nan, final_max_penalty_mean=nan, final_mean_penalty_mean=nan
- `edp1_exp0200_v2_structured`: runtime pass_rate=1.0, final_max_accuracy_mean=nan, final_mean_accuracy_mean=nan, final_max_fitness_mean=0.528259165120311, final_mean_fitness_mean=nan, final_max_penalty_mean=nan, final_mean_penalty_mean=nan

## Decomposition Comparisons
- `edp1_exp0200_speciation -> edp1_exp0200_v2_staged`: delta_max_fit=-0.23569345314760093, delta_max_acc=nan, delta_max_pen=nan, residual_max=nan; delta_mean_fit=nan, delta_mean_acc=nan, delta_mean_pen=nan, residual_mean=nan
- `edp1_exp0200_speciation -> edp1_exp0200_v2_prior`: delta_max_fit=-0.2349996639504084, delta_max_acc=nan, delta_max_pen=nan, residual_max=nan; delta_mean_fit=nan, delta_mean_acc=nan, delta_mean_pen=nan, residual_mean=nan
- `edp1_exp0200_v2 -> edp1_exp0200_v2_prior`: delta_max_fit=0.017479886422312907, delta_max_acc=nan, delta_max_pen=nan, residual_max=nan; delta_mean_fit=nan, delta_mean_acc=nan, delta_mean_pen=nan, residual_mean=nan
- `edp1_exp0200_v2 -> edp1_exp0200_v2_staged`: delta_max_fit=0.016786097225120367, delta_max_acc=nan, delta_max_pen=nan, residual_max=nan; delta_mean_fit=nan, delta_mean_acc=nan, delta_mean_pen=nan, residual_mean=nan
- `edp1_exp0200_v2_prior -> edp1_exp0200_v2_staged`: delta_max_fit=-0.0006937891971925403, delta_max_acc=-0.0017578125000000666, delta_max_pen=nan, residual_max=nan; delta_mean_fit=0.003799036458333349, delta_mean_acc=0.0038977864583333854, delta_mean_pen=nan, residual_mean=nan

## Notes
- Residual near 0 implies consistency with delta_fitness ~= delta_accuracy - delta_penalty.
- `NaN` penalty/complexity deltas indicate historical runs without decomposition columns (UNVERIFIED by policy).
