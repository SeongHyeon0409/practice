temp = input().split('-')

sumlist = []

for i in temp:
    if '+' in i:
        temp2 = i.split('+')
        #print(temp2)
        sum1 = sum(list(map(int, temp2)))
        #print(sum1)
        sumlist.append(sum1)
    else:
        sumlist.append(int(i))

#print(sumlist)
answer = sumlist[0]
for i in range(1, len(sumlist)):
    answer -= sumlist[i]

print(answer)