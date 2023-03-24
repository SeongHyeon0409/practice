t = int(input())

for _ in range(t):
    n = int(input())
    AL, BL = [], []
    AS, BS = 0, 0
    for i in range(n):
        a = input()
        if a[0] == 'O':
            ord, count, fac = a.split()
        else:
            ord, fac = a.split()

        if ord == 'ORDER':
            if fac == 'C':
                if AS <= BS:
                    AL.append(int(count))
                    AS += (int(count))
                else:
                    BL.append(int(count))
                    BS += (int(count))
            elif fac == 'A':
                AL.append(int(count))
                AS += (int(count))
            else:
                BL.append(int(count))
                BS += (int(count))
        else:
            if fac == 'A':
                AS -= AL.pop(0)
            else:
                BS -= BL.pop(0)

    print(AS, BS)