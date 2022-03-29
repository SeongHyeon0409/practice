import sys
input = sys.stdin.readline

t = int(input().strip())

for i in range(t):
    n = int(input().strip())
    l = list(map(int, input().strip().split()))

    answer = 0
    maxn = l[n-1]
    for j in range(n-1, -1, -1):
        if l[j] < maxn:
            answer += maxn-l[j]
        else:
            maxn = l[j]

    print(answer)