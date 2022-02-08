from multi_transition import multi_transition
from bit_stuffing import bit_unstuff

def changeTobit(inputData):

    outputData = []

    if inputData[0] == "+":
        outputData.append("1")
    elif inputData[0] == "0":
        outputData.append("0")

    for i in range(1, len(inputData)):
        if inputData[i] == inputData[i-1]:
            outputData.append("0")
        else:
            outputData.append("1")

    return ''.join(outputData)


if __name__ == "__main__":

    inputData = input("bit_stream입력(ex +0-0++0-0): ")
    bit_ary = list(inputData)

    for i in bit_ary:
        if i != "0" and i != "+" and i != "-":
            print("알맞은 데이터를 입력하세요.")
            exit()

    outputData = changeTobit(bit_ary)
    print("MLT-3 처리 결과 : ",outputData)
    print("bit-unstuffing 처리 결과 : ",bit_unstuff(outputData))

