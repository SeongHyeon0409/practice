case = 0

while True:
    case += 1
    a, b, c = map(int, input().split())
    if a == 0 and b == 0 and c == 0:
        break

    answer = a * (c // b)
    answer += min(a, (c % b))

    print("Case {0}: {1}".format(case, answer))