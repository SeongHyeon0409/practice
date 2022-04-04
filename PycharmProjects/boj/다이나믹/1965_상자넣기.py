# 2020.04.04
# Presented by SeongHyeon0409

n = int(input())
num = list(map(int, input().split()))

dp = [1] * n

for i in range(1, n):
    for j in range(0, i):
        if num[i] > num[j]:
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))