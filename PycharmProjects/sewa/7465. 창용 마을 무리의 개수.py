from collections import deque

t = int(input())

for _ in range(1, t+1):
    n, m = map(int, input().split())

    visited = [0] * (n+1)

    graph = [[] for i in range(n+1)]

    for i in range(m):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    ans = 0

    for i in range(1, n+1):
        if visited[i] == 0:
            ans += 1
            visited[i] = 1

            q = deque()
            q.append(i)
            while q:
                for j in graph[q.popleft()]:
                    if visited[j] == 0:
                        visited[j] = 1
                        q.append(j)

    print(f'#{_} {ans}')




