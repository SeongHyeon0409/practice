# -*- coding: utf-8 -*-
#2018.5.20
#20171656
#Digital Logic Design
#implement quine-mccluskey method

#앞으로 해야될일:
# 00- 을 001과 000으로 나누기
# spl 과 pl 분리하기
# 확장성 문제 해결하기

import copy

def DtoB(num):
    if num == 1:
        return '1'
    elif num == 0:
        return '0'
    ans = ''
    while True:
        if num % 2 == 0:
            ans += '0'
        else:
            ans += '1'
        num = int(num / 2)
        if num == 1:
            ans += '1'
            return ans[::-1]

def DtoBPlus(n,variables):
    zero = '0' * (variables - len(n))
    return zero + n

def remindCount(a, b, numVar):
    count = 0
    for i in range(numVar):
        if a[i] != b[i]:
            count += 1
    return count

def remind(a, b, numVar):
    newNum = ''
    for i in range(numVar):
        if a[i] != b[i]:
            newNum += '-'
        else:
            newNum += a[i]
    return newNum

def minimize(minimizeF, nOv):

    minimizeF2 = []
    copyF = copy.deepcopy(minimizeF)

    for j in range(len(minimizeF)):  # 0 1 2
        for i in range(len(minimizeF)):
            if remindCount(minimizeF[j],minimizeF[i],nOv) == 1:
                a = remind(minimizeF[j],minimizeF[i],nOv)
                if a not in minimizeF2:
                    minimizeF2.append(a)
                copyF[j] = 'used'
                copyF[i] = 'used'
    return (minimizeF2, copyF)

def checkEpi(minterms,a):
    b = []
    for i in minterms:
        flag = 0
        for j in range(len(i)):
            if i[j] == a[j] or i[j] == '-' or a[j] == '-':
                continue
            else:
                flag = 1
                break
        if flag == 0:
            b.append(i)

    return b

def quineMccluskey(inNumbers):
    ##error exception
    try:
        inputList2 = inNumbers.split(" ")
        inputList = list(map(int, inputList2))
    except:
        print("Please check the input again.")
        return 0

    numberOfvariables = inputList[0]
    numberOfminterms = inputList[1]
    minterms = inputList[2:]

    ##error exception
    if numberOfminterms != len(minterms):
        print("please input the number of minterms %d ." %numberOfminterms)
        return 0

    if numberOfvariables<3 or numberOfvariables>6:
        print("Please input the number of variables 3 to 6.")
        return 0

    for i in minterms:
        if i >= 2 ** numberOfvariables:
            print("please input minterms smaller than %d ." %(2 ** numberOfvariables))
            return 0
        elif i < 0:
            print("please input positive integer.")

    #degit to binary

    minterms = [DtoB(i) for i in minterms]
    minterms = [DtoBPlus(i, numberOfvariables) for i in minterms]

    print("minterms: ",minterms)
    print("")

    # if numberOfminterms == 1:
    #     result = "EPI "
    #     result += minterms[0]
    #     result += " NEPI "
    #
    #     return result

    unused = []
    minimizeF2 = copy.deepcopy(minterms)
    while(1):
        minimizeF2, temp = minimize(minimizeF2, numberOfvariables)
        for i in temp:
            if i != 'used':
                unused.append(i)
        if not temp:
            break

    print("minterms: ", minimizeF2)
    print("temp: ", temp)
    print("unsued : ", unused ,"\n")


    coverList = {}
    countList = {}
    for i in unused:
        coverList[i] = checkEpi(minterms,i)

    print("coverList : ",coverList)

    for k in minterms:
        count  = 0
        for i in coverList:
            for j in coverList[i]:
                if k == j:
                    count += 1
        countList[k] = count

    print("countList : ",countList)

    countList2 = []
    for i in countList.keys():
        if countList[i] == 1:
            countList2.append(i)

    epiList = []
    nepiList = []

    for i in coverList:
       for j in countList2:
            if j in coverList[i]:
                if i not in epiList:
                    epiList.append(i)

    for i in unused:
        if i not in epiList:
            nepiList.append(i)

    print("")
    #print result

    result = ""
    result += "EPI "
    for i in epiList:
        result += i
        result += " "
    result += "NEPI "
    for i in nepiList:
        result += i
        result += " "

    return result

if __name__ == "__main__":
    inNumbers = input("input[# of input variables][# of minterms][minterm list] : ")
    #inNumbers = "4 8 0 4 8 10 11 12 13 15"
    #inNumbers = "3 6 0 1 2 5 6 7"

    #inNumbers = "3 6 0 1 2 5 6 7"
    print(quineMccluskey(inNumbers))




