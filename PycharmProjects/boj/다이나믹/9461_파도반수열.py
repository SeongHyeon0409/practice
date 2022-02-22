
t = int(input())

for i in range(t):
    n = int(input())
    dp = [1, 1, 1, 2, 2] + ([0] * (n-5))
    #print(dp)
    for j in range(5, n):
        dp[j] = dp[j-1] + dp[j-5]

    print(dp[n-1])