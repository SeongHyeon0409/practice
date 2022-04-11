# 2020.04.11
# Presented by SeongHyeon0409

rec = [[0] * 100 for _ in range(100)]
ans = 0

for i in range(4):
    x1, y1, x2, y2 = map(int, input().split())
    for j in range(y1, y2):
        for k in range(x1, x2):
            rec[j][k] = 1

for i in rec:
    ans += sum(i)

print(ans)