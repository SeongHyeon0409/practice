# 2020.04.17
# Presented by SeongHyeon0409

n, m, b = map(int, input().split())

map = [ list(map(int, input().split())) for _ in range(n)]

ans = float('inf')
maxn = 0

for i in range(257):
    remov = 0
    build = 0
    for j in range(n):
        for k in range(m):
            if map[j][k] < i:
                build += i - map[j][k]
            else:
                remov += map[j][k] - i

    if build > remov + b:
        continue

    time = 2 * remov + build

    if time <= ans:
        ans = time
        maxn = i

print(ans, maxn)