n = int(input())

word = input()

answer = 0

for i in range(n-1):
    word2 = input()
    temp = list(word)
    count = 0
    for j in word2:
        if j in temp:
            temp.remove(j)
        else:
            count += 1

    if len(temp) > 1:
        continue

    if count < 2:
        answer += 1


print(answer)