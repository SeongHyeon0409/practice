# 2020.04.14
# Presented by SeongHyeon0409
# 이분탐색
import sys
input = sys.stdin.readline

n, k = map(int, input().strip().split())

trees = list(map(int, input().strip().split()))

start , end = 1, max(trees)

while start <= end:
    mid = (start + end) // 2
    cnt = 0 # 자른 나무 길이
    for i in trees:
        if i > mid:
            cnt += i - mid

    if cnt >= k: #더 크게 잘라야함
        start = mid + 1
    else: #더 작게 잘라야함
        end = mid - 1

print(end)
