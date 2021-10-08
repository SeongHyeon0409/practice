def brute_force(A, B): # O(n^3)
    n = len(A)
    c = [[0 for i in range(n)] for j in range(n)]
    for i in range(0, n):
        for j in range(0, n):
            c[i][j] = 0
            for k in range(0, n):
                c[i][j] = c[i][j] + A[i][k] * B[k][j]

    return c
"""
def divide_conquer(A, B):

    n = 0

    if type(A) == list:
        n = len(A)

    c = [[0 for i in range(n)] for j in range(n)]

    if n == 1:
        c[0][0] = A[0][0] * B[0][0]
    else:
        c[0][0] = divide_conquer(A[0][0], B[0][0])
        + divide_conquer(A[0][1], B[1][0])
        c[0][1] = divide_conquer(A[0][0], B[0][1])
        + divide_conquer(A[0][1], B[1][1])
        c[1][0] = divide_conquer(A[1][0], B[0][0])
        + divide_conquer(A[1][1], B[1][0])
        c[1][1] = divide_conquer(A[1][0], B[0][1])
        + divide_conquer(A[1][1], B[1][1])

    return c
"""

if __name__ == "__main__":

    A = [[1,2,3,6]
        ,[4,6,7,3]
        ,[4,4,3,2]
        ,[2,2,3,6]]


    B = [[6,8,3,2]
        ,[1,8,4,7]
        ,[2,2,3,6]
        ,[2,1,2,6]]


    c = brute_force(A, B)


    for i in range(len(A)):
        print(c[i])



# 2차원 배열 선언방법

# c = [[0 for i in range(n)] for j in range(n)]

""" 
board = [[0] * 4] * 4
for i in range(4):
    print(board[i])
"""