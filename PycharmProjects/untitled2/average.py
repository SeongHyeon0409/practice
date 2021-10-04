n = int(input())
data = list(map(int, input().split()))

maxnum = max(data)
sumscore = 0

for i in data:
    sumscore += i/maxnum*100

print(sumscore/n)