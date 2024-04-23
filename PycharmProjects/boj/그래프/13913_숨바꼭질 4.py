from collections import deque
n, k = map(int, input().split())
dist = [0] * 100001
move = [0] * 100001
arr = []

q = deque()
q.append(n)
while q:
    n = q.popleft()

    if n == k:
        t = n
        print(dist[n])
        for i in range(dist[n] + 1):
            arr.append(t)
            t = move[t]

        print(' '.join(map(str, arr[::-1])))
        break


    for i in (n + 1, n - 1, 2 * n):
        if 0 <= i <= 100000 and dist[i] == 0:
            q.append(i)
            dist[i] = dist[n] + 1
            move[i] = n


