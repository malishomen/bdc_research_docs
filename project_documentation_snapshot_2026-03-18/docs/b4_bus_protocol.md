# QBUS Protocol (Belnap B4)

## Overview
This document defines the base QBUS signal encoding and timing for the BDC quaternary memory interface (QMEM).

## B4 Encoding
- F  = 2'b00
- Mn = 2'b01 (underdetermined)
- My = 2'b10 (overdetermined)
- T  = 2'b11

## Signals
- ADDR[3:0] : 4-bit address bus (two quaternary digits)
- DATA_IN[3:0] : 4-bit data input bus
- DATA_OUT[3:0] : 4-bit data output bus
- QWR[1:0] : write enable (active T)
- QRD[1:0] : read enable (active T)
- QACK[1:0] : acknowledge response (B4)
- CLK : binary clock for state updates
- RST_N : active-low reset

## Acknowledge Behavior
- If QWR=T and QRD=T: QACK=My (conflict)
- If QWR=F and QRD=F: QACK=Mn (idle)
- If exactly one of QWR or QRD is T: QACK=T
- Other QWR/QRD values (Mn/My) are treated as inactive for this base implementation

## Timing
- On rising CLK edge:
  - If QWR=T and QRD!=T: write DATA_IN to MEM[ADDR]
  - If QRD=T and QWR!=T: drive DATA_OUT <= MEM[ADDR]
  - If both active, no read or write is performed (conflict)
- QACK is combinational from QWR/QRD
- DATA_OUT holds its previous value on idle, Mn/My, or conflict cycles

## Notes
- Memory depth is 16 entries (ADDR[3:0]).
- Reset clears memory to zero and DATA_OUT to zero.
- QMEM control decoding is separated in qmem_ctrl; bus selection can use qbus_mux.
