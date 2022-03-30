n, k = map(int, input().split())
h = (['N']*k) + list(input()) + (['N']*k)

a = k
answer = 0

for i in range(k, n+k):
    if h[i] == 'P':
        for j in range(i-k, i+k+1):
            if h[j] == 'H':
                h[j] = 'N'
                answer += 1
                break

print(answer)