# 2020.04.08
# Presented by SeongHyeon0409

n = int(input())
m = int(input())
fixed = [int(input()) for _ in range(m)]
dp = [0] * (n+1)

dp[0] = 1
dp[1] = 1

for i in range(2, n+1):
    if i-1 in fixed or i in fixed:
        dp[i] = dp[i-1]
    else:
        dp[i] = dp[i-1] + dp[i-2]

print(dp)
print(dp[n])

