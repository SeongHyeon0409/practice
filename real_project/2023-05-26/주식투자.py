T = int(input())

for _ in range(T):
    n = int(input())
    prices = list((map(int, input().split())))
    prices.reverse()

    max_v = prices[0]
    ans = 0
    for i in range(1, len(prices)):
        if prices[i] < max_v:
            ans += max_v - prices[i]
        else:
            max_v = prices[i]

    print(ans)