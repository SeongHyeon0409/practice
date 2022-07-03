# 2020.07.03
# Written by SeongHyeon0409
import math

a, b, c = map(int, input().split())
print(int(max(a*b/c, a/b*c)))