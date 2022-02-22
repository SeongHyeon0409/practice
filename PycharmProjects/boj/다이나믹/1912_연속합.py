import sys
input = sys.stdin.readline

n= int(input().strip())
nums = list(map(int, input().strip().split()))

dp = []
for i in range(n):
    dp.append(nums[i])

# 자기자신 or 바로전 최대값 + 자기자신 중 더 큰 값
for i in range(1, n):
    dp[i] = max(nums[i], nums[i] + dp[i-1])

print(max(dp))

