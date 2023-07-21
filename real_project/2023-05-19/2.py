import sys
input = sys.stdin.readline

T = int(input())

def a(num):
    return num + 1
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
    s.reverse()
    ans = [ i for i in range(n)]

    for temp in s:
        tempa = [0] * len(ans)

        for i in range(len(ans)):
            tempa[i] = ans[i] * temp

        ans = tempa[:]

        if temp == 3:
            ans.extend(list(map(a, tempa)))
            ans.extend(list(map(c, tempa)))
        else:
            ans.extend(list(map(a, tempa)))

    for i in ans:
        print(i+1, end=' ')
    print()