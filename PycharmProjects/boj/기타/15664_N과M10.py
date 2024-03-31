N, M = map(int, input().split())
numbers = list(map(int, input().split()))
numbers.sort()
visited = [0] * N

def backtracking(depth):
    prev = 0
    if len(box) == M:
        print(*box)
        return

    for i in range(depth, N):
        if numbers[i] == prev or visited[i] == 1:
            continue
        box.append(numbers[i])
        prev = numbers[i]
        visited[i] = 1
        backtracking(i +1)
        box.pop()
        visited[i] = 0


box = []
backtracking(0)

