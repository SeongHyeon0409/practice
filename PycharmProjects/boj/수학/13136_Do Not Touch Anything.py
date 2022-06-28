# 2020.06.28
# Written by SeongHyeon0409

import math

r, c, n = map(int, input().split())

print(math.ceil(r/n) * math.ceil(c/n))
