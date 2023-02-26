# 2023.02.09
# Written by SeongHyeon0409
from itertools import combinations

n = int(input())

avility = [list(map(int, input().split(" "))) for i in range(n)]
m = list(range(n))
answer = float('inf')

for start in list(combinations(m, n//2)):
    link = set(m) - set(start)
    a, b = 0, 0
    for i, j in list(combinations(start, 2)):
        a += avility[i][j]
        a += avility[j][i]
    for i, j in list(combinations(link, 2)):
        b += avility[i][j]
        b += avility[j][i]
    answer = min(answer, abs(a - b))

print(answer)
