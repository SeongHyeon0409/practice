import sys

def quicksort2(A, low, high):
    if low >= high:
        return
    q = partition_lomuto(A, low, high)
    quicksort2(A, low, q-1)
    quicksort2(A, q + 1, high)

def partition_lomuto(A, low, high):
    global count_swap
    global count_compare
    pivot = A[low]
    j = low
    for i in range(low+1, high+1):
        count_compare += 1
        if A[i] < pivot:

            j += 1
            A[i], A[j] = A[j], A[i]
            count_swap += 1
    pivot_pos = j
    A[pivot_pos], A[low] = A[low], A[pivot_pos]
    count_swap += 1
    return pivot_pos

def quicksort(A, low, high):
    global count_compare
    if low >= high:
        return
    q = partition_hoare(A, low, high)

    quicksort(A, low, q)
    quicksort(A, q+1, high)

def partition_hoare(A, low, high):
    global count_swap
    global count_compare
    pivot = A[low]
    i = low - 1
    j = high + 1

    while True:
        while True:
            i += 1
            count_compare += 1
            if A[i] >= pivot:
                break

        while True:
            j -= 1
            count_compare += 1
            if A[j] <= pivot:
                break

        if i < j:
            A[i], A[j] = A[j], A[i]
            count_swap += 1
        else:
            return j


if __name__ == "__main__":

    sys.setrecursionlimit(10000000)
    n = int(input())
    for i in range(n):
        count_swap = 0
        count_compare = 0
        a, b, c, d = 0, 0, 0 ,0

        A = list(map(int, sys.stdin.readline().strip().split(" ")))
        A = A[1:]
        B = A[:]

        quicksort(A, 0, len(A)-1)

        a = count_swap
        c = count_compare

        count_swap = 0
        count_compare = 0

        quicksort2(B, 0, len(B)-1)

        b = count_swap
        d = count_compare

        print(a, b, c, d)
