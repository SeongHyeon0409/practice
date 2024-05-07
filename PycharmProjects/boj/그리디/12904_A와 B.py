import sys
sys.setrecursionlimit(99999)
s = input()
t = input()

# 1. A추가
# 2. 뒤집고 B추가
# t를 s로

while len(t) > len(s):
    if t[-1] == "A":
        t = t[:-1]
    else:
        t = t[:-1]
        t = t[::-1]

if t == s:
    print(1)
else:
    print(0)