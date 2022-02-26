t = int(input())
for i in range(t):
    n, w = input().strip().split()
    n = int(n)
    w = list(w)
    for j in w:
        print(j * n, end='')
    print()