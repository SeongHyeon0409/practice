# 삽입
# 삭제
# 추가

# 0 ~ 999999 n 개

for tc in range(1, 2):
    n = int(input())
    cryp = list(map(int, input().split()))
    m = int(input())
    com = list(input().split())

    i = 0
    while i < m:
        if com[i] == 'I':
            x, y = int(com[i+1]), int(com[i+2])
            k = i+3
            for j in range(x+1, x+1+y):
                cryp.insert(j, int(com[k]))
                k += 1
            i += 2 + y
        elif com[i] == 'D':
            x, y = int(com[i+1]), int(com[i+2])
            for j in range(y):
                del cryp[x+1]
            i += 2 + y
        elif com[i] == 'A':
            y = int(com[i+1])
            for j in range(i+2, i+2+y):
                cryp.append(int(com[j]))
            i += 1 + y

    for i in range(10):
        print(cryp[i])



