n = int(input())
a = sorted(list(map(int, input().split())))
b = sorted(list(map(int, input().split())), reverse=True)

answer = 0
for i in range(n):
    answer += a[i] * b[i]

print(answer)

