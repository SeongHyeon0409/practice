num = []

while True:
    n = int(input())
    if n == 0:
        break
    num.append(n)

n = max(num)

nums = [True] * (2*n+1)
nums[0] = False
nums[1] = False

for i in range(2, 2*n+1):
    if nums[i] == True:
        j = 2
        while (i * j) <= 2*n:
            nums[i*j] = False
            j += 1

for i in num:
    count = 0
    for j in range(i+1, i*2+1):
        if nums[j] == True:
            count += 1
    print(count)
