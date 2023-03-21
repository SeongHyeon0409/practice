# 2023.03.20
# Written by SeongHyeon0409

def solve(i, j):
    if j == c - 1:
        return True

    for d in dy:
        if 0 <= i + d < r and maps[i + d][j + 1] == '.' and not visit[i + d][j + 1]:
            visit[i + d][j + 1] = True
            if solve(i + d, j + 1):
                return True
    return False

r, c = map(int, input().split())
visit = [[False] * c for _ in range(r)]
maps = []
for i in range(r):
    maps.append(list(input().strip()))

ans = 0
dy = [-1, 0, 1]

for i in range(r):
    if maps[i][0] == '.':
        if solve(i, 0):
            ans += 1

print(ans)