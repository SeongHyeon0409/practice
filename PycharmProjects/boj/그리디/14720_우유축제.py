n = int(input())

l = list(map(int, input().split()))

a = [0, 1, 2]
b = 0
answer = 0

for i in range(n):
    if a[b] == l[i]:
        answer += 1
        b += 1
        if b == 3:
            b = 0

print(answer)