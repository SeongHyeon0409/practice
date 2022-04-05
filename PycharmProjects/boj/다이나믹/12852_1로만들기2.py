# 2020.04.05
# Presented by SeongHyeon0409

n = int(input())
dp = [[10**6, 0] for i in range(n+1)]
dp[0][0] = 0
dp[1][0] = 0

for i in range(2, n+1):
    if i % 3 == 0 and dp[i//3][0] + 1 < dp[i][0]:
        dp[i][0] = dp[i//3][0] + 1
        dp[i][1] = i//3
    if i % 2 == 0 and dp[i//2][0] + 1 < dp[i][0]:
        dp[i][0] = dp[i//2][0] + 1
        dp[i][1] = i//2
    if dp[i-1][0] + 1 < dp[i][0]:
        dp[i][0] = dp[i-1][0] + 1
        dp[i][1] = i-1

print(dp[n][0])
a = n
print(n, end = ' ')
while a != 1:
    print(dp[a][1], end = ' ')
    a = dp[a][1]
