def get_divisor(n):
    divisors = []
    sqrt_n = int(n ** 0.5)

    # 1부터 sqrt(n)까지 약수 구하기
    for i in range(1, sqrt_n + 1):
        if n % i == 0:
            divisors.append(i)
            if i != sqrt_n:
                divisors.append(n // i)

    return divisors


print(get_divisor(100))