import sys
sys.stdin = open("input.txt", "r")

from collections import deque

T = 10
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n = int(input())
    nums = deque(map(int, input().split()))
    while nums[-1] != 0:
        for i in range(1, 6):
            if nums[-1] <= 0:
                nums[-1] = 0
                break
            nums.append(nums.popleft() - i)

    answer = 0

    print(f'#{test_case}', *nums)