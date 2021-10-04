word = input()
word = word.upper()
maxcount = 0
maxword = ""
countarray = []
wordarray = []
for i in word:
    count = 0
    if i not in wordarray:
        for j in word:
            if i == j:
                count += 1
        countarray.append(count)
        if count > maxcount:
            maxcount = count
            maxword = i

    wordarray.append(i)

maxcount = max(countarray)
flag = 0
for i in countarray:
    if maxcount == i:
        flag += 1
    if flag > 1:
        maxword = '?'
        break

print(maxword)