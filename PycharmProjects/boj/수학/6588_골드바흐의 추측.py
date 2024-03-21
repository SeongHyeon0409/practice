n = 1000001
a = [False,False] + [True]*(n-1)

for i in range(2, int(n**0.5) + 1):
  if a[i]:
    for j in range(2*i, n+1, i):
        a[j] = False

while True:
    n = int(input())
    if n == 0:
        break

    # 4보다 큰 모든 짝수는 두 홀수 소수의 합으로 나타낼 수 있다.
    # if 6 > 3 + 3
    # if 8 > 3 + 5
    # if 10 > 3 + 7, 5 + 5
    for i in range(3, n -3 , 2):
        if a[i] and a[n-i]:
            print(f'{n} = {i} + {n-i}')
            break

