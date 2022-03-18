n, m = map(int, input().split())

answer = 0

l = [list(map(int, input().split())) for _ in range(m)]
l.sort(key = lambda x:x[0])
pm = l[0][0]
l.sort(key = lambda x:x[1])
im = l[0][1]

while n >= 6 and pm < im * 6:
    answer += pm
    n -= 6

if pm < im * n and n < 6:
    answer += pm
else:
    answer += l[0][1] * n

print(answer)