n = int(input())
num = 665
count = 0

while(1):
    num += 1
    snum = str(num)
    if snum.find('666') > -1:
        count += 1
    if n == count:
        break


print(snum)