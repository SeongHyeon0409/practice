import sys
from itertools import permutations
input = sys.stdin.readline

n = int(input())
nums = list(permutations(list(range(1, 10)), 3))


for i in range(n):
    number, s, b = input().split()
    s, b = int(s), int(b)
    temp = []
    for num in nums:
        sc, bc = 0, 0
        for k in range(3):
            if number[k] == str(num[k]):
                sc += 1
            elif int(number[k]) in num:
                bc += 1

        if s == sc and b == bc:
            temp.append(num)

    nums = temp


print(len(nums))
