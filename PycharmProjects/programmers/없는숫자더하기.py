# 2022.12.23
# Written by SeongHyeon0409

def solution(numbers):
    answer = 0
    for i in range(1, 10):
        if i not in numbers:
            answer += i

    return answer

