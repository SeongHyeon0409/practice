# 2020.05.03
# Presented by SeongHyeon0409

from collections import deque

n = int(input())

map = [map(int, input().split()) for _ in range()]

dx, dy = [0, 0, -1, 1], [-1, 1, 0, 0]

# 초기 아기 상어 크기 2
# 1초에 상하좌우 한 칸씩 이동
# 자기보다 큰 물고기 이동 불가 ,자기보다 작은물고기 이동가능
# 가장 가까운 물고기 (위, 왼쪽 우선)
# 자기 크기와 같은 수를 먹으면 크기가 커짐

queue = deque()

for i in range(n):
    for j in range(n):
        if map[i][j] != 0:
            queue.append([i, j, map[i][j]])
