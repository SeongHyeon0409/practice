import sys
input = sys.stdin.readline

n = int(input().strip())
nums = list(map(int, input().strip().split()))
stack = [0]
rbv = [-1] * n

for i in range(1, n):
    while stack and nums[stack[-1]] < nums[i]:
        rbv[stack.pop()] = nums[i]
    stack.append(i)

print(*rbv)
