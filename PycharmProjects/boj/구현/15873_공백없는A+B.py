# 2020.07.01
# Written by SeongHyeon0409

nums = input()

ans = 0

if len(nums) == 3:
    if nums[:2] == '10':
        ans = 10 + int(nums[2])
    else:
        ans = 10 + int(nums[0])
elif len(nums) == 4:
    ans = 20
else:
    ans = int(nums[0]) + int(nums[1])

print(ans)