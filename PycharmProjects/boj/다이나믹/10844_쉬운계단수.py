n = int(input())

dp = [9]
mod = 1000000000

for i in range(1, n):
    dp.append((dp[i-1]*2-i)%(10**9))

print(dp[n-1])