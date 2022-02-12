curTem, goalTem = map(int, input().split())
if curTem > goalTem:
    curTem, goalTem = goalTem, curTem

dp = [goalTem] * 42
dp[curTem] = 0
for i in range(curTem+1, 42):
    dp[i] = min(dp[i-1]+1, dp[i])
    if i>4:
        dp[i] = min(dp[i-5]+1, dp[i])
    if i>9:
        dp[i] = min(dp[i-10]+1, dp[i])

for i in range(40, goalTem-1, -1):
    dp[i] = min(dp[i+1]+1, dp[i])
    if curTem-i > 4:
        dp[i] = min(dp[i+5]+1, dp[i])
    if curTem-i > 9:
        dp[i] = min(dp[i+10]+1, dp[i])

print(dp[goalTem])
print(dp)