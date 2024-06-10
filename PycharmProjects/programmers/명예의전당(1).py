import heapq

def solution(k, score):
    answer = []
    q = []
    for i in score:
        heapq.heappush(q, i)
        if len(q) > k:
            heapq.heappop(q)
        answer.append(q[0])
    return answer


k = 3
score = [10, 100, 20, 150, 1, 100, 200]
print(solution(k, score))