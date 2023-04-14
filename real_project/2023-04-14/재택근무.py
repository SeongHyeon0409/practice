t = int(input())

for _ in range(t):
    a, b, k, l = map(int, input().split()) # 팀개수, 재택가능개수, 불가능 개수, 사원수
    possible = list(input().split())
    impossible = list(input().split())
    imployee = dict()
    a = 1
    for i in range(1, l+1):
        # 팀번호, 담당 업무 수
        # 담당하는 m 개의 업무
        n, m = map(int, input().split())
        b =(list(input().split()))
        if n not in imployee:
            imployee[n] = [[i, b]]
        else:
            imployee[n].append([i, b])

    # print(possible)
    # print(impossible)
    # print(imployee)

    #최소 1명출근 (전원 출근인경우 가장 낮은 사원 출근)
    answer = [i for i in range(1, l+1)]
    for key, value in imployee.items(): #팀
        #print(key, value)
        flag = 0
        for k in value:
            for i in k[1]:
                if i in impossible:
                    answer.remove(k[0])
                    flag = 1
                    break
        if flag == 0: #모두 재택근무라면 첫번째가..
            answer.remove(value[0][0])

    if answer:
        print(*answer)
    else:
        print(-1)
