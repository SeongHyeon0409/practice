# 2023.03.10
# Written by SeongHyeon0409
def printm(m):
    for i in m:
        print(*i)

t = int(input())
dx = [0, 1, 1, 1, 0, -1, -1, -1]
dy = [-1, -1, 0, 1, 1, 1, 0, -1]

for _ in range(t):
    n, c, k, p = map(int, input().split())
    answer = 0
    ground = []
    trees = [[[] for _ in range(n)] for _ in range(n)]

    for i in range(n):
        ground.append(list(map(int, input().split())))
    for i in range(c):
        x, y, o = map(int, input().split())
        trees[x][y].append(o)

    # 각 칸 마다 나무 리스트가 있어야 함 (나이 적은 순 오름차순)
    for l in range(p):
        # 1
        save = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                if trees[i][j]:
                    # 어린 순부터
                    trees[i][j].sort()
                    newtree = []
                    for age in trees[i][j]:
                        if age <= ground[i][j]:
                            newtree.append(age + 1)
                            ground[i][j] -= age
                        else:

                            save[i][j] += age//2
                    trees[i][j] = newtree

        # 2
        for i in range(n):
            for j in range(n):
                if save[i][j]:
                    ground[i][j] += save[i][j]

        # 3
        for i in range(n):
            for j in range(n):
                if trees[i][j]:
                    for tree in trees[i][j]:
                        if tree % 5 == 0:
                            for x in range(8):
                                nx = j + dx[x]
                                ny = i + dy[x]
                                if 0 <= nx < n and 0 <= ny < n:
                                    trees[ny][nx].append(1)

        # 4
        for i in range(n):
            for j in range(n):
                ground[i][j] += k

    for i in range(n):
        for j in range(n):
            if trees[i][j]:
                answer += len(trees[i][j])
    print(answer)
