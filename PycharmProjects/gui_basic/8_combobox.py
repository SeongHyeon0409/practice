from tkinter import *
import tkinter.ttk as ttk

root = Tk()
root.title("GUI")
root.geometry('640x480')

values = [str(i) + "일" for i in range(1, 32)]
combobox = ttk.Combobox(root, height=5, values=values, state="readonly") # 읽기 전용
combobox.pack()
combobox.set("카드 결제일") # 최초 목록 제목 설정
#combobox.current(0) # 0번째 인덱스 값 선택

def btncmd():
    print(combobox.get())

btn = Button(root, text="선택", command=btncmd)
btn.pack()

root.mainloop()

