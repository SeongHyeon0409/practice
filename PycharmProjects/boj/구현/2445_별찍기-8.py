# 2020.05.10
# Presented by SeongHyeon0409

n = int(input())

for i in range(1, n):
    print('*' * i + ' ' * (n-i) * 2 + '*' * i)
for i in range(n, 0, -1):
    print('*' * i + ' ' * (n-i) * 2 + '*' * i)
