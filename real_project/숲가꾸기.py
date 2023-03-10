# 2023.03.10
# Written by SeongHyeon0409

t = int(input())

for _ in range(t):
    n, c, k, p = map(int, input().split())
    ground = []
    trees = [[([] * n) for m in range(n)] for _ in range(n)]
    save = [[0] * n for _ in range(n)]

    for i in range(n):
        ground.append(list(map(int, input().split())))
    for i in range(c):
        x, y, o = map(int, input().split())
        trees[y][x].append(o)

    # 각 칸 마다 나무 리스트가 있어야 함 (나이 적은 순 오름차순)

    for l in range(p):
        # 1, 2
        for i in range(n):
            for j in range(n):
                if trees[i][j]:
                    # 어린 순부터
                    trees[i][j] = sorted(trees[i][j])
                    newtree = []
                    while trees[i][j]:
                        tree = trees[i][j].pop(0)
                        if tree <= ground[i][j]:
                            newtree.append(tree + 1)
                            ground[i][j] -= tree
                        else:
                            save[i][j] += tree//2
                    trees[i][j] = newtree
        # 2
        for i in range(n):
            for j in range(n):
                if save[i][j]:
                    ground[i][j] += save[i][j]

