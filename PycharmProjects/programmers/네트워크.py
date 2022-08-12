def solution(n, computers):
    v = [False] * n
    answer = 0
    for i in range(n):
        if v[i] == False:
            v[i] = True
            q = [i]
            while q:
                c = q.pop()
                v[c] = True
                for i in range(n):
                    if i != c and computers[c][i] == 1 and v[i] == False:
                        q.append(i)
            answer += 1

    return answer