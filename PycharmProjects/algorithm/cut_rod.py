# def cut_rod(p, n):
#     if n == 0:
#         return 0
#     q = -99999
#     for i in range(1, n+1):
#         q = max(q, p[i] + cut_rod(p, n-i))
#
#     return q
#
# def memorized_cut_rod(p, n):
#     r = [-1] * (n+1)
#     return cut_rod2(p,n,r)
#
# def cut_rod2(p,n,r):
#     if r[n] >= 0:
#         return r[n]
#     if n == 0:
#         return 0
#     q = -99999
#     for i in range(1, n+1):
#         q = max(q, p[i] + cut_rod2(p, n-i, r))
#
#     r[n] = q
#     return q
#
# def botoomup(p, n):
#     dp = [0] * (n+1)
#     s = [0] * (n+1)
#     for i in range(1, n+1):
#         q = -99999
#         for j in range(1, i+1):
#             if q < (p[j] + dp[i-j]):
#                 q = p[j] + dp[i-j]
#                 s[i] = j
#
#         dp[i] = q
#
#     return dp, j
#
# def print1(p, n):
#     dp, j = bottom_up(p, n)
#     while n>0:
#         print (j[n])
#         n -= j[n]
#
# def asdf(p, n):
#     r = [-1] * (n+1)
#     return fasf(p, n, r)
#
# def fasf(p, n, r):
#     if r[n] > 0:
#         return r[n]
#     if n == 0:
#         return 0
#     q = -999999
#     for i in range(1, n+1):
#         if q < fasf(p, n-i, r):
#             q =  p[i] + fasf(p, n-i, r)
#
#     r[n] = q
#
#     return q
#
#
# def bottom_up(p, n):
#     dp = [0] * (n+1)
#     s = [0] * (n+1)
#     for i in range(0, n+1):
#         q = -99999
#         for j in range(0, i+1):
#             if p[j] + dp[i-j] > q:
#                 q = p[j] + dp[i-j]
#                 s[i] = j
#
#         dp[i] = q
#
#     return dp, s
#
# def print_bottom_up(p, n):
#     dp, s = bottom_up(p, n)
#     while n>0:
#         print (s[n])
#         n -= s[n]

def print_bottom_up(p, n):
    r = bottom_up(p, n)

    while n > 0:
        print(r[n])
        n -= r[n]

def bottom_up(p, n):
    dp = [0] * (n+1)
    r = [0] * (n+1)

    for i in range(n+1):
        q = -99999
        for j in range(i+1):
            if q < p[j] + dp[i-j]:
                q = p[j] + dp[i-j]
                r[i] = j
        dp[i] = q

    return r

def m_cut_rod(p,n):
    r = [-1] * (n+1)
    return cut_rod(p,n,r)

def cut_rod(p, n, r):
    if r[n] > 0:
        return r[n]
    if n == 0:
        return 0
    q = -1

    for i in range(1, n+1):
        q = max(q, p[i] + cut_rod(p, n-i, r))

    r[n] = q

    return q

p = [0, 1, 5, 8, 9, 10, 17, 17, 20, 24, 30]

print(m_cut_rod(p, 10))
# print(memorized_cut_rod(p, 10))

print_bottom_up(p,4)

