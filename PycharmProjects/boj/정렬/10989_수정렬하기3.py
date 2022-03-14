import sys
input = sys.stdin.readline

n = int(input())
a = [0] * 10001

for i in range(n):
    b = int(input())
    a[b] += 1

for i in range(1, 10001):
    while a[i] != 0:
        print(i)
        a[i] -= 1