# 2020.06.26
# Written by SeongHyeon0409

a = []
for i in range(4):
    a.append(int(input()))
e = int(input())
f = int(input())

a.sort()
print(sum(a[1:4]) + max(e, f))

