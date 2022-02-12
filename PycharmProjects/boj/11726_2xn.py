
def tile(n):
    a = [0, 1 ,2]
    for i in range(3, n+1):
        a.append(a[i-1]+a[i-2])
    return a[n]%10007

n = int(input())
print(tile(n))