n = int(input())

l = sorted(list(map(int, input().split())))

print(l[(n-1)//2])