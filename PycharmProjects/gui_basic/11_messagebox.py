from tkinter import *
import tkinter.messagebox as msgbox

root = Tk()
root.title("GUI")
root.geometry('640x480')

def info():
    msgbox.showinfo("알림", "정상적으로 예매 완료되었습니다.")

def warn():
    msgbox.showwarning("경고", "해당 좌석은 매진되었습니다.")

def error():
    msgbox.showerror("에러", "결제 오류가 발생했습니다.")

def okcancel():
    msgbox.askokcancel("확인 / 취소", "해당 좌석은 유아동반석입니다. 예매하시겠습니까?")

def okcancel():
    msgbox.askokcancel("확인 / 취소", "해당 좌석은 유아동반석입니다. 예매하시겠습니까?")

Button(root, command=info, text="알림").pack()
Button(root, command=info, text="경고").pack()
Button(root, command=info, text="에러").pack()
Button(root, command=okcancel, text="확인 취소").pack()


root.mainloop()

