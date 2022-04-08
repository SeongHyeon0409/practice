# 2020.04.09
# Presented by SeongHyeon0409

n = int(input())
dp = [0, 1, 1]
for i in range(3, n+1):
    dp.append(dp[i-1] + dp[i-2])

print(dp[n] * 2 + (dp[n] + dp[n-1]) * 2)
