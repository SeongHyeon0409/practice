
n = int(input())
tp = []
for i in range(n):
    data = list(map(int, input().split()))
    tp.append(data)

flag = 0
answer = 0
index = 0

while(1):

    countarr = []
    for i in range(n):
        count = 0
        for j in range(n):
            if (tp[i][0] < tp[j][0] and tp[i][1] > tp[j][1]) \
                    or (tp[i][0] > tp[j][0] and tp[i][1] < tp[j][1]):
                count += 1
        countarr.append(count)

    if sum(countarr) == 0:
        break

    maxv = 0
    for i in range(n):
        tmaxv = countarr[i]
        if tmaxv > maxv:
            maxv = tmaxv
            index = i

    del tp[index]
    del countarr[index]
    n -= 1
    answer += 1

    print(countarr)
print(answer)

