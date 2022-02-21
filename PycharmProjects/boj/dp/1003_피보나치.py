n = int(input())

for i in range(n):
    num = int(input())
    dp = [[0, 0] for i in range(num+2)]
    dp[0] = [1, 0]
    dp[1] = [0, 1]

    for i in range(2, num+1):
        dp[i][0] = dp[i-1][0] + dp[i-2][0]
        dp[i][1] = dp[i-1][1] + dp[i-2][1]

    print("{0} {1}".format(dp[num][0], dp[num][1]))