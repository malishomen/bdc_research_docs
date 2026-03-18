# TASK-0144 L0 Artifact Excerpts — exp_0017 (2h) trajectory + metadata + metrics + launcher head

Purpose: single-page L0 inspection of artifacts for `task0144_quality_2h_io` to judge plateau/noise/stability and confirm unchanged semantics (tokenizer/masking/model) + applied IO knobs.

Run tag / run_dir:
- `task0144_quality_2h_io`
- `logs/exp_0017_comprehension_v0_cloze/run_20260209T075959Z_9708fec_task0144_quality_2h_io`

## A) metrics_by_step.jsonl

### A1) Tail (last 30 lines)

```jsonl
{"step": 62000, "val": {"batches": 63, "masked_accuracy": 0.511884185054341, "masked_correct": 60711, "masked_loss": 3.264779986034027, "masked_total": 118603}}
{"step": 63000, "val": {"batches": 63, "masked_accuracy": 0.5215298095326425, "masked_correct": 61855, "masked_loss": 3.1847204757711913, "masked_total": 118603}}
{"step": 64000, "val": {"batches": 63, "masked_accuracy": 0.5054172322791161, "masked_correct": 59944, "masked_loss": 3.3643796543224167, "masked_total": 118603}}
{"step": 65000, "val": {"batches": 63, "masked_accuracy": 0.5237472913838604, "masked_correct": 62118, "masked_loss": 3.1652573935232917, "masked_total": 118603}}
{"step": 66000, "val": {"batches": 63, "masked_accuracy": 0.524000236081718, "masked_correct": 62148, "masked_loss": 3.1672667749432457, "masked_total": 118603}}
{"step": 67000, "val": {"batches": 63, "masked_accuracy": 0.5221453082974292, "masked_correct": 61928, "masked_loss": 3.1895639920937655, "masked_total": 118603}}
{"step": 68000, "val": {"batches": 63, "masked_accuracy": 0.5193376221512104, "masked_correct": 61595, "masked_loss": 3.2138604470425363, "masked_total": 118603}}
{"step": 69000, "val": {"batches": 63, "masked_accuracy": 0.5168756270920635, "masked_correct": 61303, "masked_loss": 3.2299471488233396, "masked_total": 118603}}
{"step": 70000, "val": {"batches": 63, "masked_accuracy": 0.516437189615777, "masked_correct": 61251, "masked_loss": 3.221701774360122, "masked_total": 118603}}
{"step": 71000, "val": {"batches": 63, "masked_accuracy": 0.5269934150063658, "masked_correct": 62503, "masked_loss": 3.1296899926003796, "masked_total": 118603}}
{"step": 72000, "val": {"batches": 63, "masked_accuracy": 0.5265549775300793, "masked_correct": 62451, "masked_loss": 3.1624516032272254, "masked_total": 118603}}
{"step": 73000, "val": {"batches": 63, "masked_accuracy": 0.5302648330986569, "masked_correct": 62891, "masked_loss": 3.1142876644206408, "masked_total": 118603}}
{"step": 74000, "val": {"batches": 63, "masked_accuracy": 0.5294132526158698, "masked_correct": 62790, "masked_loss": 3.125159805655639, "masked_total": 118603}}
{"step": 75000, "val": {"batches": 63, "masked_accuracy": 0.5261839919732216, "masked_correct": 62407, "masked_loss": 3.1491470265510912, "masked_total": 118603}}
{"step": 76000, "val": {"batches": 63, "masked_accuracy": 0.5254757468192204, "masked_correct": 62323, "masked_loss": 3.1529742040582933, "masked_total": 118603}}
{"step": 77000, "val": {"batches": 63, "masked_accuracy": 0.5234859151960743, "masked_correct": 62087, "masked_loss": 3.165106882885419, "masked_total": 118603}}
{"step": 78000, "val": {"batches": 63, "masked_accuracy": 0.5241182769407182, "masked_correct": 62162, "masked_loss": 3.163475035527532, "masked_total": 118603}}
{"step": 79000, "val": {"batches": 63, "masked_accuracy": 0.5338988052578771, "masked_correct": 63322, "masked_loss": 3.0731088038406624, "masked_total": 118603}}
{"step": 80000, "val": {"batches": 63, "masked_accuracy": 0.5354754938745225, "masked_correct": 63509, "masked_loss": 3.0771278363400376, "masked_total": 118603}}
{"step": 81000, "val": {"batches": 63, "masked_accuracy": 0.534632344881664, "masked_correct": 63409, "masked_loss": 3.0787493898079688, "masked_total": 118603}}
{"step": 82000, "val": {"batches": 63, "masked_accuracy": 0.5329038894463041, "masked_correct": 63204, "masked_loss": 3.092461608746228, "masked_total": 118603}}
{"step": 83000, "val": {"batches": 63, "masked_accuracy": 0.5295397249647985, "masked_correct": 62805, "masked_loss": 3.124476946058687, "masked_total": 118603}}
{"step": 84000, "val": {"batches": 63, "masked_accuracy": 0.5317066178764449, "masked_correct": 63062, "masked_loss": 3.1207783014281034, "masked_total": 118603}}
{"step": 85000, "val": {"batches": 63, "masked_accuracy": 0.5233594428471455, "masked_correct": 62072, "masked_loss": 3.1705128476186375, "masked_total": 118603}}
{"step": 86000, "val": {"batches": 63, "masked_accuracy": 0.5252480965911486, "masked_correct": 62296, "masked_loss": 3.1453576878251064, "masked_total": 118603}}
{"step": 87000, "val": {"batches": 63, "masked_accuracy": 0.5385192617387419, "masked_correct": 63870, "masked_loss": 3.03944716408483, "masked_total": 118603}}
{"step": 88000, "val": {"batches": 63, "masked_accuracy": 0.5404500729323879, "masked_correct": 64099, "masked_loss": 3.0359503636829315, "masked_total": 118603}}
{"step": 89000, "val": {"batches": 63, "masked_accuracy": 0.533148402654233, "masked_correct": 63233, "masked_loss": 3.0816616822138183, "masked_total": 118603}}
{"step": 90000, "val": {"batches": 63, "masked_accuracy": 0.535467062384594, "masked_correct": 63508, "masked_loss": 3.0585846124551286, "masked_total": 118603}}
{"step": 91000, "val": {"batches": 63, "masked_accuracy": 0.5346070504118783, "masked_correct": 63406, "masked_loss": 3.0943933426487025, "masked_total": 118603}}
```

### A2) Mid-trajectory window (around step=50000; 45000..55000)

```jsonl
{"step": 45000, "val": {"batches": 63, "masked_accuracy": 0.4827533873510788, "masked_correct": 57256, "masked_loss": 3.5012022885739675, "masked_total": 118603}}
{"step": 46000, "val": {"batches": 63, "masked_accuracy": 0.49744947429660297, "masked_correct": 58999, "masked_loss": 3.4282977440610036, "masked_total": 118603}}
{"step": 47000, "val": {"batches": 63, "masked_accuracy": 0.49998735276510714, "masked_correct": 59300, "masked_loss": 3.3804177546156806, "masked_total": 118603}}
{"step": 48000, "val": {"batches": 63, "masked_accuracy": 0.5139751945566301, "masked_correct": 60959, "masked_loss": 3.2739966136905068, "masked_total": 118603}}
{"step": 49000, "val": {"batches": 63, "masked_accuracy": 0.5124828208392705, "masked_correct": 60782, "masked_loss": 3.264235383007676, "masked_total": 118603}}
{"step": 50000, "val": {"batches": 63, "masked_accuracy": 0.5113361382089829, "masked_correct": 60646, "masked_loss": 3.281271814627568, "masked_total": 118603}}
{"step": 51000, "val": {"batches": 63, "masked_accuracy": 0.5054340952589732, "masked_correct": 59946, "masked_loss": 3.3208184593836685, "masked_total": 118603}}
{"step": 52000, "val": {"batches": 63, "masked_accuracy": 0.5094306214851226, "masked_correct": 60420, "masked_loss": 3.311666825834368, "masked_total": 118603}}
{"step": 53000, "val": {"batches": 63, "masked_accuracy": 0.5082502128951207, "masked_correct": 60280, "masked_loss": 3.319769354884474, "masked_total": 118603}}
{"step": 54000, "val": {"batches": 63, "masked_accuracy": 0.5043801590179, "masked_correct": 59821, "masked_loss": 3.345540162167193, "masked_total": 118603}}
{"step": 55000, "val": {"batches": 63, "masked_accuracy": 0.5123563484903417, "masked_correct": 60767, "masked_loss": 3.2631368222415986, "masked_total": 118603}}
```

## B) RUN_METADATA.json (selected fields)

Requested blocks:
- `training` (full)
- `masking` (full)
- `git_head`, `torch/cuda` fields

Note:
- `model` section: **absent**
- `optimizer` section: **absent**

```json
{
  "dataset_root": "D:\\datasets\\bdc\\simplified_wiki_v0\\20260201\\full_build",
  "device": "cuda",
  "git_head": "9708fecb84eccc9b2418a1e26820945bbc2a0cc5",
  "masking": {
    "mask_rate": 0.15,
    "mask_salt": "comprehension_v0_cloze_mask_v1",
    "mask_span_max": 3
  },
  "seed": 12345,
  "tokenizer": {
    "mask_id": 1,
    "name": "whitespace_hash",
    "pad_id": 0,
    "vocab_size": 8192
  },
  "torch_cuda_available": true,
  "torch_cuda_device_name": "NVIDIA GeForce GTX 1080 Ti",
  "torch_version": "2.5.1+cu121",
  "training": {
    "batch_size": 32,
    "eval_every": 1000,
    "eval_max_docs": 2000,
    "lr": 0.0003,
    "max_docs": null,
    "max_seqs_per_doc": 1,
    "max_steps": 100000000,
    "max_tokens_per_doc": 2048,
    "num_workers": 4,
    "persistent_workers": true,
    "pin_memory": true,
    "prefetch_factor": 2,
    "seq_len": 256,
    "weight_decay": 0.01
  }
}
```

## C) metrics.json (full file)

```json
{
  "baseline_random_val": {
    "masked_accuracy": 9.274638921443809e-05,
    "masked_correct": 11,
    "masked_total": 118603
  },
  "baseline_shuffled_val": {
    "masked_accuracy": 0.027646855475831133,
    "masked_correct": 3279,
    "masked_total": 118603
  },
  "final_step": 91001,
  "out_dir": "logs\\exp_0017_comprehension_v0_cloze\\run_20260209T075959Z_9708fec_task0144_quality_2h_io",
  "run_id": "run_20260209T075959Z_9708fec_task0144_quality_2h_io",
  "test": {
    "batches": 63,
    "masked_accuracy": 0.5134025948845551,
    "masked_correct": 63550,
    "masked_loss": 3.246902529181848,
    "masked_total": 123782
  },
  "val": {
    "batches": 63,
    "masked_accuracy": 0.5346070504118783,
    "masked_correct": 63406,
    "masked_loss": 3.0943933426487025,
    "masked_total": 118603
  },
  "verdict_kc_sanity": "PASS"
}
```

Extra fields check:
- `train_loss` / `lr` / `time_sec`: **not present** in `metrics.json` for this run (only val/test/baselines + final_step + verdict).

## D) Launcher log (first 20 lines)

Source:
- `logs/exp_0017_comprehension_v0_cloze/_launchers/launcher_20260209T075956Z_task0144_quality_2h_io.log`

```text
C:\Users\user\AppData\Local\Programs\Python\Python311\Lib\site-packages\torch\nn\modules\transformer.py:379: UserWarning: enable_nested_tensor is True, but self.use_nested_tensor is False because encoder_layer.norm_first was True
  warnings.warn(
expected dbb3b1bce7864db98beef169ff81181daeaaf5382d7e85ed82fba025597ff687
actual dbb3b1bce7864db98beef169ff81181daeaaf5382d7e85ed82fba025597ff687
KC_DATA_INTEGRITY: PASS
STEP 1/100000000 loss=276.703583 steps_per_s=0.24 wall_s=4.2
STEP 200/100000000 loss=24.893303 steps_per_s=10.73 wall_s=22.8
STEP 400/100000000 loss=16.738968 steps_per_s=13.15 wall_s=38.0
STEP 600/100000000 loss=11.789902 steps_per_s=13.30 wall_s=53.1
STEP 800/100000000 loss=8.107169 steps_per_s=13.15 wall_s=68.3
STEP 1000/100000000 loss=7.244287 steps_per_s=13.43 wall_s=83.2
EVAL step=1000 val_acc=0.114947 val_loss=6.860647
STEP 1200/100000000 loss=5.100416 steps_per_s=8.46 wall_s=106.8
STEP 1400/100000000 loss=6.192059 steps_per_s=14.28 wall_s=120.8
STEP 1600/100000000 loss=5.591522 steps_per_s=13.28 wall_s=135.9
STEP 1800/100000000 loss=6.077754 steps_per_s=12.46 wall_s=151.9
STEP 2000/100000000 loss=6.177290 steps_per_s=13.50 wall_s=166.7
EVAL step=2000 val_acc=0.117586 val_loss=5.909378
STEP 2200/100000000 loss=5.513007 steps_per_s=8.37 wall_s=190.6
STEP 2400/100000000 loss=5.826262 steps_per_s=12.54 wall_s=206.6
```

