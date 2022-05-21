# 2020.05.21
# Presented by SeongHyeon0409

n = int(input())

for i in range(n-1, -1, -1):
    print(' ' * (n-i-1) + ('*' * (i*2)) + '*')