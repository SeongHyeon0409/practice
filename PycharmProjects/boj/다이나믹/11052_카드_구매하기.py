n = int(input())
cards = list(map(int, input().split()))

dp = [0]
for i in range(n):
    dp.append(cards[i])


for i in range(1, n+1):
    for j in range(i, -1, -1):
        dp[i] = max(dp[i], dp[i-j] + dp[j])

#print(dp)
print(dp[-1])


n = int(input())
card = [0] + list(map(int, input().split()))
dp = card[:]

for i in range(2, n+1):
    for j in range(1, i):
        dp[i] = max(dp[i], dp[i-j] + dp[j])

print(dp[n])