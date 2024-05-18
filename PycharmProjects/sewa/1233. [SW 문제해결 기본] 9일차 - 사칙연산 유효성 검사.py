# in order : left root right

def dfs(i):
    global ans
    a = words[i][0]
    if a.isdigit():
        return int(a)
    if words[i][1] == 0 and words[i][2] == 0:
        print(a, words[i][1], words[i][2])
        ans = 0
        return 0

    li, ri = int(words[i][1]), int(words[i][2])
    op = dfs(li) + dfs(ri)


    return int(op)


for tc in range(1, 11):
    n = int(input())
    words = [[0, 0, 0] for i in range(n+1)]
    ans = 1
    for i in range(n):
        tmp = list(input().split())
        idx, w = int(tmp[0]), tmp[1]
        words[idx][0] = w
        if not w.isdigit() and len(tmp) < 3:
            ans = 0
        if len(tmp) > 2:
            words[idx][1] = tmp[2]
        if len(tmp) > 3:
            words[idx][2] = tmp[3]

    print(f'#{tc} {ans}')




