import sys

input = sys.stdin.readline

def push(a, b):
    a.append(b)

def pop(a):
    if len(a) == 0:
        return -1
    else:
        c = a[-1]
        del a[-1]
        return c

def size(a):
    return len(a)

def empty(a):
    if len(a) == 0:
        return 1
    else:
        return 0

def top(a):
    if len(a) == 0:
        return -1
    else:
        return a[-1]

if __name__ == '__main__':
    n = int(input())
    answer = []
    for i in range(n):
        a = list(input().split())
        if a[0] == "push":
            push(answer, int(a[1]))
        elif a[0] == "pop":
            print(pop(answer))
        elif a[0] == "size":
            print(size(answer))
        elif a[0] == "empty":
            print(empty(answer))
        else:
            print(top(answer))

