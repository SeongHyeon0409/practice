t = int(input())

for _ in range(t):
    n, p = map(int, input().split())
    if n%2==0:
        if p%2==0:
            print(n//2+1)
        else:
            print(n//2)
    else:
        print(n//2+1)
