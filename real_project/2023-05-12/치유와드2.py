def printm(m):
    for i in m:
        print(*i)


T = int(input())

for _ in range(T):
    n, m = map(int, input().split())
    mm = m
    a, b = map(int, input().split()) #시체의 수, 치유와드의 수
    dead = [list(map(int, input().split())) for i in range(a)]
    ward = [list(map(int, input().split())) for i in range(b)]
    maps = [[0] * n for _ in range(n)]


