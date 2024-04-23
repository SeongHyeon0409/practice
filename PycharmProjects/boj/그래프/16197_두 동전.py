from sys import stdin
input = stdin.readline
from collections import deque

dr = (-1, 1, 0, 0)
dc = (0, 0, -1, 1)

def bfs(ar, ac, br, bc):
    check = [[[[-1] * M for _ in range(N)] for _ in range(M)] for _ in range(N)]
    check[ar][ac][br][bc] = 0
    Q = deque([(ar, ac, br, bc)])
    while Q:
        ar, ac, br, bc = Q.popleft()
        # 10번보다 많이 눌러야 한다면 실패
        if check[ar][ac][br][bc] >= 10:
            break

	# 4방향 이동할 위치 좌표
        for d in range(4):
            nar = ar + dr[d]
            nac = ac + dc[d]
            nbr = br + dr[d]
            nbc = bc + dc[d]

            # 두 동전 모두 밖으로 떨어지면
            if not (0 <= nar < N and 0 <= nac < M) and not (0 <= nbr < N and 0 <= nbc < M):
                continue

            # 동전 a, b 중에 하나만 밖으로 떨어지면
            if not (0 <= nar < N and 0 <= nac < M):
                return check[ar][ac][br][bc] + 1
            if not (0 <= nbr < N and 0 <= nbc < M):
                return check[ar][ac][br][bc] + 1

            # 이동할 곳이 벽이면 제자리
            if board[nar][nac] == "#":
                nar -= dr[d]
                nac -= dc[d]
            if board[nbr][nbc] == "#":
                nbr -= dr[d]
                nbc -= dc[d]

            # check 배열의 이동할 위치에 현 횟수 + 1한 횟수 표시, 이동할 위치 큐에 담기
            if check[nar][nac][nbr][nbc] == -1:
                check[nar][nac][nbr][nbc] = check[ar][ac][br][bc] + 1
                Q.append((nar, nac, nbr, nbc))
    return -1

# main
N, M = map(int, input().split())
ar, ac, br, bc = 0, 0, 0, 0
board = []
flag = True
for i in range(N):
    board.append(list(input().rstrip()))
    for j in range(M):
        if board[i][j] == "o":
            if flag:
                ar, ac = i, j
                flag = False
            else:
                br, bc = i, j
print(bfs(ar, ac, br, bc))