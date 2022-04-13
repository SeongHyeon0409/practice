# 2020.04.13
# Presented by SeongHyeon0409

n = int(''.join(list(input().split())))
crossnums = set()

for i in range(1111, 10000):
    nums = []
    cross = list(str(i))
    if '0' not in cross:
        for j in range(4):
            cross.append(cross.pop(0))
            nums.append(int(''.join(cross)))
        nums.sort()
        crossnums.add(nums[0])
    if i == n:
        n = nums[0]

print(sorted(crossnums).index(n) + 1)
