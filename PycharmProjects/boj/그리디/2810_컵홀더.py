n = int(input())
a = input()+"a"
answer = n
i, l = 0, 0

while i < n:
    if a[i] + a[i+1] == 'LL':
        l += 1
        i += 1
    i += 1


if l > 1:
    answer -= (l-1)

print(answer)
