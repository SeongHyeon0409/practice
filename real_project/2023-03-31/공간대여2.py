import math


def check_possible(info, mid, T):
    pay = mid
    t = T // (math.ceil(info[-1][1] / pay))
    for j in info:
        if pay + (math.floor(j[0]/t) * pay) != j[1]:
            return False
    return True

def binary_search(info, flist, T):
    res = -1
    for mid in flist:
        l, r = 1, T // mid
        while l <= r:
            t = (l + r) // 2
            if check_possible(info, mid, t*T):
                res = max(res, mid*t+mid)
                l = t+1
            else:
                r = t-1
    return res

t = int(input())

for _ in range(t):
    n, T = map(int, input().split())
    info = [list(map(int, input().split())) for i in range(n)]
    info.sort(key = lambda x:x[1])

    a = list(map(lambda x:x[1], info))
    gcd = math.gcd(*a)
    flist = []
    for i in range(1, int(math.sqrt(gcd))+1):
        if gcd % i == 0:
            flist.append(i)
            if i*i != gcd:
                flist.append(gcd // i)
    flist.sort(reverse=True)

    res = binary_search(info, flist, T)
    if res == -1:
        print(-1)
    else:
        print(res)
