from tkinter import *

root = Tk()
root.title("GUI")
root.geometry('640x480')

listbox = Listbox(root, selectmod="extended", height=0) # extended : 여러 개, single : 한 개
listbox.insert(0, "사과")
listbox.insert(1, "딸기")
listbox.insert(2, "바나나")
listbox.insert(END, "수박")
listbox.pack()

def btncmd():
    # 맨 뒤에 항목을 삭제
    #listbox.delete(END)

    # 개 수 확인
    #print("리스트에는", listbox.size(), "개가 있어요.")

    # 항목 확인 (시작 idx, 끝 idx)
    #print("1번째부터 3번째까지의 항목 : ", listbox.get(0, 2))

    # 선택된 항목 확인 (위치로 반환)
    print("선택된 항목", listbox.curselection())

btn = Button(root, text="클릭", command=btncmd)
btn.pack()

root.mainloop()

