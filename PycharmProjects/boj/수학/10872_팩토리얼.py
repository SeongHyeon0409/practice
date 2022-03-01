N = int(input())

# answer = 1
#
# for i in range(2, N+1):
#     answer *= i
#
# print(answer)

def factorial(n):
    if n == 0 or n ==1:
        return 1
    return n * factorial(n-1)

print(factorial(N))
