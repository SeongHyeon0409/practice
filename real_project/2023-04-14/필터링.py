import re

t = int(input())


for _ in range(t):
    n, m = map(int, input().split())
    slang = list(input().split())
    words = input().split()
    answer = []

    for i in range(len(words)):
        word = words[i]
        for j in slang:
            if word == j:
                words[i] = '#' * len(word)
            else:
                regex = word.replace('.', '[a-z]{1,%d}' % m)
                if re.fullmatch(regex, j):
                    words[i] = '#' * len(word)

    print(' '.join(words))




