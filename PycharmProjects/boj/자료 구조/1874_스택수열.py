# n = int(input())
# stack = []
# nums = [int(input()) for _ in range(n)]
# a = 0
# i = 1
# answer = []
# flag = 0
#
# while True:
#
#     while stack and stack[-1] == nums[a]:
#         a += 1
#         stack.pop()
#         answer.append("-")
#
#     if i > n and not stack:
#          break
#     elif i > n and stack:
#         flag = 1
#         break
#
#     stack.append(i)
#     answer.append("+")
#     i += 1
#
# if flag:
#     print("NO")
# else:
#     print(*answer, sep="\n")

#-------------------------------------------------------------


n = int(input())
stack = []
nums = [int(input()) for _ in range(n)]
answer = []
current = 0

for i in range(1, n+1):

    stack.append(i)
    answer.append('+')

    while stack and stack[-1] == nums[current]:
        answer.append('-')
        stack.pop()
        current += 1


if stack:
    answer = ["NO"]

for a in answer:
    print(a)
