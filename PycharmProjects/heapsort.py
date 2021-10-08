"""
def max_heapify(A, i):
    global A_heap_size
    l = 2 * i + 1
    r = 2 * i + 2
    if l <= A_heap_size and A[l] > A[i]:
        largest = l
    else:
        largest = i
    if r <= A_heap_size and A[r] > A[largest]:
        largest = r
    if largest != i:
        A[largest], A[i] = A[i], A[largest]
        max_heapify(A, largest)

def heap_sort(A):

    global A_heap_size
    A_heap_size = len(A) - 1
    for i in range(int(len(A) /2) - 1, -1, -1):
        max_heapify(A, i)

    for i in range(len(A) - 1 , 0, -1):
        A[i], A[0] = A[0], A[i]
        A_heap_size = A_heap_size - 1
        max_heapify(A, 0)
"""


def max_heapify(A, i):
    l, r = i*2+1, i*2+2
    if l <= heap_size and A[l] > A[i]:
        largest = l
    else:
        largest = i
    if r <= heap_size and A[r] > A[largest]:
        largest = r
    if largest != i:
        A[i], A[largest] = A[largest], A[i]
        max_heapify(A, largest)

def solution(A, k):
    global heap_size
    heap_size = len(A) - 1
    for i in range(int(len(A)/2)-1, -1, -1):
        max_heapify(A, i)

    for i in range(len(A)-1, k-1, -1):
        A[i],A[0] = A[0],A[i]
        heap_size -= 1
        max_heapify(A, 0)


A = [4,1,3,2,16,9,10,14,8,7]

solution(A,1)
print(A)
