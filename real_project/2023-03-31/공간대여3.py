import math, sys
input = sys.stdin.readline

def get_divisor(n):
    divisors = []
    sqrt_n = int(n ** 0.5)

    # 1부터 sqrt(n)까지 약수 구하기
    for i in range(1, sqrt_n + 1):
        if n % i == 0:
            divisors.append(i)

    # sqrt(n)보다 큰 약수 구하기
    for i in range(len(divisors) - 1, -1, -1):
        if divisors[i] != sqrt_n:
            divisors.append(n // divisors[i])

    return divisors


def find_overlap(ranges):
    # ranges: [(start1, end1), (start2, end2), ...]
    start, end = ranges[0]
    for r_start, r_end in ranges[1:]:
        start = max(start, r_start)
        end = min(end, r_end)
    return (start, end) if start < end else None

t = int(input())

for _ in range(t):
    n, r = map(int, input().split())
    info = [list(map(int, input().split())) for i in range(n)] #t, f
    info.sort(key = lambda x:x[1])

    # 최대 공약수
    a = list(map(lambda x:x[1], info))
    gcd = math.gcd(*a)
    # f의 후보 : gcd의 모든 약수

    flist = get_divisor(gcd)
    tlist = []

    #최소요금

    # 겹치는 범위를 담을 리스트
    overlap = []
    possible = []

    for f in flist:
        trange = []
        for T, F in info:
            minv = T // (F // f)
            maxv = T // (F // f - 1) if F // f > 1 else float('inf')
            trange.append([minv, maxv])
            trange.append([minv, maxv])

        # 범위들을 하나씩 비교하여 겹치는 부분을 overlap 리스트에 추가
        ranges = find_overlap(trange)
        if ranges is not None:
            possible.append([f, ranges])

    print(possible)
    
    minv, maxv = float('inf'), 0
    if possible:
        for f, t in possible:
            for i in range(t[0]+1, t[1]+1):
                v = f + (r//i * f) # 1000 + 3 * 1000 = 4000
                minv = min(minv, v)
                maxv = max(maxv, v)

        print(minv, maxv)
    else:
        print(-1)
