x = int(input())

line = 0
n = 0

while x > n:
    line += 1
    n += line

idx = x - (n-line)

if line%2 == 0: #짝수
    top = 1 + (idx - 1)
    bottom = line - (idx - 1)
else: #홀수
    top = line-(idx-1)
    bottom = 1 + (idx - 1)

print("{0}/{1}".format(top, bottom))