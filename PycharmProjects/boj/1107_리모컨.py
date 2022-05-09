# 2020.05.09
# Presented by SeongHyeon0409

n = input()
m = int(input())
b = []

if m != 0:
    b = list(map(int, input().split()))

abc = set([0, 1, 2 ,3 ,4 ,5 ,6 ,7 ,8, 9]) - set(b)

ans = []
ans2 = []
i = 0

while True:
    temp = 10
    temp2 = 0
    flag = 0

    for j in abc:
        if abs(int(n[i]) - j) < temp:
            temp = abs(int(n[i]) - j)
            temp2 = j
        elif abs(int(n[i]) - j) == temp:
            ans2.append(str(j))
            flag = 1

    ans.append(str(temp2))

    if not flag:
        ans2.append('-1')

    if n[i] != ans[i]:
        break
    i += 1
    if i >= len(n):
        break

answer = ''
answer2 = ''

for i in range(len(ans)):
    answer += ans[i]
    if ans2[i] == '-1':
        answer2 += ans[i]
    else:
        answer2 += ans2[i]

if int(ans[len(ans) - 1]) > int(n[len(ans) - 1]):
    for i in range(len(ans), len(n)):
        answer += (str(min(abc)))
else:
    for i in range(len(ans), len(n)):
        answer += (str(max(abc)))

if int(ans2[len(ans2) - 1]) > int(n[len(ans2) - 1]):
    for i in range(len(ans2), len(n)):
        answer2 += (str(min(abc)))
else:
    for i in range(len(ans2), len(n)):
        answer2 += (str(max(abc)))

if abs(int(n) - int(answer)) < abs(int(n) - int(answer2)):
    answer = int(answer)
else:
    answer = int(answer2)

if 1 not in b:
    answer2 = '1'
    for i in range(len(n)):
        answer2 += str(min(abc))

if abs(int(n) - int(answer)) <= abs(int(n) - int(answer2)):
    answer = int(answer)
else:
    answer = int(answer2)

if answer >= 10 and abs(int(n) - answer // 10) <= abs(int(n) - answer):
    answer = answer // 10
    # 0 - 0

# print(answer)
if abs(int(n) - 100) <= len(str(answer)) + abs(int(n) - answer):
    answer = abs(int(n) - 100)
else:
    answer = len(str(answer)) + abs(int(n) - answer)

print(answer)