# 2020.05.09
# Presented by SeongHyeon0409
# 시팔

target = int(input())
ans = abs(100 - target) # ++ or -- 로 이동할 경우 -> 최댓값
M = int(input())
if M: # 고장난게 있을 경우만 인풋을 받음
    broken = set(input().split())
else:
    broken = set()

# 작은수에서 큰수로 이동할땐 500,000 까지만 보면 되지만
# 반대로 큰수에서 작은수로 내려올수도 있으므로 1,000,000 까지 봐야함
for num in range(1000001):
    for N in str(num):
        if N in broken: # 해당 숫자가 번호를 눌러서 만들 수 없는 경우엔 스탑
            break
    else: # 번호를 눌러서 만들 수 있는 경우엔
    	# min(기존답, 번호를 누른 횟수 + 해당 번호로부터 타겟까지의 차이)
        ans = min(ans, len(str(num)) + abs(num - target))

print(ans)


"""
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
    if abc:
        for i in range(len(ans), len(n)):
            answer += (str(min(abc)))
else:
    if abc:
        for i in range(len(ans), len(n)):
            answer += (str(max(abc)))

print(answer)
print(answer2)

if int(ans2[len(ans2) - 1]) > int(n[len(ans2) - 1]):
    if abc:
        for i in range(len(ans2), len(n)):
            answer2 += (str(min(abc)))
else:
    if abc:
        for i in range(len(ans2), len(n)):
            answer2 += (str(max(abc)))

if abs(int(n) - int(answer)) < abs(int(n) - int(answer2)):
    answer = int(answer)
else:
    answer = int(answer2)

if 1 not in b:
    answer2 = '1'
    if abc:
        for i in range(len(n)):
            answer2 += str(min(abc))


if abs(int(n) - int(answer)) <= abs(int(n) - int(answer2)):
    answer = int(answer)
else:
    answer = int(answer2)

if answer >= 10 and abs(int(n) - answer // 10) <= abs(int(n) - answer):
    answer = answer // 10
    # 0 - 0

answer2 = ''

if abc and len(n) > 1:
    for i in range(len(n) - 1):
        answer2 += str(max(abc))

    if abs(int(n) - int(answer2)) <= abs(int(n) - answer):
        answer = int(answer2)

if len(b) == 10:
    answer = 100

# print(answer2)
# 2230
print(answer)

if abs(int(n) - 100) <= len(str(answer)) + abs(int(n) - answer):
    answer = abs(int(n) - 100)
else:
    answer = len(str(answer)) + abs(int(n) - answer)

print(answer)
"""