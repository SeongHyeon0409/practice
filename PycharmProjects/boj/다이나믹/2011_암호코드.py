n = '0' + input()
dp = [1, 1] + [0] * (len(n)-2)

if n[1] == '0':
    print(0)
    exit()

for i in range(2, len(n)):
    if 0 < int(n[i]):
        dp[i] += dp[i-1]

    if 10 <= int(n[i-1:i+1]) <= 26:
        dp[i] += dp[i-2]

    dp[i] %= 1000000
print(dp[len(n)-1])