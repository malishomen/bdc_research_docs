Read `BDC_PACKET_READY_NATIVE_CONTRACT_FIX.md` and execute it as a pure native-intake remap cycle.

Work only inside the current measured Cockpit packet.
Do not run a new measurement cycle unless a required field is truly absent.
Do not reopen architecture discussion.
Do not widen scope.

Your goal:
Turn the already measured packet into a native `BDC Designer` packet that binds correctly at intake.

Required actions:
1. create these exact top-level files:
   - `README.md`
   - `BDC_INPUT_PACKET_COCKPIT_RUNTIME_AUDIT.json`
   - `unified_variant_comparison.csv`
   - `current_runtime_role_mapping.csv`
   - `current_slice_metrics.csv`
   - `failure_case_registry.csv`
   - `prompt_stage_matrix.csv`
   - `lead_architect_design_priorities.md`
2. remap the existing measured evidence into those files honestly;
3. preserve failures as explicit negative evidence;
4. keep supporting files and `RAW_EVIDENCE` intact;
5. package the result as `BDC_PACKET_NATIVE_READY.zip`.

Rules:
- do not invent git hashes;
- do not hide reconnect/session-loss failures;
- do not leave variant tables empty;
- do not keep required files under alternate names only;
- do not output another prep-only packet.

Final response format:
- `native_packet_ready = yes/no`
- `required_files_bound = yes/no`
- `main_negative_signal = ...`
- `main_runtime_strength = ...`
- `send_to_bdc_now = yes/no`
- `final_archive = BDC_PACKET_NATIVE_READY.zip / not_created`
