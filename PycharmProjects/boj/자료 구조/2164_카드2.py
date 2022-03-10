import collections

n = int(input())
stack = collections.deque(range(1, n+1))
i = 0

while len(stack) > 1:
    stack.popleft()
    stack.append(stack.popleft())

print(stack[0])