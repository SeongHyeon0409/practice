def dfs():
    if len(box) == 2:
        ans.append(box[:])
        return

    for i in range(n):
        box.append(nums[i])
        dfs()
        box.pop()


t = int(input())

for tc in range(1, t+1):
    n, k = map(int, input().split())
    nums = list(map(int, input().split()))

    box = []
    ans = []

    dfs()
    ans.sort()
    print(ans)
    print(f'#{tc} {sum(ans[k-1])}')

    # 2 3 3