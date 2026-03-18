# BDC Measurement Gap Detector

## Purpose
Emit the minimum additional measurement set needed to move from cautious guidance to stronger redesign guidance.

## Current priority metrics
- accepted rewrite rate
- useful rewrite rate
- semantic pass proxy
- revert rate
- runtime
- cost

## Priority slices
- `forensic_high_ai_5`
- `mid_ai_4`
- `real_eval_primary_20`

## Product rule
When BDC cannot justify stronger redesign confidence, it must name the minimum missing measurements rather than leaving the operator to guess.
