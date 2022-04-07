# 2020.04.07
# Presented by SeongHyeon0409

n, k = map(int, input().split())
stuff = [[0,0]] + [list(map(int, input().split())) for i in range(n)]
dp = [[0] * (k+1) for i in range(n+1)]


for i in range(1, n+1):
    for j in range(1, k+1):
        weight = stuff[i][0]
        value = stuff[i][1]

        if j < weight:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(value + dp[i-1][j-weight], dp[i-1][j])

print(dp[n][k])