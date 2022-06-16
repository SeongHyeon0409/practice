# 2020.06.14
# Presented by SeongHyeon0409

a, b = map(int, input().split())
c = (a + b) // 2
d = a - c

c, d = max(c, d), min(c, d)
if  a+b < 0 or a-b < 0 or (a + b) % 2:
    print(-1)
else:
    print(c, d)