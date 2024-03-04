import sys
sys.stdin = open("input.txt", "r")

T = 10
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n = int(input())
    row = [0] * 100
    cross1 = 0
    cross2 = 0
    maxc = 0
    for i in range(100):
        nums = list(map(int, input().split()))
        maxc = max(maxc, sum(nums))
        for j in range(100):
            row[j] += nums[j]
        cross1 += nums[i]
        cross2 += nums[99 - i]
    maxr = max(row)
    answer = max(maxc, maxr, cross1, cross2)


    print(f'#{test_case} {answer}')