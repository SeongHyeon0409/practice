# 2022.08.16
# Written by SeongHyeon0409

def solution(lottos, win_nums):
    answer = []
    w_c = 7
    zero_c = lottos.count(0)

    for i in lottos:
        if i in win_nums:
            w_c -= 1

    answer.append(min(6, w_c - zero_c))
    answer.append(min(6, w_c))

    return answer