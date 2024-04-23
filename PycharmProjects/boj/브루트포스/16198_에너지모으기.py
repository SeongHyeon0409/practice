n= int(input())
nums = list(map(int, input().split()))


def dfs(n, sums, arr):
    global ans
    if n == 2:
        ans = max(sums, ans)
        return

    for i in range(1, n-1):
        tmp = arr[:]
        sums += arr[i-1] * arr[i+1]
        del tmp[i]

        dfs(n-1, sums, tmp)
        sums -= arr[i-1] * arr[i+1]

ans = 0
dfs(n, 0, nums)
print(ans)

