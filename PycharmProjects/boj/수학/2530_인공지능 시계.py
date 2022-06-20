# 2020.06.20
# Presented by SeongHyeon0409

h, m, s = map(int, input().split())
d = int(input())

if d >= 3600:
    h, d = h + d//3600, d%3600
if d >= 60:
    m, d = m + d//60, d%60

s += d

if s >= 60:
    s -= 60
    m += 1

if m >= 60:
    m -= 60
    h += 1

while h >= 24:
    h -= 24

print(h, m, s)

