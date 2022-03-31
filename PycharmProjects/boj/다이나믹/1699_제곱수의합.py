n = int(input())
a = 1
dp = [0] * (n+1)
mult = []

while a*a <= n:
    mult.append(a*a)
    a += 1

for i in range(1, n+1):
    temp = []
    for j in mult:
        if j > i:
            break
        temp.append(dp[i-j] + 1)
    dp[i] = min(temp)

print(dp[n])

