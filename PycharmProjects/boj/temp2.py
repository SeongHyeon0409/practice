k = int(input())

array = [[0] * k for i in range(k)]
n = 1

for i in range(k):
    for j in range(i, k):
        array[j][i] = n
        n += 1

for i in array:
    for j in i:
        if j != 0:
            print(j, end=' ')
    print()