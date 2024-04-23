n = int(input())
nums = list(map(int, input().split()))
ans = set()
tmp = 0

def dfs(d, idx):
    global ans, tmp

    ans.add(tmp)

    if d == n:
        return

    for i in range(idx, n):
        tmp += nums[i]
        dfs(d+1, i+1)
        tmp -= nums[i]


dfs(0, 0)
ans = sorted(list(ans))

i = 1
while True:
    try:
        if ans[i] == i:
            i += 1
        else:
            print(i)
            break
    except:
        print(i)
        break

