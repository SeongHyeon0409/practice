# 2020.04.14
# Presented by SeongHyeon0409
# 이분탐색

n = int(input())
nums = sorted(list(map(int, input().split())))
m = int(input())

def binary(l, n, start, end):
    if start > end:
        return 0
    m = (start+end)//2
    if l == n[m]:
        return 1
    elif l < n[m]:
        return binary(l, n, start, m-1)
    else:
        return binary(l, n, m+1, end)

for i in list(map(int, input().split())):
    start = 0
    end = len(nums)-1
    print(binary(i, nums, start, end))

#리스트의 in연산자를 통한 포함 여부의 시간 복잡도는 O(N)입니다.
# 이분 탐색의 시간 복잡도는 O(logN) 입니다.
# Set과 Dictionary의 in연산을 통한 포함 여부 확인의 시간 복잡도는 O(1)입니다.