import sys

def cut_rod(p,n):
    if n == 0:
        return 0
    q = -9999999
    for i in range(1, n+1):
        q = max(q, p[i] + cut_rod(p, n-i))
    return q

def memorized_cut_rod(p, n):
    r = [-1]*(n+1)
    return memorized_cut_rod_aux(p, n, r)

def memorized_cut_rod_aux(p, n, r):
    if r[n] >= 0:
        return r[n]
    if n == 0:
        return 0
    else:
        q = -999999
        for i in range(1, n+1):
            q = max(q, p[i] + memorized_cut_rod_aux(p, n-i, r))
    r[n] = q
    return q

def print_bottom(p, n):
    r, s = bottom_up_cut_rod(p, n)
    while n > 0:
        print(s[n])
        n -= s[n]

def bottom_up_cut_rod(p, n):
    r = [-1]*(n+1)
    s = [-1]*(n+1)
    r[0] = 0
    for i in range(1, n+1):
        q = -99999
        for j in range(1, i+1):
            if q < p[j] + p[i-j]:
                q = max(q, p[j] + p[i-j])
                s[i] = j
        r[i] = q

    return r, s

    # r = [-1]*(n+1)
    # r[0] = 0
    # for j in range(1, n+1):
    #     q = -99999
    #     for i in range(1, j+1):
    #         q = max(q, p[i]+r[j-i])
    #     r[j] = q
    #     print(r)
    # return r[n]

def ex_bottom_up_cut_rod(p,n):
    r = [-1]*(n+1)
    s = [-1]*(n+1)
    r[0] = 0
    for j in range(1, n+1):
        q = -99999
        for i in range(1, j+1):
            if q < (p[i] + r[j-i]):
                q = p[i] + r[j-i]
                s[j] = i
        r[j] = q
    return r, s

def print_cut_rod_solution(p, n):
    r ,s = ex_bottom_up_cut_rod(p, n)
    while n > 0:
        print (s[n])
        n = n - s[n]

sys.setrecursionlimit(999999)
p = [0, 1, 5, 8, 9, 10, 17, 17, 20, 24, 30]
# print(memorized_cut_rod(p,10))
# print(bottom_up_cut_rod(p, 10))
# print_cut_rod_solution(p, 5)
print_bottom(p, 10)