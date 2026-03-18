## Reproducibility

This file defines the minimum reproducibility contract.

## Requirements (current placeholders)
- Operating system and toolchain versions (recorded per run)
- Deterministic seeding via PiStream (see `SEED_POLICY.md`)
- Fixed experiment protocol (`EXPERIMENT_SPEC.md`)
- Icarus Verilog 11.0+ for WP2 simulations

## Minimal steps (WP2)
1) Install toolchain:
   - Windows: `choco install iverilog -y` then `refreshenv`
   - Linux: `sudo apt install iverilog -y`
   - macOS: `brew install icarus-verilog`
2) Run the WP2 control simulation:
   - `iverilog -o sim_wp2 tb/tb_qmem_ctrl.v rtl/qmem_ctrl.v rtl/qmem_init.v && vvp sim_wp2 | tee sim_output.log`
3) Verify PASS marker:
   - `grep -q "PASS" sim_output.log`
4) Run reproducibility checks:
   - `bash scripts/verify_reproducibility.sh`

## Update rule
If any command, dependency, or environment requirement changes, this file MUST be
updated in the same commit, along with a new experiment version.
