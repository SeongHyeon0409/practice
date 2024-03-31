N, M = map(int, input().split())
numbers = list(map(int, input().split()))
numbers.sort()
visited = [0] * N

# 1 7 9 9
def backtracking(depth):
    prev = 0
    if len(box) == M:
        print(*box)
        return
    for i in range(depth, N):
        if prev == numbers[i]:
            continue
        prev = numbers[i]
        box.append(numbers[i])
        backtracking(i)
        box.pop()


box = []
backtracking(0)