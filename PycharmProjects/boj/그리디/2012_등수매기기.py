import sys
input = sys.stdin.readline

n = int(input().strip())
l = sorted([int(input().strip()) for _ in range(n)])

answer = 0
for i in range(n):
    answer += abs((i+1) - l[i])

print(answer)