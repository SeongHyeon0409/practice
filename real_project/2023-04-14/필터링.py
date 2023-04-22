import re

t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    slang = list(input().split())
    words = input().split()
    answer = []

    for i in range(len(words)):
        word = words[i]
        regex = word.replace('.', '[a-z]{1,%d}' % m)
        flag = 0
        for j in slang:
            if re.fullmatch(regex, j):
                answer.append('#' * len(word))
                flag = 1
                break
        if flag == 0:
            answer.append(word)


    print(' '.join(answer))




