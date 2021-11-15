def solution(c, coins):
    dp = [0] * (c + 1)
    dp[0] = 1

    for i in coins:
        for j in range(i, c + 1):
            dp[j] = dp[j] + dp[j-i]

    print(dp[c])

if __name__ == "__main__" :
    n = int(input())

    for i in range(n):
        c = int(input())
        coins = list(map(int, input().strip().split(" ")))[1:]

        solution(c, coins)