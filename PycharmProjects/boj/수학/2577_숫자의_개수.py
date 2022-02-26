a = int(input())
b = int(input())
c = int(input())

sumv = a * b * c

answer = [0] * 10

for i in str(sumv):
    answer[int(i)] += 1

for i in range(10):
    print(answer[i])