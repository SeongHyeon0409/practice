import sys, collections
input = sys.stdin.readline

n = int(input())
q = collections.deque()
for i in range(n):
    a = list(input().strip().split())
    if a[0] == "push_front":
        q.insert(0, int(a[1]))
    elif a[0] == "push_back":
        q.append(int(a[1]))
    elif a[0] == "pop_front":
        if q:
            print(q.popleft())
        else:
            print("-1")
    elif a[0] == "pop_back":
        if q:
            print(q.pop())
        else:
            print("-1")
    elif a[0] == "size":
        print(len(q))
    elif a[0] == "empty":
        if q:
            print("0")
        else:
            print("1")
    elif a[0] == "front":
        if q:
            print(q[0])
        else:
            print("-1")
    else:
        if q:
            print(q[-1])
        else:
            print("-1")