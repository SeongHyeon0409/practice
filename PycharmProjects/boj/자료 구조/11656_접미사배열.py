import math

a, b = map(int, input().split())
print(math.gcd(a, b))
print(math.lcm(a, b))

def gcd(a, b):
    while b:
        a, b = b, a%b

    return a

print(gcd(a, b))
print(a * b // gcd(a, b))