# Simulation Toolchain — Icarus Verilog

## Overview
This document describes the setup and usage of the simulation environment used for BDC quaternary logic modules (starting with WP1-C: Half-Adder).

## Tool
**Simulator:** Icarus Verilog (iverilog)
**Version:** 11.0 or later
**Supported Platforms:** Windows (Chocolatey), Linux (APT), macOS (Homebrew)

## Installation
- **Windows:**
  ```powershell
  choco install icarus-verilog -y
  refreshenv
  ```
- **Ubuntu/Debian:**
  ```bash
  sudo apt update && sudo apt install iverilog -y
  ```
- **macOS:**
  ```bash
  brew install icarus-verilog
  ```

Verify installation:
```bash
iverilog -V
```
Expected output should contain the version string.

## Usage in BDC
Simulation is used to validate RTL modules against their truth tables. Example (WP1-C Half-Adder):
```bash
iverilog -o tb_b4_halfadder.out qcore/rtl/b4_halfadder.v qcore/tests/tb_b4_halfadder.v
vvp tb_b4_halfadder.out | tee logs/WP1-C/sim_output.log
```

Final output line should read:
```
B4_HALFADDER: PASS
```

## Maintenance
- All simulation logs are stored under `logs/WP*/`.
- Temporary `.out` or `.vvp` binaries can be removed using `make clean` or manual cleanup.
- Simulation toolchain updates (e.g., new iverilog versions) should be documented and verified before TRL elevation.

## Version Control Policy
- Documentation changes are committed to branch `test`.
- Each update adds an entry in `AGENTS_LOG.md` with task ID `DOCS_SIM_TOOLCHAIN`.

## Author
BDC System Orchestrator — Codex Atomic Directive pipeline.