while True:
    words = input()
    if words == ".":
        break
    flag = 0
    stack = []
    for i in words:
        if i == "(":
            stack.append("(")
        elif i == ")":
            if not stack or stack[-1] == "[":
                flag = 1
                break
            else:
                stack.pop()
        elif i == "[":
            stack.append("[")
        elif i == "]":
            if not stack or stack[-1] == "(":
                flag = 1
                break
            else:
                stack.pop()

    if stack or flag == 1:
        print("no")
    else:
        print("yes")