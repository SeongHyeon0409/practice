import sys
input = sys.stdin.readline

T = int(input())

def a(num, b):
    return num + b

def c(num):
    return num + 2


for _ in range(T):
    n = int(input())

    b = n
    s = 1
    cnt = 0
    while True:
        if n != 2 and n % 2 == 0:
            s *= 2
            n //= 2
            cnt += 1
        elif n != 3 and n % 3 == 0:
            s *= 3
            n //= 3
            cnt += 1
        else:
            break

    print(s ,cnt)
    ans = [ i for i in range(n)]


    tempa = [0] * len(ans)

    for i in range(len(ans)):
        tempa[i] = ans[i] * s

    ans = tempa[:]
    print(ans)

    for i in range(s-1):
        tempa = list(map(lambda  x: a(x, cnt), tempa))
        ans.extend(tempa)

    for i in ans:
        print(i+1, end=' ')
    print()
