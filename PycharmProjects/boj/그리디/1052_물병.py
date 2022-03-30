#그리디, 비트마스킹

n, k = map(int, input().split())

answer = 0

while bin(n).count('1') > k: #1의개수가 k개여야함
    idx = bin(n)[::-1].index('1') #맨 뒤자리수 1을 찾는다.
    answer += 2**idx
    n += 2**idx

print(answer)

# 1011 + 0001 = 1100 (+1)
# 1100 + 0100 = 10000 (+4)
# answer = 1 + 4 = 5

