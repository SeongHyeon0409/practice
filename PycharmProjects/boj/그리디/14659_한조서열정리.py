n = int(input())
a = list(map(int, input().split()))

count = 0
h = a[0]
maxc = 0

for i in range(1, n):
    if h > a[i]:
        count += 1
        if count > maxc:
            maxc = count
    else:
        h = a[i]
        count = 0

print(maxc)