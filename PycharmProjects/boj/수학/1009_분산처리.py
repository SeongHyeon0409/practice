t = int(input())
two = [2, 4, 8, 6]
three = [3, 9, 7, 1]
seven = [7, 9, 3, 1]
eight = [8, 4, 2, 6]

for i in range(t):
    a, b = map(int, input().split())
    a = a % 10
    if a == 1:
        print(1)
    elif a == 2:
        print(two[(b%4)-1])
    elif a == 3:
        print(three[(b%4)-1])
    elif a == 4:
        if b%2 == 0:
            print(6)
        else:
            print(4)
    elif a == 5:
        print(5)
    elif a == 6:
        print(6)
    elif a == 7:
        print(seven[(b % 4) - 1])
    elif a == 8:
        print(eight[(b % 4) - 1])
    elif a == 9:
        if b%2 == 0:
            print(1)
        else:
            print(9)
    else:
        print(10)