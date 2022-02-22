N = int(input())
F = int(input())

a = N % 100

N = N - a

while 1:
    if N % F == 0:
        answer = N%100
        if answer < 10:
            print("0" + str(answer))
        else:
            print(answer)
        break
    N += 1