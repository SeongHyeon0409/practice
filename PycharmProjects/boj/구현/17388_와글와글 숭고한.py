# 2020.07.06
# Written by SeongHyeon0409

s, k, h = map(int, input().split())
c = [[s, "Soongsil"], [k, "Korea"], [h, "Hanyang"]]
c.sort(key=lambda x:x[0])
if s + k + h >= 100:
    print("OK")
else:
    print(c[0][1])
