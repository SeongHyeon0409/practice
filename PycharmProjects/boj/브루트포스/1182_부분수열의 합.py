n, s = map(int, input().split())
nums = list(map(int, input().split()))
ans = 0
tmp = 0

def dfs(d, idx):
    global ans, tmp
    if tmp == s:
        ans += 1
    if d == n:
        return

    for i in range(idx, n):
        tmp += nums[i]
        dfs(d+1, i+1)
        tmp -= nums[i]

dfs(0, 0)
if s == 0:
    ans -= 1
print(ans)

