for _ in range(1, 11):
    n = int(input())
    ans = 0
    maps = [input() for _ in range(8)]

    # 가로
    for i in range(8):
        for j in range(8-n+1):
            nw = maps[i][j:j+n]
            if nw == nw[::-1]:
                ans += 1


    # 세로
    for i in range(8-n+1):
        for j in range(8):
            nw = ''
            for l in range(n):
                nw += maps[i+l][j]
            if nw == nw[::-1]:
                ans += 1

    print(f'#{_} {ans}')