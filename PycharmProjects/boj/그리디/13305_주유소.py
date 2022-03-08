n = int(input())
v = list(map(int,input().split())) + [0]
c = list(map(int,input().split())) + [0]

answer = 0
a = v[0]
minv = c[0]

for i in range(0, n):
    if c[i] < minv:
        minv = c[i]
    answer += v[i] * minv

print(answer)
