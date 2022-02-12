
n = int(input())
ary = []
for i in range(n):
    x,y = input().split(" ")
    ary.append([int(x), y])


for i in range(1, n):
    key = ary[i][0]
    key2 = ary[i]
    j = i
    while  key < ary[j-1][0] and j > 0:
        ary[j] = ary[j-1]
        j -= 1
    ary[j] = key2


for i in ary:
    print(i[0], i[1])