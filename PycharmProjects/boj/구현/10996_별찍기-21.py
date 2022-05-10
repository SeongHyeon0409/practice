# 2020.05.10
# Presented by SeongHyeon0409

n = int(input())

for i in range(n):
    if n % 2 != 0:
        print('* ' * (n // 2 + 1))
    else:
        print('* ' * (n // 2))
    print(' *' * (n // 2))