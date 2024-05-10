# n극 s극 이동후 위아래로 다른 극이 있으면 교착상태
# 위에 빨강 아래 파랑인 경우 교착

for _ in range(1, 11):
    n = int(input())
    maps = [list(map(int, input().split())) for i in range(n)]
    ans = 0
    # 1은 아래로 이동 2는 위로 이동
    # 열마다 탐색 맨 위부터 1이 나오기전까지 2는 날리기, 맨 아래부터 2가나오기전까지 1 날리기
    # 다시 열마다 탐색 1나오고 2가 바로나오면 교착상태 + 1

    # for i in range(n):
    #     for j in range(n):
    #         if maps[j][i] != 1:
    #             maps[j][i] = 0
    #         else:
    #             break
    #     for j in range(n-1, -1, -1):
    #         if maps[j][i] != 2:
    #             maps[j][i] = 0
    #         else:
    #             break

    # 앞뒤를 날릴 필요가 없음..

    for i in range(n):
        flag = 0
        for j in range(n):
            if maps[j][i] == 1:
                flag = 1
            elif maps[j][i] == 2 and flag == 1:
                ans += 1
                flag = 0


    print(f'#{_} {ans}')