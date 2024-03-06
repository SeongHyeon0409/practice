import sys

# 1. 같은 row에 있는지 확인
# 2. 대각에 있는지 확인
# 4. n번째인지 확인

answer = 0
def dfs(s):
    global answer
    if s == n:
        answer += 1
        return

    for i in range(n):
        a[s] = i
        flag = 1
        for j in range(s): #자기 자리하고 그전값들 비교
            if a[j] == a[s] or abs(a[j] - a[s]) == abs(j - s):
                flag = 0
                break
        if flag: dfs(s+1)


if __name__ == '__main__':


    n = int(sys.stdin.readline())
    a = [0] * n

    dfs(0)
    print(answer)

