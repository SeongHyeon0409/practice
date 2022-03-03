n = int(input())
dec = 2

while n != 1:
    if n%dec == 0:
        print(dec)
        n = n//dec
    else:
        dec += 1