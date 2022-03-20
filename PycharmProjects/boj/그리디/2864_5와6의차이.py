A, B = input().split()
amax, amin = A.replace('5', '6'), A.replace('6', '5')
bmax, bmin = B.replace('5', '6'), B.replace('6', '5')

print(int(amin) + int(bmin), end=' ')
print(int(amax) + int(bmax))