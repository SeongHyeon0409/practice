def printl(list):
    for i in range(len(list)):
        print(*list[i])

t = int(input())

for i in range(t):
    n = int(input())
    s = []
    for j in range(2):
        s.append(list(map(int, input().split())))

    #printl(s)

    dp = [([0] * (n+1)) for _ in range(2)]

    dp[0][0] = s[0][0]
    dp[1][0] = s[1][0]
    
    if n > 1:
        dp[0][1] = dp[1][0] + s[0][1]
        dp[1][1] = dp[0][0] + s[1][1]

    for j in range(2, n):
        dp[0][j] = max(s[0][j] + dp[1][j-1], s[0][j] + dp[1][j-2])
        dp[1][j] = max(s[1][j] + dp[0][j-1], s[1][j] + dp[0][j-2])

    #printl(dp)
    #print("-------------------------")

    print(max(dp[0][n-1], dp[1][n-1]))