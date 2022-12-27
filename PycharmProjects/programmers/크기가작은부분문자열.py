# 2022.12.27
# Written by SeongHyeon0409

def solution(t, p):
    plen = len(p)
    answer = 0
    for i in range(0, len(t) - plen + 1):
        a = int(t[i:i + plen])
        if a <= int(p):
            answer += 1

    return answer