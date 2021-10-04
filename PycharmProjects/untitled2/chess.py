r = list(map(int, input().split()))

chess = []
answer = 0

for i in range(0, r[0]):
    row = input()
    chess.append(row)

print(chess)

for i in range(0, r[0]):
    for j in range(0, r[1]):
        if i % 2 == 0:
            if j % 2 == 0:
                if chess[i][j] != 'W':
                    answer += 1
            else:
                if chess[i][j] != 'B':
                    answer += 1
        else:
            if j % 2 == 0:
                if chess[i][j] != 'B':
                    answer += 1
            else:
                if chess[i][j] != 'W':
                    answer += 1

print (answer)

