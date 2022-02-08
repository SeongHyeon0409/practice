def multi_transition(data):

    bit_ary = [int(i) for i in data]

    def transition(current_level, last_nonzero):
        if current_level != "0":
            return "0"
        elif current_level == "0":
            if last_nonzero == "+":
                return "-"
            elif last_nonzero == "-":
                return "+"

    mlt_list = []
    last_nonzero_level = "-"
    if bit_ary[0] == 0:
        mlt_list.append("0")
    else:
        mlt_list.append("+")

    for i in range(0, len(bit_ary)-1):
        if bit_ary[i+1] == 0:
            mlt_list.append(mlt_list[i])
        elif bit_ary[i+1] == 1:
            mlt_list.append(transition(mlt_list[i],last_nonzero_level))
            if mlt_list[i] != 0:
              last_nonzero_level = mlt_list[i]

    return ''.join(mlt_list)

def r_multi_transition(data):

    inputData = list(data)

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

    a = input("bit 입력(ex 10010001): ")
    bit_ary = list(a)

    try:
        bit_ary = [int(i) for i in bit_ary]
    except:
        print("숫자만 입력하세요.")
        exit()

    for i in bit_ary:
        if i != 1 and i != 0:
            print("1과 0 만입력하세요")
            exit()

    print(multi_transition(bit_ary))
