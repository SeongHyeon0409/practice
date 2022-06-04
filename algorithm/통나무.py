def solution(l, c ,lo):
    dp = [[0] * (l+1) for i in range(l+1)]
    for i in range(c-1, -1, -1):
        for j in range(i+2, c+2):
            temp = 9999999;
            for k in range(i+1, j):
                temp = min(temp, dp[i][k]+dp[k][j]+lo[j]-lo[i]);
            dp[i][j] = temp
    print (dp[0][c+1])


if __name__ == "__main__" :
    n = int(input())

    for i in range(n):
        l, c = map(int, input().strip().split(" "))
        lo = list(map(int, input().strip().split(" ")))
        lo = [0] + lo + [l]

        solution(l, c, lo)
