n = int(input())

dp = [5001] * (n+5)
dp[1] = 1
dp[3] = 1
dp[5] = 1

for i in range(6, n+1):
        dp[i] = min(dp[i-3]+1 , dp[i-5]+1)

if dp[n] > 5000:
    print(-1)
else:
    print(dp[n])



