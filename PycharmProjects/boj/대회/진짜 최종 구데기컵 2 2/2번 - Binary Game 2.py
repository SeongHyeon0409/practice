n = int(input())
answer = ''
for i in range(n+1):
    answer += str(bin(i)[2:])

print(answer)

