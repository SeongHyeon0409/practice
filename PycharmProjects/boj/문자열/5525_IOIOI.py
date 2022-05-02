# 2020.05.02
# Presented by SeongHyeon0409
# 문자열

n = int(input())
m = int(input())
s = input()

# solution 1 but timeout
# p = 'I'
# ans = 0
#
# for i in range(n):
#     p += 'OI'
# print(p)
#
# for i in range(m):
#     if s[i:i+len(p)] == p:
#         ans += 1
#
# print(ans)

ans, i, count = 0, 0, 0

while i < (m-1):
    if s[i:i+3] == 'IOI':
        i += 2
        count += 1
        if count == n:
            ans += 1
            count -= 1
    else:
        i += 1
        count = 0

print(ans)
