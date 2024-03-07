import sys
input = sys.stdin.readline

n = int(input().strip())
nums = list(map(int, input().strip().split()))
stack = [0]
rbv = [-1] * n
counts = [0] * (1000000 + 1)

for i in nums:
    counts[i] += 1

for i in range(1, n):
    while stack and counts[nums[stack[-1]]] < counts[nums[i]]:
        rbv[stack.pop()] = nums[i]
    stack.append(i)


print(*rbv)
