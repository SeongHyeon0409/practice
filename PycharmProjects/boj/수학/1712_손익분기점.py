A, B, C = map(int, input().split())
#A + B * n = 생산비용 C = 판매비용

if B == C:
    n = -1
else:
    n = A//(C-B) + 1

print(int(n) if n>0 else -1 )

