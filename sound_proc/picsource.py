import pandas as pd
df = pd.read_csv("gakuhu.txt")
prev_interval = ''
with open("picsource.asm","w") as f:
    for i,v in zip(df['length'],df['interval']):
        if prev_interval == v:
            f.write("\tCALL\tTIME100U\n")
        prev_interval = v
        if i != 1:
            f.write("\tMOVLW\tD'{}'\n".format(int(i)-1))
        f.write("\tCALL\t{}\n".format(v.upper()))
