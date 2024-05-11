for tc in range(1, 11):
    n = int(input())
    words = input()
    ans = 1

    #'()' '[]' '{}' '<>'
    stack = []

    for w in words:
        if w == '(':
            stack.append('(')
        elif w == '[':
            stack.append('[')
        elif w == '{':
            stack.append('{')
        elif w == '<':
            stack.append('<')
        elif w == ')':
            if stack and stack.pop() == '(':
                continue
            else:
                ans = 0
                break
        elif w == ']':
            if stack and stack.pop() == '[':
                continue
            else:
                ans = 0
                break
        elif w == '}':
            if stack and stack.pop() == '{':
                continue
            else:
                ans = 0
                break
        elif w == '>':
            if stack and stack.pop() == '<':
                continue
            else:
                ans = 0
                break

    if stack:
        ans = 0

    print(f'#{tc} {ans}')

