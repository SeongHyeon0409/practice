def solution(targets):
    answer = 0
    targets.sort(key=lambda x: [x[1], x[0]])
    e = 0
    for t in targets:
        if t[0] >= e:
            answer += 1
            e = t[1]

    return answer

targets = [[4,5],[4,8],[10,14],[11,13],[5,12],[3,7],[1,4]]
print(solution(targets))