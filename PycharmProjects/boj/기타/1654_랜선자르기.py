# 2020.04.14
# Presented by SeongHyeon0409
# 이분탐색

n, k = map(int, input().split())

lines = [int(input()) for _ in range(n)]

start , end = 1, max(lines)

while start <= end:
    mid = (start + end) // 2
    lans = 0 # 랜선 수
    for i in lines:
        lans += i // mid
    if lans >= k: #더 크게 잘라야함
        start = mid + 1
    else: #더 작게 잘라야함
        end = mid - 1

print(end)

