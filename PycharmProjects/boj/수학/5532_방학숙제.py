# 2020.06.18
# Presented by SeongHyeon0409
import math

L = int(input())
A = int(input())
B = int(input())
C = int(input())
D = int(input())

A = math.ceil(A/C)
B = math.ceil(B/D)

print(L-max(A,B))