# 2020.04.08
# Presented by SeongHyeon0409

def koong(n):
    if dp[n] != 0:
        return dp[n]
    elif n < 2:
        return 1
    elif n == 2:
        return 2
    elif n == 3:
        return 4
    else:
        dp[n] = koong(n-1) + koong(n-2) + koong(n-3) + koong(n-4)
        return dp[n]

t = int(input())

dp = [0] * 70

for i in range(t):
    n = int(input())
    print(koong(n))