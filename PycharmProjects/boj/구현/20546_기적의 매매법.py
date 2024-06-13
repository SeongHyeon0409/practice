c = int(input())
s = list(map(int, input().split()))

jc, sc = c, c
js, ss = 0, 0
upstack = 0
lowstack = 0

for i in range(len(s)):
    # 준현
    if s[i] <= jc:
        js += jc//s[i]
        jc = jc%s[i]
    # 성민
    if i > 0:
        if s[i] > s[i-1]:
            lowstack = 0
            upstack += 1
        elif s[i] < s[i-1]:
            upstack = 0
            lowstack += 1
    if lowstack >= 3:
        ss += sc//s[i]
        sc = sc%s[i]
    elif upstack >= 3:
        sc += ss * s[i]
        ss = 0

junhyeon = jc + s[-1] * js
seongmin = sc + s[-1] * ss
print("SAMESAME" if junhyeon == seongmin else ("BNP" if junhyeon > seongmin else "TIMING"))