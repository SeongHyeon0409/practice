# 2023.03.17
# Written by SeongHyeon0409

t = int(input())

for _ in range(t):
    n = int(input())
    construct = list(map(int, input().split()))
    construct.reverse()
    answer = 1
    minv = construct[0]
    for i in range(1, n):
        if construct[i] > minv:
            answer += 1
            minv = construct[i]

    print(answer)


