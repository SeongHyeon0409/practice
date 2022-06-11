# 2020.06.11
# Presented by SeongHyeon0409

a, b = input().split()

# 제일 많이 겹치는걸 찾아야함

ans = []

for i in range(len(b) - len(a) + 1):
    count = 0
    for j in range(len(a)):
        if a[j] != b[i + j]:
            count += 1
    ans.append(count)

print(min(ans))