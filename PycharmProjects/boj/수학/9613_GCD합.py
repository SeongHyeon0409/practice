from itertools import combinations

def gcd(n, m):
    while m:
        n, m = m, n%m

    return n

t = int(input())

for _ in range(t):
    nums = list(map(int, input().split()))[1:]
    ans = 0
    for n, m in combinations(nums, 2):
        ans +=  gcd(n, m)

    print(ans)