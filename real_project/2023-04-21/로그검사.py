t = int(input())

for _ in range(t):
    n = int(input())

    logs = []
    for i in range(n):
        logs.append(input())

    answer = 0

    for log in logs:
        if len(log) > 100:
            answer += 1
            continue

        temp = log.split(" ")
        if len(temp) != 12:
            answer += 1
            continue

        if temp[1] != ':' or temp[4] != ':' or temp[7] != ':' or temp[10] != ':':
            answer += 1
            continue

        if temp[0] != 'line_name' or temp[3] != 'product_name' or temp[6] != 'error_level' or temp[9] != 'message':
            answer += 1
            continue

        if not temp[2].isalpha() or not temp[5].isalpha() or not temp[8].isalpha() or not temp[11].isalpha():
            answer += 1

    print(answer)

