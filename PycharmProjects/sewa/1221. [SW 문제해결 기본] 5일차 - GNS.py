nums1 = {"ZRO" : 0, "ONE" : 1, "TWO" : 2, "THR" : 3, "FOR" : 4, "FIV" : 5,
        "SIX" : 6, "SVN" : 7, "EGT" : 8, "NIN" : 9}
nums = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN","EGT", "NIN"]

def cnums(w):
    return nums.index(w)

def clnums(w):
    return nums[w]

t = int(input())
for _ in range(t):
    tc, n = input().split()
    words = list(input().split())

    words = list(map(cnums, words))
    words.sort()
    words = list(map(clnums, words))

    print(tc)
    print(*words)
