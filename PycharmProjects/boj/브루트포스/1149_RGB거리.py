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

# -------------------------------

n = int(input())
homes = [list(map(int, input().split())) for i in range(n)]

dp = [[0,0,0] for i in range(n)]
dp[0][0] = homes[0][0]
dp[0][1] = homes[0][1]
dp[0][2] = homes[0][2]


for i in range(1, n):
    dp[i][0] = min(dp[i-1][1] + homes[i][0], dp[i-1][2] + homes[i][0])
    dp[i][1] = min(dp[i-1][0] + homes[i][1], dp[i-1][2] + homes[i][1])
    dp[i][2] = min(dp[i-1][0] + homes[i][2], dp[i-1][1] + homes[i][2])

print(min(dp[n - 1]))