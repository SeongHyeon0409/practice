n = int(input())
ary = [list(map(int, input().split())) for _ in range(n)]
answer = [1] * n

for i in range(n):
    for j in range(n):
        if ary[i][0] < ary[j][0] and ary[i][1] < ary[j][1]:
            answer[i] += 1
        #elif ary[i][0] > ary[j][0] and ary[i][1] > ary[j][1]:
        #    continue
        #else:
        #    pass

print(*answer)
        