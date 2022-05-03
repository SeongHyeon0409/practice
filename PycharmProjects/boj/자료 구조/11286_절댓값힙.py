# 2020.05.03
# Presented by SeongHyeon0409

import heapq
import sys

input = sys.stdin.readline
heap = []
n = int(input().strip())

for i in range(n):
    c = int(input().strip())
    if c != 0:
        heapq.heappush(heap, (abs(c), c))
    else:
        try:
            print(heapq.heappop(heap)[1])
        except:
            print(0)