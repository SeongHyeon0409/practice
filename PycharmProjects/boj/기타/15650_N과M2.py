# 백트래킹은 모든 가능한 경우의 수 중에서 특정한 조건을 만족하는 경우만 살펴보는 것

n, m = map(int,input().split())

s = []

def dfs(start):
    if len(s) == m:
        print(' '.join(map(str, s)))
        return

    for i in range(start, n+1):
        if i in s :
            continue
        #if len(s) > 0 and i < s[len(s) - 1]:
            #continue
        s.append(i)
        dfs(i+1)
        s.pop()

dfs(1)