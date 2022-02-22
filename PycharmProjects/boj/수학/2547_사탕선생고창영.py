n = int(input())
answer = []

for i in range(0, n):
    a = input()
    sn = int(input())
    sum = 0
    for j in range(0, sn):
        c = int(input())
        sum += c
    if (sum % sn) == 0:
        answer.append('YES')
    else:
        answer.append('NO')


for i in answer:
    print(i)