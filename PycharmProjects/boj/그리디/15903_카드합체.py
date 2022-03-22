from queue import PriorityQueue

que = PriorityQueue()

n, m = map(int, input().split())
a = list(map(int, input().split()))

for i in a:
    que.put(i)

for i in range(m):
    a = que.get()
    b = que.get()
    que.put(a+b)
    que.put(a+b)

sumv = 0

for i in range(que.qsize()):
    sumv += que.get()

print(sumv)