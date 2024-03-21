n = int(input())
nums = list(map(int, input().split())) + [-float('inf')]
dp = nums[:]
dp[1] = max(nums[1], nums[0] + nums[1])
dp2 = dp[:]
ans = dp[:]


for i in range(2, n):
    dp[i] = max(nums[i], dp[i-1] + nums[i])
    dp2[i] = max(dp[i-1], dp2[i-1] + nums[i]) #자기거 제거 or 전에거 제거 한거에 자기꺼더한거

    #기회 쓰려면 기회안쓴 -2에서 가져와야함.
    #기회 이미 썻다고치면 기회쓴거 -1에서 가져와야함.
print(dp)
print(dp2)

print(max(max(dp), max(dp2)))


