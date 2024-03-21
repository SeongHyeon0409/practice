n = int(input())

dp = [0] * (n + 2)

dp[2] = 3

for i in range(4, n+1, 2):
    dp[i] = dp[i-2] * 3

    for j in range(i - 4, -1, -2):
        dp[i] += dp[j] * 2  # dp[j]에 특수한 모양 2개의 조합

    dp[i] += 2  # 특수한 모양 2개 추가

print(dp[n])