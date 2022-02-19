t = int(input())

for i in range(t):
    answer = 0
    n, q = map(int, input().split())

    mask = [0] * n
    mask[q] = 1

    doc = list(map(int, input().split()))

    while True:
        if doc[0] < max(doc):
            a = doc.pop(0)
            doc.append(a)
            b = mask.pop(0)
            mask.append(b)
        else:
            a = doc.pop(0)
            answer += 1
            b = mask.pop(0)
            if b == 1:
                print(answer)
                break
