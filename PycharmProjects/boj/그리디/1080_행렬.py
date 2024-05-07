n, m = map(int, input().split())
A = [list(map(int, list(input()))) for _ in range(n)]
B = [list(map(int, list(input())))  for _ in range(n)]

def flip(y, x):
    for i in range(y, y+3):
        for j in range(x, x+3):
            if A[i][j] == 0:
                A[i][j] = 1
            else:
                A[i][j] = 0

cnt = 0

if n < 3 or m < 3:
    if A != B:
        print(-1)
        exit()
else:
    for i in range(n-2):
        for j in range(m-2):
            if A[i][j] != B[i][j]:
                flip(i, j)
                cnt += 1
if A == B:
    print(cnt)
else:
    print(-1)
