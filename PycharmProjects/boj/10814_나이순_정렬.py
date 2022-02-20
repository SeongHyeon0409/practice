import sys

input = sys.stdin.readline

n = int(input())
a = []

for i in range(n):
    x,y = input().strip().split(" ")
    a.append([int(x), y])

a.sort(key = lambda x : x[0])

for i in a:
    print(i[0], i[1], sep=" ")
