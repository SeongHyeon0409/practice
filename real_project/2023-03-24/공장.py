from collections import deque

t = int(input())

for _ in range(t):
    n = int(input())
    AL, BL = deque(), deque()
    AS, BS = 0, 0
    for i in range(n):
        a = input()
        if a[0] == 'O':
            ord, count, fac = a.split()
            count = int(count)
        else:
            ord, fac = a.split()

        if ord == 'ORDER':
            if fac == 'C':
                if AS <= BS:
                    AL.append(count)
                    AS += count
                else:
                    BL.append(count)
                    BS += count
            elif fac == 'A':
                AL.append(count)
                AS += count
            else:
                BL.append(count)
                BS += count
        else:
            if fac == 'A':
                AS -= AL.popleft()
            else:
                BS -= BL.popleft()

    print(AS, BS)