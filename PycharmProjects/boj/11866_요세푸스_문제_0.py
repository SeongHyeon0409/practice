n, k = map(int, input().split())
ary = [i for i in range(1, n+1)]
idx = k - 1
answer = []


while ary:
    while idx >= len(ary):
        idx = idx - len(ary)
    answer.append(ary.pop(idx))
    idx += k-1


print("<", end='')
for i in range(n-1):
    print("{0}, ".format(answer[i]), end='')
print("{0}>".format(answer[n-1]))