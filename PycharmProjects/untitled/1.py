def gcdlcm(a, b):
    answer = []
    a1 = []
    b1 = []
    for i in range(1, a + 1):
        if a % i == 0:
            a1.append(i)
    for i in range(1, b + 1):
        if b % i == 0:
            b1.append(i)

    print(a1, b1)
    answer1 = 0
    for i in a1:
        if i in b1:
            answer1 = i
    answer.append(answer1)

    a2 = a
    b2 = b

    while a2 == b2:
        if a2 < b2:
            a2 += a
        else:
            b2 += b

    answer.append(b2)

    return answer


# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(gcdlcm(3, 12))