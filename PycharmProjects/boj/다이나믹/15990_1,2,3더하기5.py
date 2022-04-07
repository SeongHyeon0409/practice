# 2020.04.08
# Presented by SeongHyeon0409

t = int(input())

dp = [[0,0,0] for _ in range(100001)]

mod = 1000000009

dp[1] = [1, 0, 0]
dp[2] = [0, 1, 0]
dp[3] = [1, 1, 1]

for i in range(4, 100001):
    dp[i][0] = dp[i-1][1] + dp[i-1][2] % mod
    dp[i][1] = dp[i-2][0] + dp[i-2][2] % mod
    dp[i][2] = dp[i-3][0] + dp[i-3][1] % mod

for i in range(t):
    n = int(input())
    print(sum(dp[n]) % mod)