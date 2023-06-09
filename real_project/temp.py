t = int(input())

for _ in range(t):
    n = int(input())
    stock = list(map(int, input().split()))
    stock.reverse()

    # 4 5 9
    # 4 7 9 7 3 3
    maxv = stock[0]
    ans = 0
    for i in range(1, len(stock)):
        if stock[i] > maxv:
            maxv = stock[i]
        else:
            ans += maxv - stock[i]

    print(ans)