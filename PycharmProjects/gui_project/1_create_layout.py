from tkinter import *

root = Tk()
root.title("GUI")
#root.geometry("640x480+300+100") # 가로 * 세로 + x좌표 + y좌표

# 파일 프레임 (파일 추가, 선택 삭제)
file_frame = Frame(root)
file_frame.pack()

btn_add_file = Button(file_frame, padx=5, pady=5, width=12, text="파일추가")
btn_add_file.pack(side="left")

btn_del_file = Button(file_frame, padx=5, pady=5, width=12, text="선택삭제")
btn_del_file.pack(side="right")

root.resizable(False, False) # x, y 값 변경 불가 ( 창 크기 변경 불가 )
root.mainloop()
