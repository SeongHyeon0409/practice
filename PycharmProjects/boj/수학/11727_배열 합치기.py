n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

ans = []
ai = 0
bi = 0

while ai < n or bi < m:
    if bi >= m:
        ans.append(a[ai])
        ai += 1
    elif ai >= n:
        ans.append(b[bi])
        bi += 1
    else:
        if a[ai] < b[bi]:
            ans.append(a[ai])
            ai += 1
        else:
            ans.append(b[bi])
            bi += 1

print(*ans)