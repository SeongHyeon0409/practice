def simulate_forest(n, m, k, p, trees, strengths):
    # 초기화

    n, m, k, p = map(int, input().split())
    answer = 0
    ground = []
    forest = [[[] for _ in range(n)] for _ in range(n)]
    save = [[0] * n for _ in range(n)]

    for i in range(n):
        ground.append(list(map(int, input().split())))
    for i in range(c):
        x, y, o = map(int, input().split())
        trees[y][x].append(o)

    forest = [[[] for _ in range(n)] for _ in range(n)]
    for i in range(m):
        x, y, z = trees[i]
        forest[x - 1][y - 1].append(z)

    for _ in range(p):
        # 각 나무가 자신의 위치에서 양분만큼의 지력을 흡수합니다.
        for i in range(n):
            for j in range(n):
                if len(forest[i][j]) > 0:
                    forest[i][j].sort()
                    age_sum = 0
                    new_trees = []
                    for age in forest[i][j]:
                        if age <= strengths[i][j]:
                            strengths[i][j] -= age
                            age_sum += age
                            new_trees.append(age + 1)
                        else:
                            break
                    strengths[i][j] += (age_sum - sum(new_trees))
                    forest[i][j] = new_trees

        # 죽은 나무는 그 자리의 지력으로 변합니다.
        for i in range(n):
            for j in range(n):
                if len(forest[i][j]) > 0:
                    dead_sum = 0
                    for age in forest[i][j]:
                        if age % 5 == 0:
                            for di, dj in [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (-1, 1), (1, -1), (-1, -1)]:
                                ni, nj = i + di, j + dj
                                if 0 <= ni < n and 0 <= nj < n:
                                    forest[ni][nj].append(1)
                        if (strengths[i][j] + age // 2) >= age:
                            strengths[i][j] += age // 2
                        else:
                            dead_sum += age // 2
                    strengths[i][j] += dead_sum

        # 지력 회복을 진행합니다.
        for i in range(n):
            for j in range(n):
                strengths[i][j] += k

    # 남아있는 나무의 수를 세어 반환합니다.
    tree_count = 0
    for i in range(n):
        for j in range(n):
            tree_count += len(forest[i][j])
    return tree_count

simulate_forest(4, 2, 12, 420)