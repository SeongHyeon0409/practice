# 2020.05.21
# Presented by SeongHyeon0409

n = int(input())
ans = 0

for i in map(int,input().split()):
    if i == n:
        ans += 1

print(ans)