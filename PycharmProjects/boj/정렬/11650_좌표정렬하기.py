import sys
input = sys.stdin.readline

n = int(input().strip())
list = [ list(map(int, input().strip().split())) for _ in range(n) ]

list.sort(key = lambda x : (x[0], x[1]))

for i in list:
    print(*i)
