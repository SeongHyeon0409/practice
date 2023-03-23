# 2023.03.23
# Written by SeongHyeon0409

from itertools import combinations

n, m = map(int, input().split())
house = []
chicken = []

for _ in range(n):
    a = list(map(int, input().split()))
    for j, l in enumerate(a):
        if l == 1:
            house.append([_+1, j+1])
        elif l == 2:
            chicken.append([_+1, j+1])

ans = float('inf')

for x in combinations(chicken, m):
    temp = 0
    for i in house:
        minc = float('inf')
        for j in x:
            minc = min(minc, abs(i[0] - j[0]) + abs(i[1] - j[1]))
        temp += minc

    ans = min(ans, temp)


print(ans)