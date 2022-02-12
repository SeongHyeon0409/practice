n = int(input())
tp = []
for i in range(n):
    data = list(input())
    tp.append(data)

answer = 0


for i in range(1, n):
    flag = 0
    dn = 0
    if len(tp[i]) == len(tp[0]):
        for j in range(len(tp[i])):
            if tp[i][j] != tp[0][j]:
                dn += 1
    else:
        for j in tp[i]:
            if j not in tp[0]:
                dn += 1

    if (len(tp[i]) - 1 <= len(tp[i]) <= len(tp[0]) + 1 and dn == 0) or (len(tp[i]) == len(tp[0]) and dn == 1) :
        answer += 1



print(answer)


