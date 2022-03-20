n, m = map(int, input().split())
a = [input() for _ in range(n)]
answer = 0

def dsf(a, n, m, x, y):
    try:
        if a[n + y][m + x] == 'N' or a[n + y][m + x] == 'S':
            if a[n + (y*2)][m + (x*2)] == 'F' or a[n + (y*2)][m + (x*2)] == 'T':
                if a[n + (y*3)][m + (x*3)] == 'P' or a[n + (y*3)][m + (x*3)] == 'J':
                    #print(a[n][m] + a[n + y][m + x] + a[n + (y*2)][m + (x*2)] + a[n + (y*3)][m + (x*3)], sep='')
                    if n + y*3 < 0 or m + x*3<0:
                        return 0
                    else:
                        return 1
    except:
        return 0

    return 0


for i in range(n):
    for j in range(m):
        if a[i][j] == 'E' or a[i][j] == 'I':
            answer += dsf(a, i, j, 1, 0)
            answer += dsf(a, i, j, 1, 1)
            answer += dsf(a, i, j, 0, 1)
            answer += dsf(a, i, j, -1, 1)
            answer += dsf(a, i, j, -1, 0)
            answer += dsf(a, i, j, -1, -1)
            answer += dsf(a, i, j, 0, -1)
            answer += dsf(a, i, j, 1, -1)

print(answer)