insts = {}
with open("test.disass") as test_disass:
    for line in test_disass:
        if line.startswith("800") and ":" in line:
            insts[line[0:8]] = line.strip()

with open("rtl.dump")  as rtl_dump, open("spike.dump") as spike_dump:
    print("    spike      |     rtl        |                            	instruction")
    for rtl_line, spike_line in zip(rtl_dump, spike_dump):
        if rtl_line != spike_line:
            addr = rtl_line[4:12]
            print(f"{spike_line.strip()[26:]} | {rtl_line.strip()[26:]} | {insts[addr]}")
