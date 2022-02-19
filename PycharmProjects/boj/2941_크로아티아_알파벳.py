word = input()
c_a = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]

i = 0
answer = 0
while i < len(word):
    if i+2 < len(word):
        if word[i] + word[i+1] + word[i+2] in c_a:
            answer += 1
            i += 3
            continue
    if i+1 < len(word):
        if word[i] + word[i+1] in c_a:
            answer += 1
            i += 2
            continue

    answer += 1
    i += 1

print(answer)

# croatia = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
# word = input()
#
# for i in croatia :
#     word = word.replace(i, '*')
# print(len(word))