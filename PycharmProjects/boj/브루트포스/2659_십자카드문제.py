# 2020.04.13
# Presented by SeongHyeon0409

n = int(''.join(list(input().split())))

def get_clock(n):
    cross = list(str(n))
    nums = []
    for j in range(4):
        cross.append(cross.pop(0))
        nums.append(int(''.join(cross)))
        nums.sort()

    return(nums[0])

clock_num = get_clock(n)
ans = 1

for i in range(1111, clock_num):
    nums = []
    cross = list(str(i))
    if '0' not in cross:
        if i == get_clock(i):
            ans += 1

print(ans)
#print(sorted(crossnums).index(n) + 1)
