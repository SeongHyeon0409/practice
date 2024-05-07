n = int(input()) # n < 50
p = []
m = []
ans = 0

for i in range(n):
    num = int(input())
    if num > 1:
        p.append(num)
    elif num == 1:
        ans += 1
    else:
        m.append(num)

# 양수는 양수끼리 # 1은 곱하기 x 무조건 더하기
# 음수는 음수끼리
# 0은 남는 음수가 있으면 곱해주기

p.sort()
m.sort(reverse=True)

while p:
    if len(p) > 1:
        ans += p.pop() * p.pop()
    else:
        ans += p.pop()

while m:
    if len(m) > 1:
        ans += m.pop() * m.pop()
    else:
        ans += m.pop()
print(ans)