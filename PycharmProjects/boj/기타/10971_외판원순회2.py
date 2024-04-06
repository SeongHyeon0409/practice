n = int(input())
cities = [list(map(int, input().split())) for i in range(n)]

ans = float('inf')
visited = [0] * n
start = 0

def dfs(depth, idx, value):
    global ans, tmp, start
    if depth == n+1:
        if cities[start][idx] == 0:
            value += cities[idx][start]
            ans = min(ans, value)
        return

    if value > ans:
        return

    # 0 인 경우는 못가는 경우
    # 출발이 0인 경우는 허용
    # 출발지와 도착지가 같아야함
    for i in range(n):
        if depth == 0:
            start = i
            dfs(depth + 1, i, value + cities[idx][i])
            #tmp -= cities[idx][i]
        elif visited[i] == 0 and cities[idx][i]:
            visited[i] = 1
            tmp += cities[idx][i]
            dfs(depth+1, i, value + cities[idx][i])
            #tmp -= cities[idx][i]
            visited[i] = 0

tmp = 0
dfs(0, 0, 0)
print(ans)
