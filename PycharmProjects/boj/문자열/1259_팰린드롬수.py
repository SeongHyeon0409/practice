# 2020.04.13
# Presented by SeongHyeon0409

while True:
    n = input()
    if n == '0':
        break

    if len(n) % 2 == 0:
        if n[:len(n)//2] == n[len(n)//2:][::-1]:
            print('yes')
        else:
            print('no')
    else:
        if n[:len(n)//2] == n[len(n)//2 + 1:][::-1]:
            print('yes')
        else:
            print('no')
