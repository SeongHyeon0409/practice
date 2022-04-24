# 2020.04.23
# Presented by SeongHyeon0409
# 자료구조, 힙
from queue import PriorityQueue
import sys

input = sys.stdin.readline

n = int(input().strip())
que = PriorityQueue()

for i in range(n):
    x = -(int(input().strip()))
    if x == 0:
        if que.qsize() > 0:
            print(-(que.get()))
        else:
            print(0)
    else:
        que.put(x)