t = int(input())

keys = {'F' : 0, 'R' : 1, 'L' : 2, 'B' : 3}

def decrypt(before, stride):
    if before == 'R':
        return [0, stride]
    elif before == 'L':
        return [0, -stride]
    elif before == 'F':
        return [stride, 0]
    elif before == 'B':
        return [-stride, 0]

def encrypt(before, present): #진행방향
    # F, R, L, B
    if before == 'F':
        a = ['F', 'R', 'L', 'B']
    elif before == 'R':
        a = ['R', 'B', 'F', 'L']
    elif before == 'L':
        a = ['L', 'F', 'B', 'R']
    elif before == 'B':
        a = ['B', 'L', 'R', 'F']

    return a[keys[present]]


for _ in range(t):
    n = int(input())

    maps = [list(input().split()) for i in range(n)]
    check = [[[0] * 4 for i in range(n)] for j in range(n)]

    before = 'B'
    present = maps[0][0][0]

    coord = [0, 0]
    check[0][0][3] = 1
    while True:
        stride = int(maps[coord[0]][coord[1]][1])

        before = encrypt(before, present) # 진행방향 'F'
        b = decrypt(before, stride) # [-stride, 0]

        coord[0] += b[0]
        coord[1] += b[1]
        present = maps[coord[0]][coord[1]][0]
        check[coord[0]][coord[1]][keys[before]] += 1


        #두 번 이상 같은 방향으로이동한곳
        if check[coord[0]][coord[1]][keys[before]] > 1:
            print(coord[0], coord[1])
            break



