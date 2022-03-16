n = 1000 - int(input())

a = [500, 100, 50, 10, 5, 1]
answer = 0

for i in a:
    while n >= i:
        n -= i
        answer += 1

print(answer)