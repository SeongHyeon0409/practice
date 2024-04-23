alpha = [0] * 26

n = int(input())

for i in range(n):
    word = input()
    tmp = len(word) - 1
    for j in range(len(word)):
        alpha[ord(word[j]) - 65] += 10 ** tmp
        tmp -= 1

alpha.sort(reverse=True)

ans = 0
c = 9

for i in range(9):
    ans += alpha[i] * c
    c -= 1

print(ans)