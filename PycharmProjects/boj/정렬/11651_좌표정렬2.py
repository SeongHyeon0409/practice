
n = int(input())
ary = []
for i in range(n):
    x,y = map(int,input().split(" "))
    ary.append((y, x))



b = sorted(ary)
for i in range(n):
    ary[i] = (b[i][1], b[i][0])
    print (ary[i][0], ary[i][1])

