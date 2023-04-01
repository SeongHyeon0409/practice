t = int(input())

for _ in range(t):
    n, T = map(int, input().split())
    info = [list(map(int, input().split())) for i in range(n)] #t, f
    info.sort(key = lambda x:x[1])
    print(info)

    # 기본요금 f원, t분 경과시 f원씩 비용 상승
    # T분 대여
    # 최소, 최대 파악 방법

    # t = 10 , t = 9가 어디서나옴??
    # 최소가 되려면 t가 커야되고 f가 적어야함.
    # 최대가 되려면 t가 작아야되고 f가 커야함.

    # T 가 경계선에 걸쳐야한다??

    # 요금 별로 정렬?

    #가능한 t와 f를 모두 찾기.
    #if t=1 이면?

    # 바뀌는 경계. 4 16, 6 16 -> 12, 10
    #           최소 12 분에 1000원, 10분에 1000원
    # 16 21, 16 26 ->5, 10
    # 5분에 1000원, 10분에 1000원
    # 최
    # 8 : 8원 2000원 16에 3000이.. 24에 4000이
    # 11 : 11에 2000원 21.은 2000원 22에 3000원 33에 4천원
    tlist = []
    #최소요금
    pay = 0
    for i in range(len(info)-1):
        if info[i][1] != info[i+1][1]:
            pay = info[i+1][1] - info[i][1]
    for t in range(1, T+1):
        flag = 0
        for j in info:
            print('t:',t,pay + (j[0]//t * pay))
            if pay + (j[0]//t * pay) != j[1]:
                flag = 1
                break
            if flag == 1:
                break
        if flag == 0:
            tlist.append(t)
    print(tlist)


