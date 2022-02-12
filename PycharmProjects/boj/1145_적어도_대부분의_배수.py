numArray = list(map(int, input().split()))

tem = min(numArray)

while True:
    count = 0
    for i in numArray:
        if tem % i == 0 and tem >= i:
            count += 1
    if count > 2:
        print(tem)
        break

    tem += 1


