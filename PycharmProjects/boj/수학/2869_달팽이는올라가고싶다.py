import math
A, B, V = map(int, input().split())

answer = math.ceil((V-A) / (A-B)) + 1


print(answer)

