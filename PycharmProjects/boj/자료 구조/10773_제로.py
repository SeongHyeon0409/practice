n = int(input())
nums = []
for i in range(n):
    a = int(input())
    if a != 0:
        nums.append(a)
    else:
        nums.pop()

print(sum(nums))