import math


def get_divisor(n):
    n = int(n)
    divisors = []
    divisors_back = []

    for i in range(1, int(n ** (1 / 2)) + 1):
        if (n % i == 0):
            divisors.append(i)
            if (i != (n // i)):
                divisors_back.append(n // i)

    return divisors + divisors_back[::-1]

t = int(input())

for _ in range(t):
    n, T = map(int, input().split())
    info = [list(map(int, input().split())) for i in range(n)] #t, f
    info.sort(key = lambda x:x[1])

    # 최대 공약수
    a = list(map(lambda x:x[1], info))
    gcd = math.gcd(*a)
    # f의 후보 : gcd의 모든 약수

    flist = get_divisor(gcd)
    tlist = []
    #최소요금

    for pay in flist:
        for t in range(1, T+1):
            flag = 0
            for j in info:
                if pay + (j[0]//t * pay) != j[1]:
                    flag = 1
                    break
            else:
                tlist.append([t, pay])

    print(tlist)

    if tlist:
        minv, maxv = float('inf'), 0
        for i in tlist:
            v = i[1] + (T//i[0] * i[1])
            minv = min(minv, v)
            maxv = max(maxv, v)
        print(minv, maxv)

    else:
        print(-1)