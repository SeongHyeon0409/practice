n = int(input())
a = [0,1,3]
for i in range(3,n+1):
    a.append(a[i-1]+a[i-2]*2)

print(a[n]%10007)