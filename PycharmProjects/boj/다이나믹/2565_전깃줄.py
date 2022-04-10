# 2020.04.10
# Presented by SeongHyeon0409

n = int(input())

l = sorted([list(map(int, input().split())) for _ in range(n)])

dp = [1] * n

for i in range(n):
    for j in range(i): #안겹치는 줄을 찾기위해 두번째 전봇대의 lis를 구해준다.
        if l[i][1] > l[j][1]:
            dp[i] = max(dp[j] + 1, dp[i])

print(n - max(dp)) #전체 전깃줄 개수 - 안겹치는 전깃줄 = 최소 없애야 하는 전깃줄