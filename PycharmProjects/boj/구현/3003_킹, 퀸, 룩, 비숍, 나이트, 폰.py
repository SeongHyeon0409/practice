# 2020.04.28
# Presented by SeongHyeon0409

nums = list(map(int, input().split()))

chess = [1, 1, 2, 2, 2, 8]

for i in range(len(nums)):
    print(chess[i] - nums[i], end = ' ')
