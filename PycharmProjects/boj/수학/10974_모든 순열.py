N = int(input())
def backtracking():

    if len(box) == N:
        print(*box)
        return
    for i in range(1, N + 1):
        if i in box:
            continue
        box.append(i)
        backtracking()
        box.pop()


box = []
backtracking()