n = int(input())
temp = []
for i in range(n):
    temp.append(list(map(int, input().split())))

for j in temp:
    maxv = 0
    for i in range(j[0], 0, -1):
        if j[0] % i == 0 and j[1] % i == 0:
            maxv = i
            break

    print(j[0] * j[1] // maxv, maxv)
