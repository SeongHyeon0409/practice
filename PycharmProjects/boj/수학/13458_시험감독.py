# 2023.02.09
# Written by SeongHyeon0409

n = int(input())
a = list(map(int, (input().split())))
b ,c = map(int, input().split())

answer = n
for i in a:
    if i <= b:
        continue
    remainder = i - b
    answer += (remainder // c if remainder % c == 0 else remainder // c + 1)
print(answer)