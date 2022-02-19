def solution1(param0):
    max = param0[0]
    for i in range(0, len(param0)):
        profit = 0
        for j in range(i, len(param0)):
            profit = profit + param0[j]
            if (profit > max):
                max = profit

    return max

left , right, sum = 0 ,1 ,2
print(left, right, sum)