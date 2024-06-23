while True:
    n, m = map(int, input().split())
    if n == 0:
        break
    rank = [list(map(int, input().split())) for i in range(n)]

    player = [0] * 10001

    for i in range(n):
        for p in rank[i]:
            player[p] += 1

    total = sorted(set(player), reverse=True)
    maxp = total[1]

    answer = []
    for i in range(10001):
        if player[i] == maxp:
            answer.append(i)

    print(*answer)