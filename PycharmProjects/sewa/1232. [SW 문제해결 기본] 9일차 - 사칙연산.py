# in order : left root right

def dfs(i):
    a = words[i][0]
    if a.isdigit():
        return int(a)

    else:
        li, ri = int(words[i][1]), int(words[i][2])
        if a == '*':
            op = dfs(li) * dfs(ri)
        elif a == '/':
            op = dfs(li) / dfs(ri)
        elif a == '+':
            op = dfs(li) + dfs(ri)
        elif a == '-':
            op = dfs(li) - dfs(ri)

    return int(op)


for tc in range(1, 11):
    n = int(input())
    words = [[0, 0, 0] for i in range(n+1)]
    for i in range(n):
        tmp = list(input().split())
        idx, w = int(tmp[0]), tmp[1]
        words[idx][0] = w
        if len(tmp) > 2:
            words[idx][1] = tmp[2]
        if len(tmp) > 3:
            words[idx][2] = tmp[3]

    ans = int(dfs(1))

    print(f'#{tc} {ans}')




