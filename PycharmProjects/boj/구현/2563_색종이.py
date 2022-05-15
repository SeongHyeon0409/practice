# 2020.05.14
# Presented by SeongHyeon0409

n = int(input())
m = [[0] * 100 for i in range(100)]

for i in range(n):
    a, b = map(int, input().split())
    for j in range(a, a + 10):
        for k in range(b, b + 10):
            m[j][k] = 1

ans = 0

for i in m:
    ans += sum(i)

print(ans)
