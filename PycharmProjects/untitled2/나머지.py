data = []
for i in range(0,10):
    dat = int(input())
    data.append(dat)

tp = []

for i in data:
    a = i % 42
    if a not in tp:
        tp.append(a)

print(len(tp))