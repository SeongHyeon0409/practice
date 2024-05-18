t = int(input())

def dfs(s, d):
    global n

    for i in range(d, n):
        s += sc[i]
        dfs(s, i+1)
        s -= sc[i]

    v[s] = 1


for tc in range(1, t+1):
    n = int(input())
    sc = list(map(int, input().split()))
    v = [1] + [0] * sum(sc)
    ans = [0]

    for s in sc:
        for i in range(len(ans)):
            if v[ans[i] + s] == 0:
                v[ans[i] + s] = 1
                ans.append(ans[i] + s)


    print(f'#{tc} {sum(v)}')

