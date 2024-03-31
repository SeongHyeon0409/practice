N, M = map(int, input().split())
numbers = list(map(int, input().split()))

numbers.sort()

def backtracking(depth):
    if depth == M:
        print(' '.join(map(str, box)))
        return

    for i in range(N):
        box.append(numbers[i])
        backtracking(depth+1)
        box.pop()


box = []
backtracking(0)


