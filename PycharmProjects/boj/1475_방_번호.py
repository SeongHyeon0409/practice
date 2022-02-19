import math
n = int(input())

set = {}

for i in range(0, 10):
    set[i] = 0

for i in str(n):
    set[int(i)] += 1

set[6] = math.ceil((set[6] + set[9]) / 2)
set[9] = 0

print(max(set.values()))
