m = 2
def compare(a, b):
    i = 0
    j = 0
    c = m
    while i <= len(a):
        if a[i] == b[j]:
            i += 1
            j += 1
        elif a[i] == '.':
            for k in range(0, m+1):
                if a[i] == b[j+k]:
                    i += 1
                    j += 1
                    break
                
        else:
            break

    return(b)

print(compare('badword', 'bad.ord'))