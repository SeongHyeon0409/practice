n, k = map(int, input().split())
c = sorted([int(input()) for _ in range(n)])

dp = [0] * (k+1)

for i in c:
    if i <= k:
        dp[i] = 1

for i in range(1, k+1):
    if dp[i] == 1:
        continue
    temp = []
    for j in c:
        if j > i:
            break
        if dp[i-j] > 0:
            temp.append(dp[i-j])

    if temp:
        dp[i] = min(temp) + 1


if dp[k]:
    print(dp[k])
else:
    print(-1)