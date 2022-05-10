# 2020.05.10
# Presented by SeongHyeon0409

n = int(input())

for i in range(1, n+1):
    print((' ' * (n - i)) + ('*' * ( i * 2 - 1)) )
