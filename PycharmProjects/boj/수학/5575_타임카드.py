# 2020.06.20
# Presented by SeongHyeon0409

for i in range(3):
    h, m, s, oh, om, os = map(int, input().split())
    if os < s:
        om -= 1
        os += 60
    if om < m:
        oh -= 1
        om += 60
    s = os - s
    m = om - m
    h = oh - h
    print(h, m, s)
