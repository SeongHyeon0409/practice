# 2020.07.09
# Written by SeongHyeon0409

n, w, h ,l = map(int, input().split())

print(min(n, (w//l) * (h//l)))

