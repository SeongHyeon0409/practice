n = int(input())
l = sorted([int(input()) for _ in range(n)], reverse=True)
a = 0
answer = 0
for i in l:
    temp = i-a
    if temp > 0:
        answer += temp
    a += 1

print(answer)