# Seed Failure Analysis

## Scope
- Analyze negative-delta GPU seeds from Phase-4 gate aggregate.

## Seed Set
- Total negative seeds: 5
- Seed 1342: delta=-1.182948
- Seed 1356: delta=-1.026403
- Seed 1352: delta=-0.891922
- Seed 1359: delta=-0.309654
- Seed 1339: delta=-0.282298

## Per-seed Findings

| Seed | Delta | Final val_loss | Grad norm mean | Token entropy mean | Mean prob max mean | Logits abs max |
|---:|---:|---:|---:|---:|---:|---:|
| 1342 | -1.182948 | 127.153430 | 1.000000 | 0.000214 | 0.999925 | 218.500000 |
| 1356 | -1.026403 | 126.691658 | 1.000000 | 0.000096 | 0.999956 | 226.625000 |
| 1352 | -0.891922 | 127.432866 | 1.000000 | 0.000160 | 0.999943 | 224.875000 |
| 1359 | -0.309654 | 126.243261 | 1.000000 | 0.000120 | 0.999958 | 235.375000 |
| 1339 | -0.282298 | 128.431806 | 1.000000 | 0.000142 | 0.999942 | 234.250000 |

## Global hypothesis
- Negative seeds are not caused by runtime nondeterminism.
- They show seed/protocol sensitivity with high-confidence token prediction collapse (low entropy, high logits magnitude).
- This degrades validation loss on a minority of seeds, while overall aggregate remains positive.
