from collections import deque

t = int(input())

for _ in range(t):
    n, m = map(int, input().split()) # m = 우선권
    f = sorted(list(map(int, input().split())), reverse=True)
    f = deque(f)
    ans = 0

    if len(f) % 2 == 1:
        f.append(0)

    diff = []


    while len(f) > 1:
        diff.append(f[0] - f[1])
        f.popleft()
        ans += f.popleft()

    diff.sort(reverse=True)
    diff = deque(diff)

    for i in range(m):
        if diff and diff[0] == 0:
            break
        if not diff:
            break
        ans += diff.popleft()
        m -= 1


    print(ans)

    # 차이가 큰 것 선택,,
    # 1 2 3 4 5 10 11 12