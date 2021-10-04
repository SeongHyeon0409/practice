

def getDayName(a, b):
    month = {1: 31, 2: 29, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
    total = 0
    for key in sorted(month.keys()):
        if a > key:
            print(key)
            total += month[key]
            print (total)

    total += b

    if total % 7 == 1:
        answer = "FRI"
    elif total % 7 == 2:
        answer = "SAT"
    elif total % 7 == 3:
        answer = "SUN"
    elif total % 7 == 4:
        answer = "MON"
    elif total % 7 == 5:
        answer = "TUE"
    elif total % 7 == 6:
        answer = "WED"
    else:
        answer = "THU"
    return answer


# 아래 코드는 테스트를 위한 출력 코드입니다.