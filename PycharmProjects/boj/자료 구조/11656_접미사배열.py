word = input()
words = []

for i in range(len(word)):
    words.append(word[i:])

for i in sorted(words):
    print(i)
