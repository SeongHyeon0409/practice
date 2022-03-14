n = int(input())
l = list(map(int, input().split()))
d = dict()
a = 0

for i in sorted(l):
    if i not in d:
        d[i] = a
        a += 1

for i in l:
    print(d[i], end = ' ')
