n = int(input())
sentence = input()

dicts = dict()
stack = []

for i in range(65, 65+n):
    dicts[chr(i)] = int(input())

for i in sentence:
    if i == '*':
        stack.append(stack.pop() * stack.pop())
    elif i == '/':
        a = stack.pop()
        b = stack.pop()
        stack.append(b / a)
    elif i == '+':
        stack.append(stack.pop() + stack.pop())
    elif i == '-':
        a = stack.pop()
        b = stack.pop()
        stack.append(b - a)
    else:
        stack.append(dicts[i])

print("%0.2f" %stack[0])
