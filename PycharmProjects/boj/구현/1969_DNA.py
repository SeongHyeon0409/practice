n, m = map(int, input().split())

dna = []
for i in range(n):
    dna.append(input())

answer = ''
hd = 0
for i in range(m):
    c = [0] * 26
    for j in range(n):
        c[ord(dna[j][i]) - 65] += 1

    mv = max(c)
    hd += sum(c) - mv
    answer += chr(c.index(mv) + 65)

print(answer)
print(hd)