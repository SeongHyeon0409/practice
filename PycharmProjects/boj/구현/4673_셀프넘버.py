def d(n):
    a = n

    while True:
        b = n%10
        a += b
        n = n//10
        if n<10:
            a += n
            break

    return a

nums = []

for i in range(1,10000):
    n = d(i)
    nums.append(n)


for i in range(1, 10000):
    if i not in nums:
        print(i)