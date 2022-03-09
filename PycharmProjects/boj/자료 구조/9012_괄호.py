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


        #print(stack)
    if stack:
        print("NO")
    else:
        print("YES")