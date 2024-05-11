for tc in range(1, 11):
    n = int(input())
    ex = input()
    # 그냥 곱하기먼저?

    ans = 0
    stack = []

    i = 0
    while i < n:
        if ex[i] == '+':
            i += 1
            continue
        elif ex[i] == '*':
            stack.append(stack.pop() * int(ex[i+1]))
            i += 1
        else:
            stack.append(int(ex[i]))

        i += 1

    print(f'#{tc} {sum(stack)}')
