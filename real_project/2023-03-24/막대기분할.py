t = int(input())

for _ in range(t):

    l = input()
    stack = []
    ans = 0
    i = 0
    while i != len(l):
        if l[i] == '(' and l[i+1] == ')':
            ans += len(stack)
            i += 1
        elif l[i] == '(':
            stack.append(1)
        elif l[i] == ')':
            stack.pop()
            ans += 1
        i += 1
    print(ans)
            # 닫히기 전 모든 열린거에 레이저 개수 추가.
            # 닫히면 스택 마지막 막대기 제거.


    # 막대기 겹칠때 위에가 더길어야함
    # 겹치는거 완전히 포함 끝점 안겹침
    # 막대기 1당 최소 1 레이저
    #
    # 괄호 열고 닫힘 () > 레이저
    # ( 막대기 왼쪽 끝, ) 오른쪽 끝
    # 막대기 수 계산

    # () -> 레이저
    # )(