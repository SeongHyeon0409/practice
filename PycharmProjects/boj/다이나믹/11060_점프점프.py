# 2020.05.31
# Presented by SeongHyeon0409

n = int(input())
map = list(map(int, input().split()))

dp = [n+1] * n
dp[0] = 0

for i in range(n):
    for j in range(1, map[i]+1):
        if i + j < n:
            dp[i + j] = min(dp[i + j], dp[i] + 1)

print(dp[n-1] if dp[n-1] != n + 1 else -1)

