from functools import cmp_to_key

def wordlen(x, y):
    return len(x) - len(y)

n = int(input())

words = set()
for i in range(n):
    words.add(input())

words = sorted(words)
words = sorted(words, key=cmp_to_key(wordlen))

print(*words, sep='\n')