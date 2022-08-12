# 2020.06.13
# Presented by SeongHyeon0409
# 배낭 문제

n = int(input())
L = [0] + list(map(int, input().split()))
J = [0] + list(map(int, input().split()))

dp = [[0] * 101 for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(1, 101):
        if L[i] <= j: #배낭에 넣을 수 있다면
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-L[i]] + J[i])
            print(dp[i-1][j-L[i]])
        else:
            dp[i][j] = dp[i-1][j]

print(dp[n][99])
