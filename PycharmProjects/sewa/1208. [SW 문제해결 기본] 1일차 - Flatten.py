import sys
sys.stdin = open("input.txt", "r")

T = 10
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n = int(input())
    nums = list(map(int, input().split()))
    for i in range(n):
        nums.sort()
        nums[0] = nums[0] + 1
        nums[99] = nums[99] - 1
    answer = max(nums) - min(nums)

    print(f'#{test_case} {answer}')