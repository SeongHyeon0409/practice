import heapq

n = int(input())
d = [[] for i in range(10001)]
# 만약 3개 대학, (1,1), (10,2), (10,2) (10, 3) (4, 4) ( 3 , 4)과 같은 경우 출력값은 무엇인가?
# 거꾸로?
# 4 이상중에서 가장큰거 4
# 3 이상중에서 가장 큰거? 10
# 2 이상중에서 가장 큰거? 10
# 1 이상중에서 가장 큰거? 10
lec = []
# 20
for i in range(n):
    a, b = map(int, input().split())
    lec.append([a, b])
lec.sort(key = lambda x : x[1])

hq = []

for a, b in lec:
    heapq.heappush(hq, a)
    if (len(hq) > b): #len(hq) 현재 일수 (n일차) 가 가능일수를 넘기면 가장작은 원소 제거
        heapq.heappop(hq)

print(sum(hq))

