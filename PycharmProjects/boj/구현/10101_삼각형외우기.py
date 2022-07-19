# 2020.07.19
# Written by SeongHyeon0409

a = sorted([int(input()) for i in range(3)])

if sum(a) != 180:
    print("Error")
elif a[0] == a[1] == a[2]:
    print("Equilateral")
elif a[0] != a[1] != a[2]:
    print("Scalene")
else:
    print("Isosceles")

