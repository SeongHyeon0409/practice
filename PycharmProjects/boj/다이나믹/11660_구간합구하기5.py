# 2020.04.04
# Presented by SeongHyeon0409
import copy
import sys
input = sys.stdin.readline

def printl(l):
    for i in l:
        print(*i)

def sub_one(n):
    return n - 1

n, m = map(int, input().strip().split())
l = [list(map(int, input().strip().split())) for _ in range(n)]

sum_mat = copy.deepcopy(l)

for i in range(n):
    for j in range(n):
        if i == 0 and j == 0:
            pass
        elif i == 0:
            sum_mat[0][j] += sum_mat[0][j-1]
        elif j == 0:
            sum_mat[i][0] += sum_mat[i-1][0]
        else:
            sum_mat[i][j] += sum_mat[i-1][j] + sum(l[i][:j])

for i in range(m):
    y1, x1, y2, x2 = map(sub_one, map(int, input().strip().split()))

    ans = sum_mat[y2][x2]
    if x1 > 0:
        ans -= sum_mat[y2][x1-1]
    if y1 > 0:
        ans -= sum_mat[y1-1][x2]
    if x1 > 0 and y1 > 0:
        ans += sum_mat[y1-1][x1-1]

    print(ans)
