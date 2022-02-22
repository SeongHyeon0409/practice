n = int(input())
words = [input() for _ in range(n)]

answer = n
for word in words: #happy, new, year
    ary = [word[0]]
    for i in range(1, len(word)): #(h) a p p y
        bw = word[i-1]
        if word[i] in ary and bw != word[i]:
            answer -= 1
            break
        if word[i] not in ary:
            ary.append(word[i])

print(answer)