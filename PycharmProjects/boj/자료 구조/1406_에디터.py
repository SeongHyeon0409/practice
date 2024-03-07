import sys
input = sys.stdin.readline

word1 = list(input().rstrip())
word2 = []
n = int(input().rstrip())

for i in range(n):
    command = input().rstrip()
    if len(command) > 1:
        word1.append(command[-1])
    else:
        if command == 'L':
            if word1:
                word2.append(word1.pop())
        elif command == 'D':
            if word2:
                word1.append(word2.pop())
        elif command == 'B':
            if word1:
                word1.pop()

word1.extend(reversed(word2))
print(''.join(word1))
