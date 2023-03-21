# 2023.03.17
# Written by SeongHyeon0409

# 이진트리 > O(nlogn) 투포인터 > O(n)

def binary(target, com):
    start = 0
    end = len(com) - 1
    while start <= end:
        mid = (start + end) // 2
        if com[mid] == target:
            return target
        elif com[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    return None

t = int(input())

for _ in range(t):
    n, p = map(int, input().split())
    com = list(map(int, input().split())) # 1 ~ 200
    com.sort()

    start = 0
    end = n-1

    while True:
        if com[start] + com[end] == p:
            print(com[start], com[end])
            break
        elif com[start] + com[end] < p:
            start += 1
        else:
            end -= 1
