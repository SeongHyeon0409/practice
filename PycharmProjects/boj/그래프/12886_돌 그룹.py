from collections import deque

def bfs():
    global a, b, c
    q = deque()
    q.append((a, b))
    visited[a][b] = True
    while q:
        x, y = q.popleft()

        z = total - x - y
        if x == y == z:
            print(1)
            return

        for a, b in (x, y), (y, z), (x, z):
            if a < b:
                b -= a
                a += a
            elif a > b:
                a -= b
                b += b
            else:
                continue

            c = total - a - b

            x = min(min(a, b), c)
            y = max(max(a, b), c)

            if not visited[x][y]:

                q.append((x, y))

                visited[x][y] = True

    print(0)

a, b, c = map(int, input().split())
total = a + b + c
# x + x, y - x
visited = [[False] * (total + 1 ) for _ in range(total + 1)]

if total % 3 != 0:
    print(0)
else:
    bfs()



