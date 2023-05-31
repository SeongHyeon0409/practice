def sum_gauss(n):
	return int(n*(n+1)/2)

T = int(input())

for _ in range(T):
    n = int(input())
    cards = list(map(int, input().split()))
    sum_v = sum(cards)
    print(sum_gauss(n)-sum_v)
