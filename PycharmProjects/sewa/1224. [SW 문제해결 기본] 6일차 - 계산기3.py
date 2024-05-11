for tc in range(1, 11):
    n = int(input())
    ex = input()
    # 괄호가 있으면 스택에 다 쳐넣기
    # 괄호 닫히면 스택 처리하기?

    ans = 0
    stack = []
    tmp = []
    # 후위 표기식으로 바꾸기
    for i in ex:
        if i.isdigit():
            tmp.append(i)
        elif i == '(':
            stack.append('(')
        elif i == '+':
            while stack:
                if stack[-1] == '(': break
                tmp.append(stack.pop())
            stack.append(i)
        elif i == '*':
            while stack[-1] == '*':
                tmp.append(stack.pop())
            stack.append(i)
        else: #)
            while stack:
                if stack[-1] == '(':
                    stack.pop()
                    break
                tmp.append(stack.pop())

    print(tmp)


    print(f'#{tc} {1}')
