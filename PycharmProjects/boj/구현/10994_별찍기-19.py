import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

N = int(input())
L = 4 * N - 3
stars = [[" "] * L for _ in range(L)]


def recursive(T, y, x):
    L = 4 * T - 3
    if T == 1:
        stars[y][x] = "*"
        return
    else:
        # L = 2
        for i in range(L):
            stars[y + i][x] = "*"  # 왼쪽 변
            stars[y + L - 1][x + i] = "*"  # 아랫쪽 변
            stars[y + i][x + L - 1] = "*"  # 오른쪽 변
            stars[y][x + i] = "*"  # 위쪽 변
        T -= 1
        y += 2
        x += 2
        recursive(T, y, x)


recursive(N, 0, 0)
for row in stars:
    print(''.join(map(str, row)))