import sys
sys.stdin = open("input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n = int(input())
    start = n//2
    end = n//2
    answer = 0
    for i in range(n):
        nums = input()
        for j in range(start, end+1):
            answer += int(nums[j])
        if i < (n//2):
            start -= 1
            end += 1
        else:
            start += 1
            end -=1

    print(f'#{test_case} {answer}')


