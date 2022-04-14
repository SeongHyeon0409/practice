# 2020.04.14
# Presented by SeongHyeon0409

n = int(input())
nums = list(map(int, input().split()))
m = int(input())
f = list(map(int, input().split()))

dict = {}

for i in nums:
    if i not in dict:
        dict[i] = 1
    else:
        dict[i] += 1

for i in f:
    if i not in dict:
        print(0, end=' ')
    else:
        print(dict[i], end=' ')