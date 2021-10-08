n = int(input())
tp = []
for i in range(n):
    cent = int(input())
    tp.append(cent)


for i in tp:
    a = i // 25
    b = i % 25
    print(a, end=" ")

    c = b // 10
    d = b % 10
    print(c, end=" ")

    e = d // 5
    f = d % 5
    print(e, f)
