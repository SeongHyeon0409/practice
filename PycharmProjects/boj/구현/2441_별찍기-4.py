# 2020.04.25
# Presented by SeongHyeon0409

n = int(input())

for i in range(n, -1, -1):
    print(' ' * (n-i) + '*' * i)