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

# - --------------------

t = int(input())

for _ in range(t):
    n = int(input())
    s1 = list(map(int, input().split()))
    s2 = list(map(int, input().split()))

    dp = [[0] * n for _ in range(3)]

    # 선택 x , 1번 선택, 2번 선택
    dp[1][0] = s1[0]
    dp[2][0] = s2[0]
    for i in range(1, n):
        dp[0][i] = max(dp[1][i-1], dp[2][i-1])
        dp[1][i] = max(dp[0][i-1] + s1[i], dp[2][i-1] + s1[i])
        dp[2][i] = max(dp[0][i-1] + s2[i], dp[1][i-1] + s2[i])

    print(max(dp[0][n-1], dp[1][n-1], dp[2][n-1]))


