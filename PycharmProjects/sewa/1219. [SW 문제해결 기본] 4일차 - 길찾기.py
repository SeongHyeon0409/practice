from collections import deque

for tc in range(1, 11):
    t, n = map(int, input().split())
    graph = [[] for _ in range(100)]
    road = list(map(int, input().split()))

    for i in range(0, n * 2 - 1, 2):
        graph[road[i]].append(road[i+1])

    q = deque()
    # 출발 0 도착 99
    q.append(0)
    ans = 0
    while q:

        for i in graph[q.popleft()]:
            if i == 99:
                ans = 1
                break
            q.append(i)

    print(f'#{tc} {ans}')
