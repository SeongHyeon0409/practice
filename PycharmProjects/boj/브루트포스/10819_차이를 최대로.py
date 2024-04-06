from itertools import permutations
import sys

# 주어진 값 입력
n = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))

# # permutation 저장(per: reference of permutation tuples)
# per = permutations(a)
# ans = 0
#
# # 순열마다 차이를 더해(s), ans 보다 크면 ans를 update
# for i in per:
#     s = 0
#     for j in range(len(i) - 1):
#         s += abs(i[j] - i[j + 1])
#     if s > ans:
#         ans = s
#
# print(ans)

a = []
permutation = []
visited = [0] * n
def backtracking():
    if len(a) == n:
        permutation.append(a[:])
        return

    for i in range(n):
        if not visited[i]:
            visited[i] = 1
            a.append(nums[i])
            backtracking()
            a.pop()
            visited[i] = 0

backtracking()
ans = 0
for num in permutation:
    tmp = 0
    for i in range(1, n):
        tmp += abs(num[i] - num[i-1])

    ans = max(ans, tmp)

print(ans)



