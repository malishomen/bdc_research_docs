# Lead Architect Design Priorities

1. Preserve the same bounded FIFO mechanism; do not add a second mechanism.
2. Treat control-resistant conditions as mandatory, not advisory.
3. Confirm a second bounded signal only if measured superiority survives the stricter slice.
4. Do not widen beyond bounded mechanism continuation.
