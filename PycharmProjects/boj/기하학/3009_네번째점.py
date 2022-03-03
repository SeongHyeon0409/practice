x = []
y = []
for i in range(3):
    x1, y1 = map(int, input().split())
    x.append(x1)
    y.append(y1)


for i in range(3):
    if x.count(x[i]) == 1:
        x1 = x[i]
    if y.count(y[i]) == 1:
        y1 = y[i]

print(x1, y1)



