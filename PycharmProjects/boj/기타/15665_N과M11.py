N, M = map(int, input().split())
numbers = list(map(int, input().split()))
numbers.sort()
visited = [0] * N

def backtracking(depth):
    prev = 0
    if len(box) == M:
        print(*box)
        return

    for i in range(N):
        if numbers[i] == prev:
            continue
        box.append(numbers[i])
        prev = numbers[i]

        backtracking(i+1)
        box.pop()



box = []
backtracking(0)

