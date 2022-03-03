n, m = map(int, input().split())

if n == 1:
    n = 2

nums = [True] * (m+1)
nums[0] = False
nums[1] = False

for i in range(2, m+1):
    if nums[i] == True:
        j = 2
        while (i * j) <= m:
            nums[i*j] = False
            j += 1

for i in range(n, m+1):
    if nums[i] == True:
        print(i)