t = int(input())

for i in range(t):
    n = int(input())

    dp = [1, 1]
    a = 0
    i = 2
    while True:
        a = dp[i - 1] + dp[i - 2]
        if a > n:
            break
        dp.append(a)
        i += 1

    temp = n
    ans = []

    for j in reversed(dp):
        if j <= temp:
            ans.append(j)
            temp -= j

    if temp == 0:
        print(*reversed(ans))
    else:
        print(-1)


