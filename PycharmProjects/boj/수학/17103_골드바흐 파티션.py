t = int(input())
n = 1000001
a = [False,False] + [True]*(n-1)

for i in range(2, int(n**0.5) + 1):
  if a[i]:
    for j in range(2*i, n+1, i):
        a[j] = False

for _ in range(t):
    n = int(input())
    ans = 0
    for i in range(2, n//2 + 1):
        if a[i] and a[n-i]:
            ans += 1

    print(ans)

