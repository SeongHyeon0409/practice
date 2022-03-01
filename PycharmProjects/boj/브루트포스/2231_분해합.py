def d(n):
    a = n
    while True:
        b = n%10
        a += b
        n = n//10
        if n<10:
            a += n
            break
    return a

N = int(input())
answer = []

for i in range(N):
    if d(i) == N:
        answer.append(i)

if answer:
    print(min(answer))
else:
    print(0)
