N, M = map(int, input().split())
chess = []
for i in range(N):
    chess.append(list(input()))

#0x0 = black or white
minn = 2501
for i in range(N-7): #0, 1
    for j in range(M-7): #0, 1
        answer1 = 0
        answer2 = 0
        for k in range(i, i+8): #0, 7
            for l in range(j, j+8): #0, 7
                if (k + l) % 2== 0:
                    if chess[k][l] != 'W':
                        answer1 += 1
                    else:
                        answer2 += 1
                else:
                    if chess[k][l] != 'B':
                        answer1 += 1
                    else:
                        answer2 += 1

        minn = min(minn, answer1, answer2)

print(minn)

