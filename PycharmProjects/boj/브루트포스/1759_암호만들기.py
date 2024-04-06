l, c = map(int, input().split())
words = sorted(list(input().split()))
visited = {}
m = ['a', 'e', 'i', 'u', 'o']
for i in range(c):
    visited[words[i]] = False
# 최소 한 개의 모음, 최소 두 개의 자음
def check(arr):
    v, c = 0, 0
    for i in arr:
        if i in m:
            v += 1
        else:
            c += 1

    return True if (v > 0 and c > 1) else False
def dfs(d):
    if len(box) == l:
        if check(box):
            print(''.join(box))

        return

    for i in range(d, c):
        if visited[words[i]] == False:
            visited[words[i]] = True

            box.append(words[i])
            dfs(i+1)
            box.pop()

            visited[words[i]] = False

box = []
mn = [0, 0]
dfs(0)

