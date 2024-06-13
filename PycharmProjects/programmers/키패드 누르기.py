from collections import deque

pad = [[1, 2, 3], [4, 5, 6], [7, 8, 9], ['*', 0, "#"]]
dy, dx = [0, 0 - 1, 1], [-1, 1, 0, 0]


def dis(y, x, b):  # (y, x) to b
    v = 0
    q = deque()
    q.append((y, x))
    while q:
        y, x = q.pop()
        v += 1
        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            if 0 <= ny < 4 and 0 <= nx < 3:
                if pad[ny][nx] == b:
                    return v
                q.append((ny, nx))


def solution(numbers, hand):
    l = [3, 0]
    r = [3, 2]

    for n in numbers:
        ld = dis(l[0], l[1], n)
        rd = dis(r[0], r[1], n)
        print(ld, rd)

    answer = ''
    return answer

print(solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], "a"))