# in order : left root right

def dfs(i):
    global ans
    if int(words[i][1]) != 0:
        dfs(int(words[i][1]))

    ans += words[i][0]

    if int(words[i][2]) != 0:
        dfs(int(words[i][2]))


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


    # start = words[1]
    # while True:
    #     if start[1] != 0:
    #         start = words[int(start[1])]
    #     else:
    #         break
    ans = ''
    dfs(1)

    print(f'#{tc} {ans}')




