n = int(input())
nums = list(map(int, input().split()))
dp = [1] * n
# nums2 = list([num] for num in nums)
#
# for i in range(n):
#     for j in range(i):
#         if nums[i] > nums[j]:
#             if dp[i] < dp[j] + 1:
#                 nums2[i] = [nums[i]]
#                 dp[i] = dp[j] + 1
#                 for k in nums2[j]:
#                     nums2[i].append(k)
#
# print(max(dp))
# print(*reversed(nums2[dp.index(max(dp))]))

for i in range(n):
    for j in range(i):
        if nums[j] < nums[i]: #자기보다 작으면
            dp[i] = max(dp[i], dp[j]+1)

print(max(dp))

sequence = []
maxidx = dp.index(max(dp))
maxn = max(dp)

for i in range(maxidx, -1, -1):
    if maxn == dp[i]:
        sequence.append(nums[i])
        maxn -= 1

print(*reversed(sequence))