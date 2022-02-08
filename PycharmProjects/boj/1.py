road = []
for i in range(10):
    road.append(list(map(int, input().split())))

def a(road, i, j):
    if road[i][j + 1] == 0:
        road[i][j + 1] = 9
        a(road, i, j+1)
    elif road[i + 1][j] == 0:
        road[i + 1][j] = 9
        a(road, i+1, j)
    else:
        if road[i][j + 1] == 2:
            road[i][j + 1] = 9
        elif road[i+1][j] == 2:
            road[i+1][j] = 9
        return 0

bp = 0

for i in range(10):
    for j in range(10):
        if not road[i][j]:
            road[i][j] = 9
            a(road, i, j)
            bp = 1
            break
    if bp == 1:
        break


for i in range(10):
    print(*road[i])
