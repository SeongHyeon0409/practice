n = int(input())
tp = []
for i in range(0, n):
    data = input()
    tp.append(data)

for i in tp:
    score = 0
    point = 0
    for j in i:
        if j == 'O':
            point = point + 1
            score = score + point
        if j == 'X':
            point = 0
    print(score)