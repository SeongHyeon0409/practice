# 2020.06.07
# Presented by SeongHyeon0409

word = input()

for i in word:
    if 65 <= ord(i) <= 77:
        print(chr(ord(i)+13), end='')
    elif 78 <= ord(i) <= 96:
        print(chr(ord(i)-13), end='')
    elif 97 <= ord(i) <= 109:
        print(chr(ord(i)+13), end='')
    elif 110 <= ord(i) <= 122:
        print(chr(ord(i)-13), end='')
    else:
        print(i, end='')


