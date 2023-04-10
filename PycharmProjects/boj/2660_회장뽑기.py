# 2023.04.03
# Written by SeongHyeon0409
from collections import deque

n = int(input()) # < 50
member = {}

while True:
    a, b = map(int, input().split())
    if a == -1:
        break
    if a not in member:
        member[a] = [b]
    else:
        member[a].append(b)
    if b not in member:
        member[b] = [a]
    else:
        member[b].append(a)

visited = []
ans = []
score = 51

for i in range(1, n+1):
    visited = [0] * (n+1)
    q = deque([i])
    while q:
        v = q.popleft()
        for j in member[v]:
            if visited[j] == 0:
                visited[j] = visited[v] + 1
                q.append(j)
    visited[i] = 1

    temp = max(visited)

    if temp < score:
        score = temp
        lst = [i]
    elif temp == score:
        lst.append(i)

print(score, len(lst))
print(*lst)