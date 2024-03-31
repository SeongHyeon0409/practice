import sys
sys.setrecursionlimit(99999)
n = int(input())
numbers = list(map(int, input().split()))

xidx = 0
yidx = 0
flag = 0
for i in range(n-1, -1, -1):
    if numbers[i] > numbers[i-1]:
        yidx = i
        xidx = i-1
        break

for i in range(n-1, -1, -1):
    if numbers[i] > numbers[xidx]:
        numbers[i], numbers[xidx] = numbers[xidx], numbers[i]
        break

numbers1 = numbers[:yidx] + sorted(numbers[yidx:])

if numbers1 == sorted(numbers):
    print(-1)
else:
    print(*numbers1)