# 2020.07.09
# Written by SeongHyeon0409

import math

n, w, h ,l = map(int, input().split())

print(min(n, math.floor(w/l) * math.floor(h/l)))

