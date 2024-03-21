import sys

input = sys.stdin.readline

n, m = map(int, input().split())


def count2(N):
    if N < 2:
        return 0

    count = 0
    while N >= 2:
        count += N // 2
        N = N // 2
    return count


def count5(N):
    if N < 5:
        return 0

    count = 0
    while N >= 5:
        count += N // 5
        N //= 5
    return count


two_count = count2(n) - count2(n - m) - count2(m)
five_count = count5(n) - count5(n - m) - count5(m)
print(min(two_count, five_count))