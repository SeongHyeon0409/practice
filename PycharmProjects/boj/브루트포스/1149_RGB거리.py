n = int(input())
d = []
dp = []
for i in range(n):
    dp.append(list((map(int,input().split(" ")))))
print(dp)
for i in range(1, n):
    dp[i][0] += min(dp[i - 1][1], dp[i - 1][2])
    dp[i][1] += min(dp[i - 1][0], dp[i - 1][2])
    dp[i][2] += min(dp[i - 1][1], dp[i - 1][0])

print(dp)
print(min(dp[i]))