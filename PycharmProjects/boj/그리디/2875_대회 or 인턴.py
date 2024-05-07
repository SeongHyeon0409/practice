n, m, k = map(int, input().split())

m *= 2

while k:
    if n > m:
        n -= 1
        k -= 1
    else:
        m -= 2
        k -= 1

m //= 2
n //= 2
ans = min(n, m)

print(ans)
