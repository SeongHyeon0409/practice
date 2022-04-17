# 2020.04.17
# Presented by SeongHyeon0409
import sys
input = sys.stdin.readline

n, m = map(int, input().strip().split())
a = set()
ans = []

for i in range(n):
    a.add(input().strip())

for j in range(m):
    b = input().strip()
    if b in a:
        ans.append(b)

print(len(ans))
print(*sorted(ans), sep='\n')
