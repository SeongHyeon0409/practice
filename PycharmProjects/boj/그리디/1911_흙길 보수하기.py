# 2023.03.13
# Written by SeongHyeon0409

import math

n, l = map(int, input().split())
holes = []

for i in range(n):
    start, end = map(int, input().split())
    holes.append([start, end])

holes = sorted(holes, key=lambda x:x[0])
answer = 0

for i in range(len(holes)):
    a = math.ceil((holes[i][1] - holes[i][0]) / l)
    answer += a
    if not i == len(holes) - 1 and holes[i+1][0] - holes[i][1] < a * l - (holes[i][1] - holes[i][0]):
        holes[i+1][0] += (a * l) - (holes[i][1] - holes[i][0]) - (holes[i+1][0] - holes[i][1])


print(answer)
