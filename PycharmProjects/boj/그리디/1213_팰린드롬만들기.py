a = sorted(input())
temp = []
flag = 0

f = ""
b = ""
m = ""

for i in a:
    if a.count(i) % 2 != 0 and i not in temp:
        temp.append(i)
        flag += 1
    if flag > 1 :
        break

if flag > 1:
    print("I'm Sorry Hansoo")
else:
    while a:
        if a.count(a[0]) % 2 == 0:
            f += a.pop(0)
            b += a.pop(0)
        else:
            m += a.pop(0)

    print(f + m + "".join(reversed(b)))