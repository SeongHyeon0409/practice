n = int(input())
if n == 0:
    print(0)
else:
    ans = ''
    while n:
        print(n)
        ans += str(n%2)
        n//=2
        n*=-1
    print(ans[::-1])