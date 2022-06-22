from tkinter import *

root = Tk()
root.title("GUI")
root.geometry('640x480')

btn1 = Button(root, text="버튼1")
btn2 = Button(root, text="버튼2")

btn1.pack()
btn2.pack()

root.mainloop()

