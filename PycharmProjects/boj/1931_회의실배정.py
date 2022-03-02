# number of conference
N = int(input())

#start time, end time
cn = [ list(map(int, input().split())) for _ in range(N)]

print(cn)

cn.sort(key = lambda x : x[0] )

print(cn)