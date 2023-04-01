# 2023.03.27
# Written by SeongHyeon0409

n, m, x, y, k = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(n)]
cmd = list(map(int, input().split()))
#동 1 서 2 북 3 남 4
# 북 바닥 : 6 2 1 5 6
# 남 바닥 : 6 5 1 2 6
# 가운데 한줄씩 올라갔다 내려오기
# 2 1 5 6 '4' '3'
# '2' 1 '5' 6 4 3
# 2 4 5 3 6 1
#
# 2 1 5 6 4 3 # 바닥 : dice[3]
# 동 : new_dice = new_dice[dice[0], dice[4], dice[2], dice[5], dice[3], dice[1]]
# 서 : new_dice = new_dice[dice[0], dice[5], dice[2], dice[4], dice[1], dice[3]]
# 북 : new_dice = new_dice[dice[1], dice[2], dice[3], dice[0], dice[4], dice[5]]
# 북 : new_dice = new_dice[dice[3], dice[0], dice[1], dice[2], dice[4], dice[5]]
# 동 1 6 4 3 > 4 3 6 1
# 서 1 6 4 3 > 3 4 1 6
# 북 2 1 4 6 > 1 5 6 2
# 남 2 1 4 6 > 6 2 1 5

# 동 바닥 : 6 3 1 4 6

# 서 바닥 : 6 4 1 3 6
# 2 4 1 3 5 6

dice = [0, 0, 0, 0, 0, 0]
new_dice = [0, 0, 0, 0, 0, 0]
# if maps[x][y] == 0:
#   maps[x][y] = new_dice[3]
for i in cmd:
    if i == 1:
        if y + 1 < m:
            y += 1
            new_dice = [dice[0], dice[4], dice[2], dice[5], dice[3], dice[1]]
            if maps[x][y] == 0:
                maps[x][y] = new_dice[3]
            else:
                new_dice[3] = maps[x][y]
        else:
            continue
    elif i == 2:
        if y - 1 > -1:
            y -= 1
            new_dice = [dice[0], dice[5], dice[2], dice[4], dice[1], dice[3]]
            if maps[x][y] == 0:
                maps[x][y] = new_dice[3]
            else:
                new_dice[3] = maps[x][y]
        else:
            continue
    elif i == 3:
        if x - 1 > -1:
            x -= 1
            new_dice = [dice[1], dice[2], dice[3], dice[0], dice[4], dice[5]]
            if maps[x][y] == 0:
                maps[x][y] = new_dice[3]
            else:
                new_dice[3] = maps[x][y]
        else:
            continue
    elif i == 4:
        if x + 1 < n:
            x += 1
            new_dice = [dice[3], dice[0], dice[1], dice[2], dice[4], dice[5]]
            if maps[x][y] == 0:
                maps[x][y] = new_dice[3]
            else:
                new_dice[3] = maps[x][y]
        else:
            continue
    print(new_dice[1])
    dice = new_dice