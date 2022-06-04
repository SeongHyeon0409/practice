# 2020.06.03
# Presented by SeongHyeon0409

n, m = map(int, input().split())
mp = [list(map(int, input().split())) for _ in range(n)]
dp = [[0] * (m+1) for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(1, m+1):
        dp[i][j] = mp[i-1][j-1] + dp[i-1][j] + dp[i][j-1] - dp[i-1][j-1]

t = int(input())
for i in range(t):
    a, b, c, d = map(int, input().split())
    print(dp[c][d] - dp[c][b-1] - dp[a-1][d] + dp[a-1][b-1])
