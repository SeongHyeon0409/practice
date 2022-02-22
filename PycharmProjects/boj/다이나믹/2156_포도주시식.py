n = int(input())
g = [int(input()) for _ in range(n)]

dp = [0] * n

dp[0] = g[0]

if n > 1:
    dp[1] = g[0] + g[1]

if n > 2:
    dp[2] = max(dp[1], g[1]+g[2] ,g[0]+g[2])

for i in range(3, n):
    dp[i] = max(dp[i-2] + g[i], dp[i-1], dp[i-3]+g[i-1]+g[i])

print(dp)
print(dp[-1])