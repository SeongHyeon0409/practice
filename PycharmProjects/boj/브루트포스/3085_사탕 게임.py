n = int(input())
board = []
for i in range(n):
    board.append(list(input()))

dx, dy = [0, 0, -1, 1], [-1, 1, 0, 0]
# 0, 0 부터 상하좌우 교체 해보고 상하좌우로 같은게 몇개인지 세기 > 개수 일일이 저장..

count = 0

# 변경 안했을 때 최댓값 구하기

def checkx(i, j, d):
    global temp
    ty = j
    while 0 <= ty < n:
        ty += d
        if 0 <= ty < n:
            if board[i][ty] == board[i][j]:
                temp += 1
            else:
                break
def checky(i, j, d):
    global temp
    ty = i
    while 0 <= ty < n:
        ty += d
        if 0 <= ty < n:
            if board[ty][j] == board[i][j]:
                temp += 1
            else:
                break

for i in range(n):
    for j in range(n):
        for d in range(4):
            nx, ny = j + dx[d], i + dy[d]
            if 0 <= nx < n and 0 <= ny < n:
                board[i][j], board[ny][nx] = board[ny][nx], board[i][j] # 교체
                # 위 아래로 퍼져서 찾기
                temp = 1
                checkx(i, j, -1)
                checkx(i, j, 1)
                count = max(count, temp)
                temp = 1
                checky(i, j, -1)
                checky(i, j, 1)
                count = max(count, temp)

                board[i][j], board[ny][nx] = board[ny][nx], board[i][j]  # 교체

print(count)