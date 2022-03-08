n = int(input())
l = list(map(int, input().split()))

a = l[0]

def gcd(x, y):
   while y:
       x, y = y, x % y
   return x


for i in range(1, n):
    if a % l[i] == 0:
        print("{0}/{1}".format(a//l[i], 1))
    else:
        print("{0}/{1}".format(a//gcd(a, l[i]), l[i]//gcd(a, l[i])))
