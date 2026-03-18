## SEED POLICY (PiStream)

Single source of truth for seeding and stream separation.

## Streams (mandatory, separated)
- ENV_PISTREAM: environment generation
- INIT_PISTREAM: initial states
- NOISE_PISTREAM: sensor/environment noise
- MUT_DECISION_PISTREAM: mutation locations/targets
- MUT_MAGNITUDE_PISTREAM: mutation magnitudes
- QUERY_PISTREAM: memory query selection (random access)

## Rules
- A stream MUST NOT be reused across subsystems.
- All seeds are deterministic and recorded.
- All experiments MUST record the master seed and all derived stream seeds.

## Pi to base-4 conversion
Canonical method (base-10 digits -> base-4 pairs):
1) Source Pi digits as an ASCII file containing decimal digits only.
   Record the file path and SHA-256 in experiment metadata.
2) Use digits after the decimal point only (ignore the leading "3.").
3) For each decimal digit d (0-9), convert to base-4 with zero pad to 2 digits:
   d=0 -> 00, 1 -> 01, 2 -> 02, 3 -> 03, 4 -> 10, 5 -> 11, 6 -> 12, 7 -> 13, 8 -> 20, 9 -> 21.
4) Concatenate all base-4 pairs to form the PiStream.
5) Stream slicing uses zero-based indexing with explicit start and length.
   Record start/length for each stream in the experiment record.
