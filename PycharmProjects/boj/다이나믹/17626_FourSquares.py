n = int(input())
dp = [0, 1]

for i in range(2, n+1):

    minv = 1e9
    j = 1

    while (j**2) <= i:
        minv = min(minv, dp[i - (j**2)])
        j += 1

    dp.append(minv + 1)

print(dp[n])

# n = int(input())
#
# sqa = [i**2 for i in range(1, 225)]
#
# dp = [0] * (n+1)
# dp[1] = 1
#
# for i in range(1, n+1):
#     temp = []
#     for j in sqa:
#         if j <= i:
#             temp.append(dp[i-j])
#     if temp:
#         dp[i] = min(temp) + 1
#
# print(dp[n])
