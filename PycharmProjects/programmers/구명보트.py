from collections import deque

# 2022.12.23
# Written by SeongHyeon0409

def solution(people, limit):
    answer = 0
    people = deque(sorted(people, reverse=True))
    while len(people) > 1:
        if people[0] + people[-1] <= limit:
            people.pop()
            people.popleft()
            answer += 1
        else:
            people.popleft()
            answer += 1

    if len(people) == 1:
        answer += 1

    return answer

