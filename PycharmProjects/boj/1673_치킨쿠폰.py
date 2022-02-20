while True:
    try:
        n, k= map(int,input().split())
        s = n #stamp
        while s >= k:
            temp = s//k
            n += temp
            s %= k
            s += temp

        print(n)

    except:
        break
