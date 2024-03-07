words = input() + '1'

answer = []
i = 0

while i < len(words) - 1:
    stack = []
    if words[i] == '<':
        while words[i] != '>':
            stack.append(words[i])
            i += 1
        stack.append('>')
        i += 1
        answer.append(''.join(stack))
    else:
        if words[i] != '>' :
            while words[i] != ' ' and words[i] != '<' and i < len(words) - 1:
                stack.append(words[i])
                i += 1
            answer.append(''.join(reversed(stack)))
            if words[i] == ' ':
                answer.append(' ')
                i += 1

print(''.join(answer))