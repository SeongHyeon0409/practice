A, B = map(int, input().split())
answer = 1

while A < B:
    if B % 10 == 1:
        B //= 10
        answer += 1
    elif B % 2 == 0:
        B //= 2
        answer += 1
    else:
        answer = -1
        break

    if B < A:
        answer = -1

print(answer)