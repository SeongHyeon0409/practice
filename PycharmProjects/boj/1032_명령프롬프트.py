n = int(input())
file_name = [input() for i in range(n)]

answer = file_name[0]

for i in range(1, n):
    for j in range(len(answer)):
        if answer[j] != file_name[i][j]:
            answer = list(answer)
            answer[j] = '?'
            answer = "".join(answer)
print(answer)

