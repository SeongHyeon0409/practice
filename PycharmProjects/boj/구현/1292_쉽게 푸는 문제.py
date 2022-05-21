# 2020.05.21
# Presented by SeongHyeon0409

a, b = map(int, input().split())
c = []
t = 1

while len(c) < 1001:
    for i in range(t):
        if len(c) > 1000:
            break
        c.append(t)
    t += 1


print(sum(c[a-1:b]))
