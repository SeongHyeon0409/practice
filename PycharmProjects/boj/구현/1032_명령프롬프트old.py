n = int(input())
temp = [input() for i in range(n)]

a = temp[0]

for i in temp:
    answer = ""
    for j in range(len(a)):
        if a[j] == i[j]:
            if a[j] == '?':
                answer += '?'
            else:
                answer += i[j]
        else:
            answer += '?'
    a = answer

print(answer)
