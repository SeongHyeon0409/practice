n, m = map(int, input().split())
dp = [0] * (n + 1)
dp[m] = 1
dp[2*m] = 2

for i in range(2*m + 1, n + 1):
    for j in range(1, i - m):
        dp[i] += dp[j]
    for j in range(1, i - 1):
        dp[i] += dp[j]
    dp[i] %= 10007

print(dp[n])