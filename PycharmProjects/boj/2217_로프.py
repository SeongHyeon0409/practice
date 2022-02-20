import sys
input = sys.stdin.readline

n = int(input().strip())
lope = [int(input().strip()) for _ in range(n)]

answer = 0
count = 1

lope.sort(reverse=True)

for i in lope:
    answer = max(answer, i*count)
    count += 1


print(answer)