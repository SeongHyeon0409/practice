import sys
input = sys.stdin.readline

n = int(input().strip())

l = [-1] + list(map(int, input().strip().split())) + [-1]

temp = 1
a = 1
for i in range(1, n+1):
    if l[i] != 0:
        if l[i] == l[i-1] or l[i] == l[i+1]:
            temp = 0
            break
    else:
        a = 0

if temp == 1 and a == 0:
    for i in range(1, n+1):
        if l[i] == 0:
            temp = -1
            if l[i-1] == 1:
                if l[i+1] != 2:
                    l[i] = 2
                else:
                    l[i] = 3
            elif l[i-1] == 2:
                if l[i+1] != 1:
                    l[i] = 1
                else:
                    l[i] = 3
            elif l[i-1] == 3:
                if l[i+1] != 1:
                    l[i] = 1
                else:
                    l[i] = 2
            else:
                if l[i+1] != 1:
                    l[i] = 1
                else:
                    l[i] = 2


if temp == 0 and a != 0:
    print(-1)
else:
    print(*l[1:-1])
