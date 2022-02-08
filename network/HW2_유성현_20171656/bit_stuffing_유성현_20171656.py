def bit_stuff(inputData):
    outputData = inputData.replace("11111", "111110")
    return outputData
if __name__ == "__main__":

    inputData = input("bit 입력(ex 10010001): ")
    bit_ary = list(inputData)

    try:
        bit_ary = [int(i) for i in bit_ary]
    except:
        print("숫자만 입력하세요.")
        exit()

    for i in bit_ary:
        if i != 1 and i != 0:
            print("1과 0 만입력하세요")
            exit()

    stuffedData = bit_stuff(inputData)
    print(stuffedData)