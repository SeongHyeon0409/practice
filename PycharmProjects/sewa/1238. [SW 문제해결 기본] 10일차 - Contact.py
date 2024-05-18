from collections import deque

for tc in range(1, 11):
    n, start = map(int, input().split())
    graph = [[] for i in range(101)]
    visited = [0] * 101

    data = list(map(int, input().split()))
    for i in range(0, n, 2):
        graph[data[i]].append(data[i+1])

    q = deque()
    q.append((start, 0))
    tmp = []
    while q:
        s, d = q.popleft()
        f = 0
        for i in graph[s]:
            if visited[i] == 0:
                f = 1
                q.append((i, d+1))
                visited[i] = 1
        if f == 0:
            tmp.append((s, d))

    ans = 0
    maxd = tmp[-1][1]
    for i in tmp[::-1]:
        if i[1] == maxd:
            ans = max(i[0], ans)

    print(f'#{tc} {ans}')