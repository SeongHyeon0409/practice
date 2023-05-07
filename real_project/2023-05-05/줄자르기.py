t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    # 1 if n = 1 or n < m (홀수)
    dp = [0] * (n+1)
    dp[0] = 1
    for i in range(1, n+1):
        q = (i - m)//2 # 1 if m이 홀수 일경우 = n이 홀수
        #if m이 짝수일경우 m이 짝수일경우만 ,

        if i <= m and i % 2 != 0:
            dp[i] = 1
        else:
            dp[i] = (dp[i-m] * dp[m])
            #print("dpi1", i, (dp[i-m] * dp[m]))
            if i % 2 == 0 and i-m != i//2:
                dp[i] += dp[i // 2] * dp[i // 2]
                #print("dpi:", i, dp[i // 2] ** 2)
            if (m % 2 == 0 and i % 2 == 0):
                if i - m != i - q and m != q and i - m != q and m != i -q:
                    dp[i] += + dp[i-q] * dp[q]
            elif (m % 2 != 0 and i % 2 != 0):
                if i - m != i - q and m != q and i - m != q and m != i -q:
                    dp[i] += + dp[i-q] * dp[q]

        dp[i] %= 10007
        #print(i, dp[i])
    #print(dp)

    print(dp[i])