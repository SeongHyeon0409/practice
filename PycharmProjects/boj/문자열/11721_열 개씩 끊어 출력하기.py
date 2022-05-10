# 2020.05.10
# Presented by SeongHyeon0409

word = input()

print(word[0], end='')

for i in range(1, len(word)):
    if i % 10 == 0:
        print('\n', word[i], end='' , sep='')
    else:
        print(word[i], end='')