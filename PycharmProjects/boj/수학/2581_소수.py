n = int(input())
m = int(input())

if n == 1:
    n = 2

nums = []

for i in range(n, m+1):
    flag = 0
    for j in range(2, i):
        if i % j == 0:
            flag = 1
            break
    if flag == 0:
        nums.append(i)

if not nums:
    print(-1)
else:
    print(sum(nums))
    print(min(nums))