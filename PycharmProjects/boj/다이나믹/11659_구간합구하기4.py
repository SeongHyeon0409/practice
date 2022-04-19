# 2020.04.19
# Presented by SeongHyeon0409
# 누적 합
import sys
input = sys.stdin.readline

n, m = map(int, input().strip().split())
nums = list(map(int, input().strip().split()))
dp = [0] * (n + 1)
dp[1] = nums[0]

for i in range(1, n+1):
    dp[i] = dp[i-1] + nums[i-1]

for i in range(m):
    a, b = map(int, input().strip().split())
    print(dp[b] - dp[a-1])