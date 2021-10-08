def countingsort(A, k):

    C = [0 for i in range(10)]
    B = [0 for i in range(len(A))]

    for j in A:
        C[j] += 1

    for i in range(k):
        C[i+1] += C[i]

    for j in reversed(range(len(A))):
        B[C[A[j]]-1] = A[j]
        C[A[j]] -= 1

    return B

if __name__ == '__main__':
    A = [4, 1, 2, 3, 4, 6, 8]
    countingsort(A, max(A))