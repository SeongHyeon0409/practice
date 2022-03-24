a = input()
l = []

for i in a:
    if not l and i == 'U':
        l.append(i)
    elif l == ['U'] and i == 'C':
        l.append(i)
    elif l == ['U', 'C'] and i == 'P':
        l.append(i)
    elif l == ['U', 'C', 'P'] and i == 'C':
        l.append(i)

if l == ['U', 'C', 'P', 'C']:
    print("I love UCPC")
else:
    print("I hate UCPC")
