n, m = map(int, input().split())
j = int(input())

apples = [int(input()) for _ in range(j)]
answer = 0
np = 1

for i in range(j):
    if apples[i] < np:
        answer += np-apples[i]
        np = apples[i]
    else:
        temp = apples[i] - np - (m - 1)
        if temp > 0:
            answer += temp
            np = apples[i] - (m - 1)

print(answer)