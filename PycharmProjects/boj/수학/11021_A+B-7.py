import sys
input = sys.stdin.readline

n = int(input().strip())
for i in range(n):
    a, b = map(int, input().strip().split())
    print("Case #{0}: {1}".format(i+1, a + b))