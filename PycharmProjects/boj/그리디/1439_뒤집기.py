S = list(input()) + [2]

z = 0
o = 0

for i in range(0, len(S)-1):
    if S[i] == '1':
        if S[i] != S[i+1]:
            z += 1
    else:
        if S[i] != S[i+1]:
            o += 1

print(min(z, o))
