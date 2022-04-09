# 2020.04.09
# Presented by SeongHyeon0409

n = int(input())

dp = [50001] * (n+5)

dp[0] = -1
dp[1] = -1
dp[2] = 1
dp[3] = -1
dp[5] = 1

for i in range(4, n+1):
    if dp[i-2] != -1:
        dp[i] = min(dp[i], dp[i-2] + 1)
    if dp[i-5] != -1:
        dp[i] = min(dp[i], dp[i-5] + 1)

print(dp[n])