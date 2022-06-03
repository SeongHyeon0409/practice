from math import log



def digit16(n, d):
    n = n >> d * 4
    return n & 0xf

def countingsort(A, d):

    C = [0 for i in range(16)]
    B = [0 for i in range(len(A))]

    for i in A:
        C[digit16(i[0], d)] += 1
    for i in range(15):
        C[i+1] += C[i]
    for j in reversed(range(len(A))):
        B[C[digit16(A[j][0], d)]-1] = A[j]
        C[digit16(A[j][0], d)] -= 1
    return B

if __name__ == '__main__':


    n = int(input())
    c = []
    for i in range(n):
        a, b = input().strip().split(' ')
        c.append((int(a), b))


    B = radixsort(c)

    print (B)

    for i in range(len(B)):
        print(B[i][0], B[i][1])