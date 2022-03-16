import sys
input = sys.stdin.readline

t = int(input().strip())

for i in range(t):
    n = int(input().strip())
    s = []
    answer = n

    for j in range(n):
        s.append(list(map(int, input().split())))

    s.sort()
    maxn = s[0][1]
    for j in range(1, n):
        if maxn > s[j][1]:
            maxn = s[j][1]
        else:
            answer -= 1

    print(answer)