# 2020.04.09
# Presented by SeongHyeon0409

n = int(input())
nums = list(map(int, input().split()))
dpmax = [1] * n
dpmin = [1] * n

for i in range(1, n):
    if nums[i] >= nums[i-1]:
        dpmax[i] = dpmax[i-1] + 1
    if nums[i] <= nums[i-1]:
        dpmin[i] = dpmin[i-1] + 1

print(max(max(dpmin), max(dpmax)))

