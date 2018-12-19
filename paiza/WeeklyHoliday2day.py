# coding: utf-8

max_input = int(input())
data = [int(x) for x in input().split(" ")]
count = 0
start = 0
end = 0
max = 0
for loop in range(max_input-6):
    week = data[loop:loop+7]
    if sum(week) <= 5:
        count += 1
        if max < count:
            max = count
    else:
        count = 0
if max:
    max += 6
print(max)
