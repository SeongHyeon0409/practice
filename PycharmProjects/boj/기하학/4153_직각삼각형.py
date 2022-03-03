while True:
    xyz = list(map(int, input().split()))
    xyz.sort()

    if xyz[0] == 0:
        break

    if xyz[0]**2 + xyz[1]**2 == xyz[2]**2:
        print("right")
    else:
        print("wrong")