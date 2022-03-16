n = sorted(list(input()), reverse=True)

answer = 0
for i in n:
    answer += int(i) #모든 자리 수의 합이 3의 배수여야함
if answer % 3 != 0 or "0" not in n:
    print(-1)
else:
    print(''.join(n))