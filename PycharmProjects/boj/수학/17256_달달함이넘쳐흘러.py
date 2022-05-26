# 2020.05.26
# Presented by SeongHyeon0409

a = list(map(int, input().split()))
b = list(map(int, input().split()))

print("{0} {1} {2}".format(b[0] - a[2], b[1] // a[1], b[2] - a[0]))