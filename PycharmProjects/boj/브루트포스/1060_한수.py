#한수 = 123, 147, 357
N = int(input())
answer = 0

for i in range(1, N+1):
    stri = list(map(int, str(i)))
    if i < 100:
        answer += 1
    elif stri[0]-stri[1] == stri[1]-stri[2]:
        answer += 1

print(answer)
