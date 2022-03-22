n = int(input())
l = [int(input()) for _ in range(n)]
answer = 0
for i in range(n-2, -1, -1):
    if l[i] >= l[i+1]:
        temp = l[i]
        l[i] = l[i+1] - 1
        answer += temp - l[i]

print(answer)