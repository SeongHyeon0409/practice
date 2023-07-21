b = [ 1, 2, 3]

def a(num, b):
    return num + b
print(list(map(lambda x: a(x, 2),b)))