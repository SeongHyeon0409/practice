n = int(input())

def gcd(x, y):
    while y:
        x, y = y, x % y
    return x

for i in range(n):
    a, b = map(int, input().split())
    print(a * b // gcd(a, b))