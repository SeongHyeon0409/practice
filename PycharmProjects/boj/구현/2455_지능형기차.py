# 2020.05.21
# Presented by SeongHyeon0409

ans = 0
temp = 0

for i in range(4):
    a, b = map(int, input().split())
    temp = temp - a + b
    ans = max(ans, temp)

print(ans)