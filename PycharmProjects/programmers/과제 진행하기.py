def solution(plans):
    answer = []
    stack = []
    p = []
    for data in plans:
        sub, start, time = data[0], data[1], data[2]
        sh, sm = map(int, start.split(":"))
        start = sh * 60 + sm
        p.append([sub, start, int(time)])

    p.sort(key=lambda x: x[1])
    ptime = p[0][1]
    for d in range(len(p)):

        if d == len(p)-1:
            answer.append(p[d][0])
            break

        dsub, dstart, dtime = p[d][0], p[d][1], p[d][2]
        nsub, nstart, ntime = p[d+1][0], p[d+1][1], p[d+1][2]

        if not stack:
            ptime = dstart

        if ptime + dtime <= nstart:
            answer.append(dsub)
            ptime += dtime
        else:
            stack.append([dsub, dtime - (nstart - ptime)])
            ptime = nstart

        # 다음시작까지 시간이 남아돌면...
        while stack and ptime < nstart:
            s = stack.pop()
            sub, time = s[0], s[1]
            if ptime+time <= nstart:
                ptime += time
                answer.append(sub)
            else:
                stack.append([sub, time - (nstart - ptime)])
                ptime = nstart


    while stack:
        answer.append(stack.pop()[0])
    return answer

plans = [["aaa", "12:00", "30"], ["bbb", "12:10", "30"], ["ccc", "14:00", "30"]]

1240
print(solution(plans))