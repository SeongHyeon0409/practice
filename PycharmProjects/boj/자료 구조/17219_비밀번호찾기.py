# 2020.04.13
# Presented by SeongHyeon0409

import sys

input = sys.stdin.readline

n, m = map(int, input().strip().split())

site = {}

for i in range(n):
    adress, password = input().strip().split()
    site[adress] = password

for i in range(m):
    print(site[input().strip()])