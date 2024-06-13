bingo = []
for i in range(5):
    bingo.append(list(map(int ,input().split())))
s = []
for i in range(5):
    temp = list(map(int, input().split()))
    s.extend(temp)

def check():
    count = 0
    # 가로
    for i in range(5):
        if sum(bingo[i]) == 0:
            count += 1

    # 세로
    for i in range(5):
        flag = 0
        for j in range(5):
            if bingo[j][i] != 0:
                flag = 1
                break
        if flag == 0:
            count += 1

    # 대각선
    flag = 0
    for i in range(5):
        if bingo[i][i] != 0:
            flag = 1
            break
    if flag == 0:
        count += 1

    flag = 0
    for i in range(5):
        if bingo[i][4-i] != 0:
            flag = 1
            break
    if flag == 0:
        count += 1

    return count

for n in range(25):
    for i in range(5):
        for j in range(5):
            if bingo[i][j] == s[n]:
                bingo[i][j] = 0
                if check() > 2:
                    print(n+1)
                    exit()