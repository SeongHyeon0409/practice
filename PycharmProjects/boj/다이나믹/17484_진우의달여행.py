# 2020.05.14
# Presented by SeongHyeon0409

n, m = map(int, input().split())

map = [list(map(int, input().split())) for i in range(n)]

dp = [[[0,0,0] for _ in range(m)]] +\
     [[[float('inf'),float('inf'),float('inf')]
       for _ in range(m)]for _ in range(n)]

for i in range(1, n+1):
    for j in range(m):
        if j < m-1:
            dp[i][j][0] = min(dp[i-1][j+1][1], dp[i-1][j+1][2]) + map[i-1][j]
        if j > 0:
            dp[i][j][2] = min(dp[i-1][j-1][1], dp[i-1][j-1][0]) + map[i-1][j]
        dp[i][j][1] = min(dp[i-1][j][0], dp[i-1][j][2]) + map[i-1][j]

ans = float('inf')

for i in dp[n]:
    for j in i:
        ans = min(ans, j)

print(ans)
