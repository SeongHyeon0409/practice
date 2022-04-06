# 2020.04.07
# Presented by SeongHyeon0409

n, m, k = map(int, input().split())

if k == 0:
    k = 1

dp = [[0] * (m) for _ in range(n)]
dp2 = [[0] * (m) for _ in range(n)]
dp[0][0] = 1

x = (k-1) // m
y = (k-1) % m

dp2[x][y] = 1

for i in range(x + 1):
    for j in range(y + 1):
        if j > 0:
            dp[i][j] += dp[i][j-1]
        if i > 0:
            dp[i][j] += dp[i-1][j]

for i in range(x, n):
    for j in range(y, m):
        if j > 0:
            dp2[i][j] += dp2[i][j-1]
        if i > 0:
            dp2[i][j] += dp2[i-1][j]

ans = dp[x][y] * dp2[n-1][m-1]
print(ans)