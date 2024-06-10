# 자기보다 큰것들 (각각에 count 1)
# 루프 도는 횟수마다 자기한테 (count 1)
from collections import deque

t = int(input())

for tc in range(1, t+1):
    n = int(input())
    m = int(input())
    graph = [[] for i in range(n+1)]
    for i in range(m):
        a, b = map(int, input().split())
        graph[a].append(b)

    count = [0] * (n+1)
    for i in range(1, n+1):
        visited = [0] * (n + 1)
        q = deque()
        q.append(i)
        while q:
            count[i] += 1
            for j in graph[q.popleft()]:
                if visited[j] == 0:
                    count[j] += 1
                    visited[j] = 1
                    q.append(j)

    ans = 0
    for i in count:
        if i == n:
            ans += 1
    print(f'#{tc} {ans}')
