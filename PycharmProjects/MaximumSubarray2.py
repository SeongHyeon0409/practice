import sys
sys.setrecursionlimit(10 ** 7)

def solution(param0):
    left, right, sum = fms(param0, 0, len(param0) -1 )
    return sum


def fms(A, low, high):
    if high == low:
        return low, high, A[low]
    else:
        mid = int((low + high) / 2)
        left_low, left_high, left_sum = fms(A, low, mid)
        right_low, right_high, right_sum = fms(A, mid + 1, high)
        cross_low, cross_high, cross_sum = fmcs(A, low, mid, high)
        if left_sum >= right_sum and left_sum >= cross_sum:
            return left_low, left_high, left_sum
        elif right_sum >= left_sum and right_sum >= cross_sum:
            return right_low, right_high, right_sum
        else:
            return cross_low, cross_high, cross_sum

def fmcs(A, low, mid, high):
    left_sum = A[mid]
    max_left = 0
    max_right = 0
    sum = 0
    for i in range(mid, low-1, -1):
        sum = sum + A[i]
        if sum > left_sum:
            left_sum = sum
            max_left = i

    right_sum = A[mid + 1]
    sum = 0
    for j in range(mid + 1, high+1):
        sum = sum + A[j]
        if sum > right_sum:
            right_sum = sum
            max_right = j
    return max_left, max_right, left_sum + right_sum

a = [21, 3, -5, 45, -66, -75, -95]
print(solution(a))