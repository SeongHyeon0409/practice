ary = [7,3,2,1,5]

for i in range(1, 5):
    key = ary[i]
    j = i
    while  key < ary[j-1] and j > 0:
        ary[j] = ary[j-1]
        j -= 1
    ary[j] = key

print(ary)

