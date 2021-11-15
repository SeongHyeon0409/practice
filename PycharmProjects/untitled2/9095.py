k = int(input())
for j in range(k):
    n = int(input())
    ary = [0, 1, 2, 4]
    for i in range(4,n+1):
        ary.append(ary[i-1] + ary[i-2] + ary[i-3])

    print(ary[n])


