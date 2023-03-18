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

    ans1, ans2 = 0, 0

    for i in range(len(com)):
        ans2 = binary(p - com[i], com[i+1:])
        if ans2:
            ans1 = com[i]
            break

    print(ans1, ans2)
