from collections import Counter
import sys

input = sys.stdin.readline

n = int(input().strip())
nums = [int(input().strip()) for _ in range(n)]


print(round(sum(nums)/n))

print(nums[n//2])

# cnt = Counter(nums).most_common(2)
#
# if len(nums) > 1 and cnt[1][1] == cnt[0][1]:
#     print(cnt[1][0])
# else:
#     print(cnt[0][0])


c = dict()

for i in nums:
    if i not in c:
        c[i] = 1
    else:
        c[i] += 1

c = sorted(c.items(), key=lambda x: x[1], reverse=True)

maxb = c[0][1]
d = []

for i in c:
    if i[1] == maxb:
        d.append(i[0])

if len(d) > 1:
    print(d[1])
else:
    print(c[0][0])

print(max(nums) - min(nums))
