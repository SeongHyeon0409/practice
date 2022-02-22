n = int(input())
t = []
for i in range(n):
    t.append(list(map(int,input().split())))


dp = []

for i in range(1, n+1):
    dp.append([0] * i)

dp[0][0] = t[0][0]

for i in range(1, n):
    for j in range(i+1):
        if j==i:
            dp[i][j] = dp[i-1][j-1] + t[i][j]
        elif j==0:
            dp[i][j] = dp[i-1][j] + t[i][j]
        else:
            dp[i][j] = max(dp[i-1][j-1] + t[i][j], dp[i-1][j] + t[i][j])

print(max(dp[n-1]))

