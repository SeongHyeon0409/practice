def stick(a):
    temp = [64]

    while sum(temp) > a:
        t = int(min(temp)/2)
        temp.remove(min(temp))
        temp.append(t)
        if sum(temp) < a:
            temp.append(t)

    return (len(temp))

n = int(input())
print(stick(n))