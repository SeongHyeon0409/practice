from math import factorial

def bridge(m, n):
    if m < n:
        m, n = n, m
    return int(factorial(m)/(factorial(m-n) * factorial(n)))

n = int(input())

for i in range(n):
    m, n = map(int, input().split(' '))
    print(bridge(m, n))

