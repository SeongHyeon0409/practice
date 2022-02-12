n = int(input())
answer = n
count = 0

while True:
    a = answer // 10
    b = answer % 10
    c = a + b % 10
    answer = b * 10 + c
    count += 1
    if n != answer:
        continue
    break

print(count)