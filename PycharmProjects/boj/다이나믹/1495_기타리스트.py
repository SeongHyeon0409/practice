# 2020.04.06
# Presented by SeongHyeon0409

n, s, m = map(int, input().split())
v = list(map(int, input().split()))

dp = [[0] * (m+1) for i in range(n+1)] # 0 ~ m 까지 볼륨의 가능성을 n개의 곡에 각각 저장
dp[0][s] = 1
flag = 0 #마지막 곡을 연주할 수 없으면 1

for i in range(n):
    for j in range(0, m+1):
        if dp[i][j] == 1:
            if j-v[i] > -1:
                dp[i+1][j-v[i]] = 1
            if j+v[i] < m+1:
                dp[i+1][j+v[i]] = 1

ans = -1

for i in range(m, -1, -1):
    if dp[n][i] == 1:
        ans = i
        break

print(ans)