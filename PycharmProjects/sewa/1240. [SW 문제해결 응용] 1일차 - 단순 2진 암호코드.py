import sys
sys.stdin = open("input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
code = ['0001101', '0011001', '0010011', '0111101', '0100011', '0110001', '0101111', '0111011', '0110111', '0001011']
for test_case in range(1, T + 1):
    r, c = map(int, input().split())
    maps = [input() for i in range(r)]
    passw = ''
    for i in maps:

        if i.find('1') > 0:
            rev = i[::-1]
            passw = rev[rev.find('1'):rev.find('1') + 56]
            break

    passw = passw[::-1]
    #passw를 7글자씩 슬라이싱 해야함

    passa = []

    while len(passw) > 0:
        passa.append(passw[:7])
        passw = passw[7:]


    for i in range(8):
        passa[i] = code.index(passa[i])

    sc = (passa[0] + passa[2] + passa[4] + passa[6]) * 3 + (passa[1] + passa[3] + passa[5] + passa[7])
    if sc % 10 == 0:
        answer = sum(passa)
    else:
        answer = 0
    print(f'#{test_case} {answer}')

