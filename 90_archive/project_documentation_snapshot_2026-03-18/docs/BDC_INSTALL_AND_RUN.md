# BDC Designer CLI: Install and Run

This guide provides a release-ready install and run path for `bdc-designer`.

## 1) Prerequisites

- Python 3.10+
- `pip` available in your environment

Optional:
- `pipx` for isolated CLI installation

## 2) Install (pip)

From the repository root:

```bash
python -m pip install .
```

For editable local development:

```bash
python -m pip install -e .
```

## 3) Install (pipx)

If you use `pipx`, install from local path:

```bash
pipx install .
```

## 4) Stable Entrypoints

- Installed command: `bdc-designer`
- Backward-compatible script path: `python tools/bdc_designer_cli.py`

Both use the same output schema: `bdc_designer_cli_v1`.

## 5) Single Run Example

```bash
bdc-designer --task_family planner_augmented --causal_asymmetry 0.58 --dag_depth 6 --dag_branching 4 --budget_tier high --pretty
```

## 6) Batch Example

```bash
bdc-designer --input_json examples/release_examples.json --pretty
```

## 7) Save Machine-Readable Output

```bash
bdc-designer --input_json examples/release_examples.json --out_json results/tmp_release_cli_output.json
```

## 8) Version

```bash
bdc-designer --version
```

## 9) Reproducibility Check

Run the same command twice with the same input and compare outputs.
For the bundled release examples, output should be deterministic.

## 10) Scope Safety

BDC Designer is a restricted architecture-prior and strategy-selection tool.
It does not claim universal optimization or universal dominance across all tasks.
