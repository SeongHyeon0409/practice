import math

n, s = map(int, input().split())
loc = list(map(int, input().split()))

# 1 3 7 9 10 11 모든 값의 차이중 최솟값 2?
# 33 57 81 105

# s와 각 동생의 차를 모두 구한 뒤 최대공약수를 찾아야함.

newa = []

for i in loc:
    newa.append(abs(i - s))

ans = newa[0]
for i in newa:
    ans = math.gcd(ans, i)

print(ans)