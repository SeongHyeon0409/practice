# number of conference
N = int(input())

#start time, end time
cn = [ list(map(int, input().split())) for _ in range(N)]

cn.sort(key = lambda x : (x[1], x[0]))

count = 1
a = cn[0][1]

for i in range(1, N):
    if a <= cn[i][0]:
        a = cn[i][1]
        count += 1

print(count)