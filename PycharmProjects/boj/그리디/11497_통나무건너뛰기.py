import sys
input = sys.stdin.readline
t = int(input().strip())
for i in range(t):
    n = int(input().strip())
    l = list(map(int, input().strip().split()))
    l.sort()

    a = []

    while l:
        a.insert(0, l.pop())
        if l:
            a.append(l.pop())

    answer = 0

    for j in range(len(a)-1):
        answer = max(answer, abs(a[j]- a[j+1]))

    print(answer)

