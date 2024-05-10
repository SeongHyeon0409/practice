for _ in range(1, 11):
    n = int(input())
    ans = 0
    maps = [input() for _ in range(100)]

    # 가로
    for i in range(100):
        for j in range(100):
            for k in range(j, 100):
                nw = maps[i][j:k+1]
                if nw == nw[::-1]:
                    ans = max(ans, len(nw))


    # 세로
    for i in range(100):
        for j in range(100):
            for l in range(i, 100): # i 부터 l 까지
                nw = ''
                for k in range(i, l):
                    nw += maps[k][j]
                if nw == nw[::-1]:
                    ans = max(ans, len(nw))

    print(f'#{n} {ans}')