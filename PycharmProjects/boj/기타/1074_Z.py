# 2020.04.26
# Presented by SeongHyeon0409
# 이분탐색

n, r, c = map(int, input().split())
num = 0
# map = [[0] * (2**n) for i in range(2**n)]
#
# def printm(map):
#     for i in map:
#         print(*i)
#
# def z(x, y, n):
#     global num
#     if n == 1:
#         map[y+0][x+0] = num
#         num += 1
#         map[y+0][x+1] = num
#         num += 1
#         map[y+1][x] = num
#         num += 1
#         map[y+1][x+1] = num
#         num += 1
#     else:
#         a =  n//2
#         z(x, y, a)
#         z(x+a, y, a)
#         z(x, y+a, a)
#         z(x+a, y+a, a)

def solve(x, y, n):
    global num
    if x == r and y == c:
        print(num)
        exit(0)
    if n == 1:
        num += 1
        return
    if not (x <= r < x+n and y <=c < y+n):
        num += n * n
        return
    solve(x, y, n//2)
    solve(x, y + n//2, n//2)
    solve(x + n//2, y, n//2)
    solve(x + n//2, y + n//2, n//2)

solve(0, 0, 2 ** n)
print(num)