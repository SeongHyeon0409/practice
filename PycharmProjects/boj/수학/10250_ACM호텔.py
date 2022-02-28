import math
t = int(input())

for i in range(t):
    H, W, N = map(int, input().split()) # 6 12 10

    a = N%H
    if a == 0: a = H

    b = math.ceil(N/H) # 4

    if b < 10:
        b = "0" + str(b)

    answer = (str(a) + str(b))

    print(answer)

