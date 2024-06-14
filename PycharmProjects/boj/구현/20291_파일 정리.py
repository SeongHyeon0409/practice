import sys

input = sys.stdin.readline
n = int(input())

dic = dict()
for i in range(n):
    a, b = input().strip().split('.')
    if b in dic:
        dic[b] += 1
    else:
        dic[b] = 1

for n in sorted(dic.keys()):
    print(n, dic[n])