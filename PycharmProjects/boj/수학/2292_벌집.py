#1 7 19 37 61
# 6 12 18 24

n = int(input())
b = 0
c = 1

while True:
    if n == 1:
        print(1)
        break

    b += 1
    c = c + (6*b)

    if c - n >= 0:
        print(b+1)
        break




