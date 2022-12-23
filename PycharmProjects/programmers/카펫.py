# 2022.12.23
# Written by SeongHyeon0409

def solution(brown, yellow):
    flag = 0
    answer = []
    for i in range(3, brown//2+1):
        if flag == 1:
            break
        for j in range(3, brown//2+1):
            if (i * 2) + (j * 2) - 4 == brown:
                if (i - 2) * (j - 2) == yellow:
                    answer = [i, j]
                    flag = 1
                    break
    answer.sort(reverse=True)
    return answer