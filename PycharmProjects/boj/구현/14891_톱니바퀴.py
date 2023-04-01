# 2023.03.27
# Written by SeongHyeon0409

# s, n 서로 반대 방향 회전
# 같은 극 회전 x
import copy

chain = []
for i in range(4):
    chain.append(input())

n = int(input())
dir = 1
def clock_wise(lst):
    global dir
    if dir == 1:
        lst = lst[7:] + lst[:7]
        dir = -1
    else:
        lst = lst[1:] + lst[:1]
        dir = 1
    return lst

for i in range(n):
    # 중간 시작 , 끝 시작
    # 돌아가기 전 같은지 확인하고 뎔랴야함.
    # 연쇄 작용이 아니라 한번에 회전...
    a, b = map(int, input().split())
    dir = b
    chainc = copy.deepcopy(chain)
    chainc[a-1] = clock_wise(chain[a-1])
    if a == 1:
        for j in range(3): #0 ,1, 2
            if chain[j][2] != chain[j+1][6]:
                chainc[j+1] = clock_wise(chain[j+1])
            else:
                break
    elif a == 4:
        for j in range(3,0,-1): #3, 2, 1
            if chain[j][6] != chain[j-1][2]:
                chainc[j-1] = clock_wise(chain[j-1])
            else:
                break
    elif a == 2:
        if chain[0][2] != chain[1][6]:
            dir = -1 * b
            chainc[0] = clock_wise(chain[0])
        if chain[1][2] != chain[2][6]:
            dir = -1 * b
            chainc[2] = clock_wise(chain[2])
            if chain[2][2] != chain[3][6]:
                chainc[3] = clock_wise(chain[3])
    elif a == 3:
        if chain[3][6] != chain[2][2]:
            dir = -1 * b
            chainc[3] = clock_wise(chain[3])
        if chain[2][6] != chain[1][2]:
            dir = -1 * b
            chainc[1] = clock_wise(chain[1])
            if chain[0][2] != chain[1][6]:
                chainc[0] = clock_wise(chain[0])
    chain = chainc

ans = 0
s = 1
for i in chain:
    if i[0] == "1":
        ans += s
    s *= 2

print(ans)