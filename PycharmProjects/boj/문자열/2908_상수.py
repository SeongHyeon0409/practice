a, b = input().split()
c = ""
d = ""
for i in range(3):
    c += a[2-i]
    d += b[2-i]

print(max(int(c), int(d)))

