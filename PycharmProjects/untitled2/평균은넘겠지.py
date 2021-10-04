n = int(input())

for i in range(n):
    data = list(map(int, input().split()))
    data2 = data[1:]
    avupc = 0
    for j in data2:
        if j > sum(data2)/len(data2):
            avupc += 1

    ratio = avupc/len(data2)
    #print(str(round(ratio, 3) * 100) + '%')
    print('{percent:.3%}'.format(percent=ratio))
