import sys

input = sys.stdin.readline

n = int(input().strip())
s = [0] * 21

for i in range(n):
    c = input().strip().split()

    if len(c) == 1:
        if c[0] == "all":
            s = [1]*21
        else:
            s = [0]*21

    else:
        c = list(c)
        c[1] = int(c[1])
        if c[0] == "add":
            s[c[1]] = 1
        elif c[0] == "remove":
            s[c[1]] = 0
        elif c[0] == "check":
            if s[c[1]] == 1:
                print(1)
            else:
                print(0)
        elif c[0] == "toggle":
            if s[c[1]] == 1:
                s[c[1]] = 0
            else:
                s[c[1]] = 1



