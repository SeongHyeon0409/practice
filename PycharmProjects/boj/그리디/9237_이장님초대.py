n = int(input())
l = list(map(int, input().split()))
l.sort(reverse=True)

answer = l[0]+1

a = l[0]-1

for i in range(1, n):
    if a < l[i]:
        answer += max(l[i] - a, 1)
        a = l[i]
    a -= 1

print(answer+1)
