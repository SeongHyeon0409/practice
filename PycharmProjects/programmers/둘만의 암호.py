# 2023.02.02
# Written by SeongHyeon0409

def solution(s, skip, inx):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    available = [c for c in alphabet if c not in skip]
    new_char = []
    for c in s:
        new_index = (available.index(c) + inx) % len(available)
        new_char.append(available[new_index])
    return ''.join(new_char)