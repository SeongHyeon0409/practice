# 2020.04.10
# Presented by SeongHyeon0409

n = int(input())

l = sorted([list(map(int, input().split())) for _ in range(n)])

dp = [1] * n

for i in range(n):
    for j in range(i):
        if l[i][1] > l[j][1]:
            dp[i] = max(dp[j] + 1, dp[i])

print(n - max(dp))