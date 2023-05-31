
# n = 65536
# a = [False,False] + [True]*(n-1)
# primes=[]
#
# for i in range(4,n+1):
#   if a[i]:
#     primes.append(i)
#     for j in range(2*i, n+1, i):
#         a[j] = False
# print(primes)

T = int(input())


for _ in range(T):
    n = int(input())
    b = n
    #print(factorization(n))
    #card(cards)

    temp = 1
    while True:
        if n != 2 and n % 2 == 0:
            n //= 2
            temp *= 2
        elif n != 3 and n % 3 == 0:
            n //= 3
            temp *= 3
        else:
            break

    for j in range(1, temp+1):
        for i in range(j, b+1, temp):
            print(i, end=' ')
    print()
