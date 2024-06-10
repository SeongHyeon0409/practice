t = int(input())

for tc in range(1, t+1):
    n = int(input())
    road = [0] * 200
    for i in range(n):
        a, b = map(int, input().split())

        if a > b : a, b = b, a

        a = a//2 -1 if a % 2 == 0 else a//2
        b = b//2 -1 if b % 2 == 0 else b//2

        for j in range(a, b+1):
            road[j] += 1


    print(f'#{tc} {max(road)}')

