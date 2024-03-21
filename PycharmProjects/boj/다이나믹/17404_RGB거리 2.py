n = int(input())
house = [[-1, -1, -1]]
for i in range(n):
    house.append(list((map(int,input().split(" ")))))

R, G, B = 0, 1, 2
INF = float('inf')

dp = [[-1] * 3 for _ in range(n+1)]
dp[1] = house[1]
answer = INF

for color in [R,G,B]:
    dp = [[-1]*3 for _ in range(n+1)]

    dp[1] = [INF, INF, INF]
    dp[1][color] = house[1][color]

    for i in range(2, n+1):
        dp[i][R] = min(dp[i-1][G], dp[i-1][B]) + house[i][R]
        dp[i][G] = min(dp[i-1][R], dp[i-1][B]) + house[i][G]
        dp[i][B] = min(dp[i-1][R], dp[i-1][G]) + house[i][B]
    dp[n][color] = INF
    answer = min(answer, min(dp[n]))
print(answer)