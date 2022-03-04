import sys
input = sys.stdin.readline

t = int(input().strip())
num = []

for i in range(t):
    n = int(input().strip())
    num.append(n)

n = max(num)

#에라토스테네스의 체
nums = [True] * (n*2+1)
nums[0] = False
nums[1] = False

for i in range(2, n//2+1):
    if nums[i] == True:
        j = 2
        while (i * j) <= n:
            nums[i*j] = False
            j += 1

for n in num:
    a = n//2 #두 수의 차이가 가장 적어야 하기 때문에 중간값부터 찾아봄
    for i in range(a, 1, -1):
        if nums[n-i] == True and nums[i] == True:
            print(i, n-i)
            break

