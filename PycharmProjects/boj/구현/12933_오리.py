q = input()
n = len(q)
quack = 'quack'

def check(s):
    global count
    i = 0
    first = 1
    for j in range(s, n):
        if q[j] == quack[i] and visited[j] == 0:
            visited[j] = 1
            i += 1

            if q[j] == 'k':
                if first:
                    count += 1
                    first = 0
                i = 0


count = 0
visited = [0] * n

if n % 5 != 0:
    print(-1)
    exit()

for i in range(n):
    check(i)

if count == 0 or not all(visited):
    print(-1)
else:
    print(count)

