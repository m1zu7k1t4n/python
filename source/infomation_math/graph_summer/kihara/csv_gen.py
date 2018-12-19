import random

with open("input.csv","w") as file:
    num = 15
    file.write("{num}\n".format(num=num))
    for _ in range(num):
        iter = " ".join([str(random.randint(1,1)) for i in range(num)])
        file.write("{}\n".format(iter))
