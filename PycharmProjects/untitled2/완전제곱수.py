minv = int(input())
maxv = int(input())
answer = []

for i in range(minv, maxv + 1):
    for j in range(i+1):
        if j*j == i:
            answer.append(i)
        if j*j > i:
            break

if answer:
    print(sum(answer))
    print(min(answer))
else:
    print(-1)