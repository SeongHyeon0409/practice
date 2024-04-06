def dfs(idx):
    if len(box) == 6:
        print(*box)
        return

    for i in range(idx, len(nums)):
        box.append(nums[i])
        dfs(i+1)
        box.pop()



while True:
    nums = list(map(int, input().split()))
    visited = [0] * (len(nums))
    if nums[0] == 0:
        break
    nums = nums[1:]
    box = []
    dfs(0)
    print()

