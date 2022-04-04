#2022.04.04
#presented by SeongHyeon0409

def lprint(l):
    for i in l:
        print(*i)

n = int(input())
m = [list(map(int, input().split())) for _ in range(n)]
dp = [[0] * n for _ in range(n)]
dp[0][0] = 1

for i in range(n):
    for j in range(n):
        if i == n-1 and j == n-1:
            break
        if i + m[i][j] < n:
            dp[i + m[i][j]][j] += dp[i][j]
        if j + m[i][j] < n:
            dp[i][j + m[i][j]] += dp[i][j]


print(dp[n-1][n-1])
