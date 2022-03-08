def gcd(x, y):
    while y:
        x, y = y, x % y
    return x

a, b = map(int, input().split())

print(gcd(a, b), a * b // gcd(a, b), sep='\n')