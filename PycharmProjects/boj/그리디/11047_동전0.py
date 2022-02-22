n, k = map(int, input().split(" "))
coin = []
answer = 0
for i in range(n):
    coin.append(int(input()))

coin = reversed(coin)
for i in coin:
    if i <= k:
        temp = k // i
        k = k % i
        answer += temp

print (answer)
