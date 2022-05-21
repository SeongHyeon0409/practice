# 2020.05.21
# Presented by SeongHyeon0409
import sys
from collections import deque

input = sys.stdin.readline

t = int(input().strip())

for i in range(t):
    c = input().strip()
    n = int(input().strip())
    try:
        temp = deque(list(map(int, input().strip()[1:-1].split(','))))
    except:
        temp = deque()

    flag = 0
    for i in c:
        if i == 'R':
            if flag == 0:
                flag = 1
            else:
                flag = 0
        else:
            try:
                if flag == 0:
                    temp.popleft()
                else:
                    temp.pop()
            except:
                temp = 'error'
                break

    if flag == 1 and temp != 'error':
        temp.reverse()

    if temp != 'error':
        print('[', end='')
        for i in range(len(temp)):
            if i != len(temp)-1:
                print(str(temp[i]) + ',', end='')
            else:
                print(str(temp[i]), end='')
        print(']')
    else:
        print(temp)
