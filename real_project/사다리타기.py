# 2023.03.10
# Written by SeongHyeon0409

# 이동은 위에서 아래
# 좌 우 이동이 우선순위가 더 높음

def printm(m):
    for i in m:
        print(*i)

t = int(input())

for _ in range(t):
    maps = []
    n, m, d = map(int, (input().split()))

    for i in range(m):
        maps.append(list(input()))

    maps = list(reversed(maps))

    # d의 위치 : 1(0, 0), 2(0, 2), 3(0, 4)
    # (0, (d-1) * 2)

    start = [0, (d - 1) * 2]

    # 좌우로 갈 경우 x 좌표 두칸 씩 이동
    # 하로 갈 경우 y 좌표 한칸 씩 이동
    current = start

    while (current[0] < m):
        if current[1] > 0 and (maps[current[0]][current[1] - 1]) == '+':
            current[1] -= 2
            current[0] += 1
        elif current[1] < n * 2 - 2 and maps[current[0]][current[1] + 1] == '+':
            current[1] += 2
            current[0] += 1
        else:
            current[0] += 1

    print(current[1] // 2 + 1)
