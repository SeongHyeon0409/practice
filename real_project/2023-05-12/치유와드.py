from pprint import pprint

T = int(input())

for _ in range(T):
    n, m = map(int, input().strip().split())
    a, b = map(int, input().strip().split())

    dead = [list(map(int, input().split())) for i in range(a)]
    ward = [list(map(int, input().split())) for i in range(b)]
    maps = [[0] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            for p in dead:
                r = p[0]
                c = p[1]
                p_dist = max(abs(r - i), abs(c - j))
                maps[i][j] -= max(m - p_dist + 1, 0)
            for h in ward:
                r = h[0]
                c = h[1]
                h_dist = abs(r - i) + abs(c - j)
                maps[i][j] += max(m - h_dist + 1, 0)
    for p in dead:
        maps[p[0]][p[1]] += 1
    for h in ward:
        maps[h[0]][h[1]] -= 1
    for i in maps:
        print(*i)
