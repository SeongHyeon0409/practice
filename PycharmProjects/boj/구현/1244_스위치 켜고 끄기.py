n = int(input())
s = [2] + list(map(int, input().split()))
m = int(input())

def switch(i):
    if s[i] == 0:
        s[i] = 1
    else:
        s[i] = 0

for i in range(m):
    a, b = map(int, input().split())

    if a == 1:
        for j in range(b, n+1, b):
            switch(j)
    else:
        switch(b)
        for j in range(1, n+1):
            if b-j >= 1 and b+j < n+1 and s[b-j] == s[b+j]:
                switch(b-j)
                switch(b+j)
            else:
                break

for i in range(1, n+1):
    print(s[i], end=' ')
    if i % 20 == 0:
        print()
