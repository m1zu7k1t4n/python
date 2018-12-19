# coding : utf-8

from collections import Counter

length = input()
dataset = [int(x) for x in input().split(" ")]

dict_set = Counter(dataset)
begin = 0
end = 0
for tup in sorted(dict_set.items(), key=lambda x: x[1]):
    for i, piece in enumerate(dataset):
        if tup[0] == piece:
            if not begin:
                begin = i
                continue
        if
