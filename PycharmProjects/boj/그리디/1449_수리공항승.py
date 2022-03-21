n, l = map(int, input().split())
t = sorted(list(map(int, input().split())))

answer = 1
a = t[0]

for i in range(1, n):
    if t[i] >= a+l:
        answer += 1
        a = t[i]

print(answer)