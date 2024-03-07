n = int(input())

for i in range(n):
    a = list(input())
    stack = []
    for j in a:
        if j == "(":
            stack.append(j)
        else:
            if not stack:
                stack = [1]
                break
            elif "(" not in stack:
                stack = []
                break
            else:
                stack.pop()

    if stack:
        print("NO")
    else:
        print("YES")

t = int(input())

for _ in range(t):
    stack = []
    answer = "YES"
    words = input()
    for word in words:
        if word == '(':
            stack.append(1)
        else:
            if not(stack):
                answer = "NO"
                break
            else:
                stack.pop()

    if stack:
        answer = "NO"

    print(answer)