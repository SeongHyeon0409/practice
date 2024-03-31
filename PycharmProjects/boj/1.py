import sys
sys.setrecursionlimit(99999)
N, M = map(int, input().split())
numbers = [int(x) for x in input().split()]

numbers.sort()

def backtracking(depth):
    if len(box) == M:
        print(' '.join(map(str,box)))
        return

    for i in range(N):
        box.append(numbers[i])
        backtracking(depth+1)
        box.pop()

box = []
backtracking(0)