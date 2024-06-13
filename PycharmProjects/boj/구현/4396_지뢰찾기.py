dx = [0, 0, -1, -1, -1, 1, 1, 1]
dy = [-1, 1, -1, 0, 1, -1, 0, 1]

n = int(input())
t = [input() for i in range(n)]
m = [input() for i in range(n)]
def chk(y, x):
    c = 0
    for i in range(8):
        ny, nx = y + dy[i], x + dx[i]
        if 0 <= ny < n and 0 <= nx < n:
            if t[ny][nx] == "*":
                c += 1

    return str(c)

answer = []
flag = 0
for i in range(n):
    p = ''
    for j in range(n):

        if m[i][j] == 'x':
            if t[i][j] == '*':
                flag = 1
            p += chk(i, j)
        else:
            p += '.'

    answer.append(p)


if flag:
    for i in range(n):
        a = ''
        for j in range(n):
            if t[i][j] == '*':
                a += '*'
            else:
                a += answer[i][j]

        print(a)

else:
    for i in answer:
        print(i)
