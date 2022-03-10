import collections

n, m = map(int, input().split())
l = list(map(int, input().split()))
q = collections.deque(list(range(1, n+1)))
answer = 0

for i in l:
    while True:
        if q[0] == i:
            q.popleft()
            break
        elif q.index(i) <= len(q)//2:
            while q[0] != i:
                q.append(q.popleft())
                answer += 1
        else:
            while q[0] != i:
                q.insert(0, q.pop())
                answer += 1

print(answer)