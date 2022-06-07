# 2020.06.07
# Presented by SeongHyeon0409

words = [input() for _ in range(5)]

for j in range(15):
    for i in range(5):
        if len(words[i]) < j+1:
            continue
        print(words[i][j], end='')