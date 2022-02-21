n = int(input())
tp = []
for i in range(0, n):
    data = list(map(int, input().split()))
    tp.append(data)

lmax = []

for i in range(0, n):
    tmax = 0
    for j in range(0,5):
        for k in range(j+1,5):
            for l in range(k+1,5):
                if ((tp[i][j] + tp[i][k] + tp[i][l]) % 10) > tmax:
                    tmax = (tp[i][j] + tp[i][k] + tp[i][l]) % 10

    lmax.append(tmax)

lastmax = 0
idex = 0

for i in range(0, n):
    if lastmax <= lmax[i]:
        lastmax = lmax[i]
        idex = i

print (idex + 1)