`riscv_buggy` incorrectly executes two instructions:
- ORI - executes XORI instead
- OR - executes XOR instead

after turning generation of these instructions off in `aapg` (using hack in `isa_funcs.py` file, by commenting out them out of `'rv32i.compute'` insturction set) all generated tests run identically on `spike` isa-simulator and `riscv_buggy`.