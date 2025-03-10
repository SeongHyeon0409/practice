from collections import deque
import sys
sys.setrecursionlimit(999999)
inpout = sys.stdin.readline

N = int(input())

graph = [[] for _ in range(N+1)]
visited = [-1 for _ in range(N+1)] # BFS시 탐색 여부 확인을 위함
children = [set() for _ in range(N+1)] # 트리의 부모자식 관계를 알기 위함

for i in range(N-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

test_case = list(map(int,input().split())) # 비교할 탐색 루트
start = 1
# BFS
queue = deque()
queue.append(start)
visited[start] = 0

while queue:
    x = queue.popleft()
    for i in graph[x]:
        if visited[i] == -1:
            visited[i] = visited[x] + 1 # 방문처리
            children[x].add(i) # x의 자식은 i이다.
            queue.append(i)


next_index = 1
for i in test_case:
    if next_index == N:
        break
    c_length = len(children[i]) #자식의 길이
    c1 = set(test_case[next_index : next_index+c_length])
    c2 = children[i]
    if c1 != c2:
        print(0)
        exit()
    next_index += c_length
print(1)

