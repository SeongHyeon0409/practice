# 2020.04.05
# Presented by SeongHyeon0409

t = int(input())
mod = 1000000009
dp = [0] * (10000001)
dp[1], dp[2], dp[3] = 1, 2, 4

for j in range(4, 10000001):
    dp[j] = (dp[j - 1] + dp[j - 2] + dp[j - 3]) % mod

for i in range(t):
    n = int(input())
    print(dp[n] % mod)