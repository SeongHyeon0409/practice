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
    s = []
    temp = 1
    while True:
        if n != 2 and n % 2 == 0:
            s.append(2)
            n //= 2
        elif n != 3 and n % 3 == 0:
            s.append(3)
            n //= 3
        else:
            break

    ans = [ i for i in range(n)]

    while s:
        temp = s.pop()
        tempa = [0 for i in range(len(ans))]

        for i in range(len(ans)):
            tempa[i] = ans[i] * temp

        ans = tempa[:]

        if temp == 3:
            for num in tempa:
                ans.append(num + 1)
            for num in tempa:
                ans.append(num + 2)
        else:
            for num in tempa:
                ans.append(num + 1)

    for i in ans:
        print(i+1, end=' ')
    print()
