n = int(input())

fibonacci = [0] * (n + 1)
fibonacci[1] = 1
print(fibonacci)

for i in range(2, n + 1):
    fibonacci[i] = fibonacci[i-1] + fibonacci[i-2]
    print(fibonacci)
    print(fibonacci[n-1], fibonacci[n])



A  1 0
B  0 1
BA 1 1
BAB 1 2
BABBA 2 3
BABBABAB 3 5