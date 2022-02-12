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


