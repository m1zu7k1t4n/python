import bisect

s = int(input())
n = int(input())

e = [False for i in range(0, s)]
v = [int(input()) for i in range(0, n)]
for t in v:
    if t < s:
        e[t] = True

v = sorted(v)
z = [a + b for (a, b) in zip(v[0:n - 1], v[1:n])]


def solve(i):
    r = s - v[i]
    a = bisect.bisect_left(v, r - v[n - 1], lo=i + 1)
    b = bisect.bisect_right(z, r, lo=a)
    return [e[r - w] for w in v[a:b]].count(True)

print(sum([solve(i) for i in range(0, n - 2)]))
