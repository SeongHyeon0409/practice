from collections import deque
import sys
input = sys.stdin.readline

def moveR(N):
    return N//10+(N%10)*1000

def moveL(N):
    return 10*N+(N//1000)

def mult(n):
    return (n * 2) % 10000

def mOne(n):
    if n == 0:
        return 9999
    return n - 1

T = int(input())

for _ in range(T):
    a, b = map(int, input().split())

    visit = [False] * 10000
    q = deque()
    path = ""
    q.append((a, path))


    while q:
        N, path = q.popleft()
        visit[N] = True
        if N == b:
            print(path)
            break

        n = mult(N) % 10000
        if not visit[n]:
            q.append((n, path + "D"))
            visit[n] = True

        n = mOne(N) % 10000
        if not visit[n]:
            q.append((n, path + "S"))
            visit[n] = True

        n = (10*N+(N//1000))%10000
        if not visit[n]:
            q.append((n, path + "L"))
            visit[n] = True

        n = (N//10+(N%10)*1000)%10000
        if not visit[n]:
            q.append((n, path + "R"))
            visit[n] = True
