# BDC Role Ontology v2 Guide

## Purpose
This guide defines the minimum supported role ontology for `BDC CLI v2`.

## Mandatory role families
- orchestrator
- planner
- analyst
- editor
- critic
- guardian
- reviewer
- harmonizer
- reporter
- router
- memory
- tool_user
- executor
- verifier
- judge
- retriever
- synthesizer

## Required metadata per role
- `role_name`
- `mission`
- `value_conditions`
- `failure_modes`
- `coordination_cost`
- `merge_candidates`
- `split_conditions`
- `anti_patterns`
- `default_caution_notes`

## Operational intent
- `coordination_cost` expresses prior overhead, not final learned truth.
- `merge_candidates` exposes deterministic merge lookup for later diagnostics.
- `anti_patterns` define default negative priors for unjustified role introduction.
- `harmonizer` is explicitly modeled as high-cost and evidence-sensitive.

## TextAI_Auto mapping
The minimum TextAI_Auto architecture roles map as:
- `orchestrator`
- `planner`
- `editor`
- `guardian`
- `harmonizer` (only as an evidence-sensitive candidate, not default recommendation)
