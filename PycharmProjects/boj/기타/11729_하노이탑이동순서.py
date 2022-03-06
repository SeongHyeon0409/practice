n = int(input())
count = 0
move = []

def hanoi(n, start, to, via):
    global count
    if n == 1:
        move.append([start, to])
        count += 1
    else:
        hanoi(n-1, start, via, to)
        move.append([start, to])
        count += 1
        hanoi(n-1, via, to, start)


hanoi(n, 1, 3, 2)
print(count)
for i in move:
    print(*i)