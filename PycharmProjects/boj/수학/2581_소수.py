n = int(input())
m = int(input())

if n == 1:
    n = 2

nums = []

for i in range(n, m+1):
    flag = 0
    for j in range(2, i):
        if i % j == 0:
            flag = 1
            break
    if flag == 0:
        nums.append(i)

if not nums:
    print(-1)
else:
    print(sum(nums))
    print(min(nums))

#에라토스네테스의 체

def is_prime_num(n):
    arr = [True] * (n + 1)  # 특정 수가 지워졌는지 아닌지 확인하기 위한 배열
    arr[0] = False
    arr[1] = False

    for i in range(2, n + 1):
        if arr[i] == True:  # 특정 수가 지워지지 않았다면 (소수여서)
            j = 2

            while (i * j) <= n:
                arr[i * j] = False  # i의 배수의 값을 False로 지워준다.
                j += 1

    return arr


# arr = is_prime_num(50)  # 0 ~ 50중 소수를 구하기 위한 함수
#
# for i in range(len(arr)):
#     if arr[i] == True:
#         print(i, end=' ')