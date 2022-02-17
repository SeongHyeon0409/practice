n = int(input())
nums = list(map(int, input().split()))

dp = [0] * n

for i in range(n):
    dp[i] = nums[i]

for i in range(1, n):
    for j in range(i):
        if nums[i] > nums[j]:
            dp[i] = max(dp[i], dp[j] + nums[i])

#print(dp)
print(max(dp))