def yosepus(n, k):
    k -= 1
    l = k
    ary = [int(i+1) for i in range(n)]
    answer = []
    while ary:
        answer.append(ary[k])
        del ary[k]
        k += l

        while k > len(ary)-1 and ary:
            k -= len(ary)

    print("<%s>" %(", ".join(map(str,answer))))

a, b = map(int, input().split(" "))

yosepus(a,b)

n ,k = map(int, input().split())
nums = [i for i in range(1, n+1)]
na = []
c = 0
while nums:

    c = c + k - 1

    if c >= len(nums):
        c = c % len(nums)

    na.append(str(nums.pop(c)))


print("<",", ".join(na),">", sep='')
