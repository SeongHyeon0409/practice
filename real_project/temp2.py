t = int(input())

for _ in range(t):
    n, p = map(int, input().split())
    com = list(map(int, input().split()))

    com.sort()
    l, r = 0, n - 1

    while True:
        temp = com[l] + com[r]
        if temp == p:
            print(com[l], com[r])
            break
        elif temp < p:
            l += 1
        elif temp > p:
            r -= 1