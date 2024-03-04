import sys
sys.stdin = open("input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n = int(input())
    nums = list(map(int, input().split()))
    answer = 0

    for i in range(2, len(nums)-2):
        maxn = max(nums[i-1], nums[i-2], nums[i+1], nums[i+2])
        if nums[i] > maxn:
            answer += nums[i] - maxn

    print(f'#{test_case} {answer}')