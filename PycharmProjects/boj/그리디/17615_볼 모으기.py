n = int(input())
balls = input().strip()

ans = float('inf')

#우측으로 레드
tb = balls.rstrip('R')
ans = min(ans, tb.count('R'))

#좌측으로 레드
tb = balls.lstrip('R')
ans = min(ans, tb.count('R'))

#우측으로 블루
tb = balls.rstrip('B')
ans = min(ans, tb.count('B'))

#좌측으로 블루
tb = balls.lstrip('B')
ans = min(ans, tb.count('B'))

print(ans)