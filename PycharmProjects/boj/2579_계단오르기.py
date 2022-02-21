n = int(input())
s = [int(input()) for i in range(n)]
#print(s)

dp = [0] * n
dp[0] = s[0]


flag = [1] * n
#print(dp)
if n == 1:
    print(dp[0])
elif n == 2:
    dp[1] = dp[0] + s[1]
    print(dp[1])
else:
    dp[1] = dp[0] + s[1]
    dp[2] = max(s[2] + s[1], s[0] + s[2])
    for i in range(3, n):


        dp[i] = s[i] + max(s[i-1] + dp[i-3], dp[i-2])

        #print("n :", i+1 , " , flag :", flag)
    #print(dp)
    print(dp[n-1])