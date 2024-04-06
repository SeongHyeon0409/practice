n = int(input())
maps = [list(map(int, input().split())) for i in range(n)]

visited = [0] * n
ans = float('inf')
def dfs(l, idx):
    global ans
    if l == n//2:
        A = 0
        B = 0
        for i in range(n):
            for j in range(n):
                if visited[i] == 0 and visited[j] == 0:
                    A += maps[i][j]
                elif visited[i] == 1 and visited[j] == 1:
                    B += maps[i][j]

        ans = min(ans, abs(A-B))
        return

    for i in range(idx, n):
        if visited[i] == 0:
            visited[i] = 1
            dfs(l + 1, i + 1)
            visited[i] = 0

dfs(0, 0)
print(ans)