n, k = map(int, input().split(" "))
coin = [ int(input()) for i in range(n)]
temp = [0] * (k+1)
for i in range(coin[0]-1, k+1):
    temp[i] = coin[0]

dp = temp[:]


for i in range(1, n): # 1
    for j in range(k+1): # 1
        if j - coin[i] >= 0: # coin[1] > 2
            dp[j] = temp[j] + dp[j-coin[i]]

    temp = dp[:]

print(temp[k])



