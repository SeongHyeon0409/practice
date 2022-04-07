# 2020.04.08
# Presented by SeongHyeon0409

n = int(input())
cards = list(map(int, input().split()))

dp = [0]

for i in range(n):
    dp.append(cards[i])

for i in range(1, n+1):
    for j in range(i+1):
        dp[i] = min(dp[i], dp[i-j] + dp[j])

print(dp[-1])