n = int(input())

nums = list(map(int, input().split()))

nums.sort()

answer = 0
a = 0

for i in nums:
    a += i
    answer += a

print(answer)