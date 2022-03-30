import sys
input = sys.stdin.readline

n = int(input().strip())
l = [0] + sorted([int(input().strip()) for _ in range(n)], reverse=True)

answer = 0

for i in range(1, n+1):
    if i%3 != 0:
        answer += l[i]

print(answer)

