t = int(input())

def dfs(s, d):
    # 마지막이어야 리턴;;해야함;;ㅇㅈ?
    global n

    for i in range(d, n):
        s += sc[i]
        dfs(s, i+1)
        s -= sc[i]

    v[s] = 1


for tc in range(1, t+1):
    n = int(input())
    sc = list(map(int, input().split()))
    v = [0] * (sum(sc) + 1)
    dfs(0, 0)
    print(f'#{tc} {sum(v)}')

