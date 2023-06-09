t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    dp = [0] * (n+1)
    dp[0] = 1
    for i in range(1, n + 1):
        temp = (i - m) // 2

        if i <= m and i % 2 != 0:
            dp[i] = 1
        else:
            dp[i] = (dp[i-m] * dp[m])
            if i % 2 == 0 and i-m != i//2:
                dp[i] += dp[i // 2] * dp[i // 2]
            if (m % 2 == 0 and i % 2 == 0):
                if i - m != i - temp  and i - m != temp and m != i -temp:
                    dp[i] += + dp[i - temp] * dp[temp]
            elif (m % 2 != 0 and i % 2 != 0):
                if i - m != i - temp  and i - m != temp and m != i -temp:
                    dp[i] += + dp[i - temp] * dp[temp]

        dp[i] %= 10007
    # 1 1 1 1 2 3 1 5
    # print(dp)
    print(dp[i])