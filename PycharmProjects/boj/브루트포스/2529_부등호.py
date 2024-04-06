n = int(input())
arr = list(input().split())
visited = [0] * 10

box = []
minv, maxv = float('inf'), float('-inf')
def dfs(d):
    global minv, maxv
    if d == n:
        value = int(''.join(map(str, box)))
        minv = min(minv, value)
        maxv = max(maxv, value)
        return

    for i in range(0, 10):
        flag = 0
        if arr[d] == '<':
            if box[-1] < i and visited[i] == 0:
                box.append(i)
                visited[i] = 1
                flag = 1
                dfs(d+1)
        elif arr[d] == '>':
            if box[-1] > i and visited[i] == 0:
                box.append(i)
                visited[i] = 1
                flag = 1
                dfs(d+1)
        if flag:
            box.pop()
            visited[i] = 0


for i in range(0, 10):
    visited[i] = 1
    box.append(i)
    dfs(0)
    visited[i] = 0
    box.pop()
if len(str(minv)) < n+1:
    minv = '0'* (n+1 - len(str(minv))) + str(minv)
print(maxv)
print(minv)