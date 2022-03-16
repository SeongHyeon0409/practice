n = int(input())

A, B, C = 0, 0, 0

if n >= 300:
    A = n//300
    n %= 300
if n >= 60:
    B = n//60
    n %= 60
if n >= 10:
    C = n//10
    n %= 10

if n != 0:
    print(-1)
else:
    print(A, B, C)