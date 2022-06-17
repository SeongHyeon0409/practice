# 2020.06.17
# Presented by SeongHyeon0409

while True:
    words = input()
    if words == '#':
        break
    count = 0
    for i in words:
        if i == 'a' or i == 'e' or i == 'i'or i == 'o' or i == 'u' \
            or i == 'A' or i == 'E' or i == 'I' or i == 'O' or i == 'U':
            count += 1
    
    print(count)
