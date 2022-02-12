word = input()
answer = []

for i in range(97, 123):
    flag = 0
    for j in range(0,len(word)):
        if word[j] == chr(i) and flag == 0:
            answer.append(j)
            flag = 1
    if flag == 0:
        answer.append(-1)

for i in answer:
    print(i,end=' ')
