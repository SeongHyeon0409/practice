N, M = map(int, input().split())
numbers = list(map(int, input().split()))

numbers.sort()

def backtracking(depth):
    if len(box) == M:
        print(' '.join(map(str, box)))
        return

    for i in range(depth, N):
        box.append(numbers[i])
        backtracking(i)
        box.pop()


box = []
backtracking(0)


