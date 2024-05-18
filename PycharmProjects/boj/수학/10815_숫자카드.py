def binary_search(start, end, target):
    if start > end:
        return 0
    mid = (start + end) // 2
    if cards[mid] > target:
        return binary_search(start, mid-1, target)
    elif cards[mid] == target:
        return 1
    else:
        return binary_search(mid+1, end, target)


n = int(input())
cards = list(map(int, input().split()))
cards.sort()
m = int(input())
scards = list(map(int, input().split()))

for c in scards:
    print(binary_search(0, n-1, c), end=" ")
