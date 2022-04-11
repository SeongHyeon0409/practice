# 2020.04.11
# Presented by SeongHyeon0409

n = int(input())

map = [ list(map(int, input())) for _ in range(n)]

def dsf(i, j, label):
    global count
    if map[i][j] == 1:
        map[i][j] = label
        count += 1
        if j < n-1:
            dsf(i, j+1, label)
        if i > 0:
            dsf(i-1, j, label)
        if j > 0:
            dsf(i, j-1, label)
        if i < n-1:
            dsf(i+1, j, label)
    return count

label = 2
ans = []

for i in range(n):
    for j in range(n):
        count = 0
        if map[i][j] == 1:
            dsf(i, j, label)
            ans.append(count)
            label += 1

print(label-2)
print(*sorted(ans), sep='\n')
