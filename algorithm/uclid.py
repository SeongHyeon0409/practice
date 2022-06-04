def uclid(a, b):
    if b == 0:
        return a
    elif b > 0:
        a, b = b, a%b
        return uclid(a, b)

if __name__ == "__main__" :
    n = int(input())
    for i in range(n):
        a, b = (map(int, input().split(" ")))
        if b > a:
            a, b = b, a
        print(uclid (a, b))