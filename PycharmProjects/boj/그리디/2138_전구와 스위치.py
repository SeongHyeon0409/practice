n = int(input())
a = list(map(int, list(input())))
a2 = a[:]
b = list(map(int, list(input())))

ans1 = 0
ans2 = 0

def switch(a, i):
    mini = 0 if i-1 < 0 else i-1
    maxi = n if i+1 > n-1 else i+2
    for j in range(mini, maxi):
        if a[j] == 0:
            a[j] = 1
        else:
            a[j] = 0

switch(a2, 0)
ans2 += 1

for i in range(1, n):
    if a[i-1] != b[i-1]:
        switch(a, i)
        ans1 += 1
    if a2[i-1] != b[i-1]:
        switch(a2, i)
        ans2 += 1

if a == b:
    print(ans1)
elif a2 == b:
    print(ans2)
else:
    print(-1)
