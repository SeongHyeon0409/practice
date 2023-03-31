# 2023.03.31
# Written by SeongHyeon0409

n, m = map(int, input().split())
nums = []
for i in range(n):
    nums.append(int(input()))
nums.sort()
ans = float('inf')
left = 0
right = 1

while right < n:
    diff = nums[right] - nums[left]  # 두 수의 차이 계산

    if diff >= m:
        ans = min(ans, diff)
        if ans == m:
            break
        left += 1
    else:
        right += 1


print(ans)