n = int(input())
nums = list(map(int, input().split()))
stack = [0]
temp = [-1] * n

for i in range(1, n):

    while stack and nums[stack[-1]] < nums[i]:
        temp[stack.pop()] = nums[i]

    stack.append(i)

print(temp)
