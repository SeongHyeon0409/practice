T = int(input())

for i in range(T):
    k = int(input())
    n = int(input())

    dp = [[0]*n for _ in range(k+1)]

    dp[0] = [j for j in range(1, n+1)]

    for j in range(1, k+1):
        dp[j][0] = 1
        for l in range(1, n):
            dp[j][l] = dp[j][l-1] + dp[j-1][l]

    print(dp[k][n-1])



