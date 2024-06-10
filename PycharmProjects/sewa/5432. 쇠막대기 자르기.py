# ( 나오면 스택에 추가
# () 나오면 스택에 있는 수만큼 count +
# ) 나오면 스택 한개 빼고 count + 1

t = int(input())

for tc in range(1, t + 1):
    r = input()
    stack = []
    ans = 0
    for i in range(len(r)):
        if r[i] == ')' and r[i - 1] == '(':
            continue
        if r[i] == '(':
            if i < len(r) - 1 and r[i + 1] == ')':
                ans += len(stack)
            else:
                stack.append('(')
        else:
            stack.pop()
            ans += 1

    print(f'#{tc} {ans}')


