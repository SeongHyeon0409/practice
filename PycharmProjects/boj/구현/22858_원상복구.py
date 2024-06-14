import copy
n, k = map(int, input().split())
s = list(map(int, input().split()))
d = list(map(int, input().split()))

t = [0] * n
for i in range(k):
    for c in range(n):
        t[d[c]-1] = s[c]
    s = t[:]

print(*s)
